import dataclasses
import json
from prettytable import PrettyTable

# Set these variables based on format of the sheet
from extraction.extract_model import Recommendations, ACRound, FlagRec


FILENAME = "2023-03-ac.csv"
NUM_HEROES_TO_SAVE = 4
NUM_ROUNDS_TO_TUCK = 6

ADDITIONAL_STRATEGIES = \
    "Flags - use strategy or courage (or brutality if weak) for all rounds except for " + \
    "rounds we are dropping"

FLAGS_RECS = [
    FlagRec("S", [10, 18, 20, 3, 12]),
    FlagRec("SC", [14, 15, 9, 17, 1, 7, 11, 23]),
]
DEFAULT_FLAG_REC = "any"
FLAGS_KEY = {
    "S": "strategy",
    "SC": "strat-or-courage-brut-if-weak"
}

COL_IDX_ROUND = 0
COL_IDX_NAME = 1
COL_IDX_SERVER = 2
COL_IDX_POWER = 8
COL_IDX_MEMBERS = 9
COL_IDX_COMMENT = 12

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
        additional_strategies=ADDITIONAL_STRATEGIES,
        flags_key=FLAGS_KEY,
        rounds=calculate_ac_rounds(),
    )
    write_file(recommendations)


def flag_rec_lookup() -> dict[int: str]:
    lookup: dict[int: str] = {}
    for flag_rec in FLAGS_RECS:
        for rd in flag_rec.rounds:
            lookup[rd] = flag_rec.rec
    return lookup


def calculate_ac_rounds() -> list[ACRound]:
    flag_lookup = flag_rec_lookup()

    ac_rounds = load_ac_rounds_from_csv()
    ac_rounds.sort(key=lambda r: r.power_billions, reverse=True)

    hero = NUM_HEROES_TO_SAVE + 1

    for i, ac_round in enumerate(ac_rounds):
        if i < NUM_ROUNDS_TO_TUCK:
            ac_round.recommendation_heroes = []
            ac_round.recommendation_heroes_sort = 99
            ac_round.recommendation_flags = "*"
        else:
            if ac_round.round in flag_lookup:
                rec_flag = flag_lookup[ac_round.round]
            else:
                rec_flag = DEFAULT_FLAG_REC

            ac_round.recommendation_flags = rec_flag
            ac_round.recommendation_heroes = [hero]
            ac_round.recommendation_heroes_sort = hero
            hero += 1

            if rec_flag == "S":
                ac_round.recommendation_heroes.append(hero)
                hero += 1

    ac_rounds.sort(key=lambda r: r.recommendation_heroes_sort)
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
    table.field_names = ["Round", "Opponent", "Server", "Power(B)", "Members", "Hero Rec", "Flags Rec"]
    for r in ac_rounds:
        table.add_row([r.round, r.opponent, r.server, r.power_billions, r.members, r.recommendation_heroes, r.recommendation_flags])
    print(table)


def load_ac_rounds_from_csv() -> list[ACRound]:
    ac_rounds: list[ACRound] = []

    with open(f"files/{FILENAME}") as f:
        lines = f.readlines()
        for line in lines:
            cols = line.split(',')
            if not cols[COL_IDX_ROUND].isdigit():
                continue
            round_num = int(cols[COL_IDX_ROUND])
            opponent = cols[COL_IDX_NAME].lower()
            server = cols[COL_IDX_SERVER]
            power_billions = float(cols[COL_IDX_POWER])
            members = cols[COL_IDX_MEMBERS]
            comment = cols[COL_IDX_COMMENT].strip().lower()
            ac_rounds.append(ACRound(round_num, opponent, server, power_billions, members, [], 0, "", comment))
    return ac_rounds


class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)


main()



