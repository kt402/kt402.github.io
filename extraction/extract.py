import dataclasses
import json
import requests
from prettytable import PrettyTable

# Set these variables based on format of the sheet
from extraction.extract_model import Recommendations, ACRound, FlagRec

SHEETS_ID = "1FO5qoViBwMe4OWgPwwNCnJi3zKwRHPaa0HXBXqbfSM8"
SHEET = "MAY-2023"
NUM_HEROES_TO_SAVE = 1
NUM_ROUNDS_TO_TUCK = 10
EXCEPTION_ROUND_FLAG = {
    1: "S",
    17: "S",
    14: "C",
}

ADDITIONAL_STRATEGIES = \
    "Use strategy for rounds where 2 heroes are denoted. Then courage is preferred.<br><br>" \
    "We are tucking 7 rounds. 3 very tough rounds we are going hard. Rest is more normal planning.<br>" \
    "Hitz - use some yellow flags where you see fit.<br>" \
    "Seren - some of the tougher opponents you can use brutality and medium hero." \

FLAGS_RECS = [
    FlagRec("S", [22, 10, 19, 6]),
    FlagRec("C", [11, 24, 9, 7, 20, 5, 25, 21, 23]),
]
DEFAULT_FLAG_REC = "*"
FLAGS_KEY = {
    "S": "strategy",
    "C": "courage",
    "*": "any",
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
    get_csv(f"https://docs.google.com/spreadsheets/d/{SHEETS_ID}/gviz/tq?tqx=out:csv&sheet={SHEET}")
    recommendations = Recommendations(
        header=SHEET,
        num_heroes_to_save=NUM_HEROES_TO_SAVE,
        num_rounds_tucking=NUM_ROUNDS_TO_TUCK - len(EXCEPTION_ROUND_FLAG),
        num_exception_rounds=len(EXCEPTION_ROUND_FLAG),
        additional_strategies=ADDITIONAL_STRATEGIES,
        flags_key=FLAGS_KEY,
        rounds=calculate_ac_rounds(),
    )
    write_file(recommendations)


def get_csv(url: str):
    r = requests.get(url)
    with open(f"files/{SHEET}.csv", "wb") as f:
        f.write(r.content)


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
        if ac_round.round in EXCEPTION_ROUND_FLAG:
            exception_round_flag = EXCEPTION_ROUND_FLAG[ac_round.round]
            ac_round.recommendation_flags = exception_round_flag
            ac_round.recommendation_heroes = [hero]
            ac_round.recommendation_heroes_sort = hero
            hero += 1
            if exception_round_flag == "S":
                ac_round.recommendation_heroes.append(hero)
                hero += 1
        elif i < NUM_ROUNDS_TO_TUCK:
            ac_round.recommendation_heroes = []
            ac_round.recommendation_heroes_sort = 99
            ac_round.recommendation_flags = "-"
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

    with open(f"files/{SHEET}.csv") as f:
        lines = f.readlines()
        for line in lines:
            cols = line.split(',')
            for i, col in enumerate(cols):
                cols[i] = col.strip('\"')

            if not cols[COL_IDX_ROUND].isdigit():
                continue
            round_num = int(cols[COL_IDX_ROUND])
            opponent = cols[COL_IDX_NAME].lower()
            server = cols[COL_IDX_SERVER]
            power_billions = float(cols[COL_IDX_POWER])
            members = cols[COL_IDX_MEMBERS]
            comment = ""
            # comment = cols[COL_IDX_COMMENT].strip().lower()
            ac_rounds.append(ACRound(round_num, opponent, server, power_billions, members, [], 0, "", comment))
    return ac_rounds


class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)


main()



