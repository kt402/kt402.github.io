import dataclasses
import json
from prettytable import PrettyTable

# Set these variables based on format of the sheet
from extraction.extract_model import Recommendations, ACRound

FILENAME = "2022-12-ac.csv"
NUM_HEROES_TO_SAVE = 2
NUM_ROUNDS_TO_TUCK = 8
ROW_IDX_START = 2
ROW_IDX_END = 26
COL_IDX_NAME = 1
COL_IDX_SERVER = 2
COL_IDX_POWER = 3
USE_TUCK_HERO_ZERO = True

"""
Extraction json format example:
[
  {
    "round": 1,
    "opponent": "UNICUS",
    "server": "386",
    "power_billions": 3.6,
    "recommendation_hero": 26,
    "recommendation_flags": "*"
  },
  ...
]
"""


def main():
    recommendations = Recommendations(
        num_heroes_to_save=NUM_HEROES_TO_SAVE,
        num_rounds_tucking=NUM_ROUNDS_TO_TUCK,
        additional_strategies="Flags - use strategy or courage (or brutality if weak) for all rounds except for "
                              "rounds we are dropping",
        flags_key={
            "S/C/B": "Strategy or courage preferred. brutality, if weak hero",
            "-": "Any or no flag",
        },
        rounds=calculate_ac_rounds(),
    )
    write_file(recommendations)


def calculate_ac_rounds() -> list[ACRound]:
    ac_rounds = load_ac_rounds_from_csv()
    ac_rounds.sort(key=lambda r: r.power_billions, reverse=True)

    hero = NUM_HEROES_TO_SAVE + 1

    tuck_hero = hero + len(ac_rounds) - NUM_ROUNDS_TO_TUCK

    for i, ac_round in enumerate(ac_rounds):
        if i < NUM_ROUNDS_TO_TUCK:
            ac_round.recommendation_hero = tuck_hero
            ac_round.recommendation_flags = "-"
            if USE_TUCK_HERO_ZERO:
                tuck_hero = 0
            else:
                tuck_hero += 1
        else:
            ac_round.recommendation_hero = hero
            ac_round.recommendation_flags = "S/C/B"
            hero += 1

    ac_rounds.sort(key=lambda r: r.recommendation_hero)
    print_pretty_table(ac_rounds, "Sorted by hero")

    ac_rounds.sort(key=lambda r: r.round)
    print_pretty_table(ac_rounds, "Sorted by round")

    return ac_rounds


def write_file(recommendations: Recommendations):
    with open("../src/views/data.ts", 'w') as out:
        json_str = json.dumps(recommendations, indent=2, cls=EnhancedJSONEncoder)
        out.write(f"export const data = {json_str};")


def print_pretty_table(ac_rounds: list[ACRound], title: str):
    table = PrettyTable()
    table.title = title
    table.field_names = ["Round", "Opponent", "Server", "Power(B)", "Hero Rec", "Flags Rec"]
    for r in ac_rounds:
        table.add_row([r.round, r.opponent, r.server, r.power_billions, r.recommendation_hero, r.recommendation_flags])
    print(table)


def load_ac_rounds_from_csv() -> list[ACRound]:
    ac_rounds: list[ACRound] = []

    with open(f"files/{FILENAME}") as f:
        lines = f.readlines()
        round_num = 0
        for line in lines[ROW_IDX_START:ROW_IDX_END + 1]:
            cols = line.split(',')
            round_num += 1
            opponent = cols[COL_IDX_NAME]
            server = cols[COL_IDX_SERVER]
            power_billions = float(cols[COL_IDX_POWER])
            ac_rounds.append(ACRound(round_num, opponent, server, power_billions, 0, ""))
    return ac_rounds


class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)





main()



