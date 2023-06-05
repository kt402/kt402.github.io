import dataclasses
import json
import requests
from prettytable import PrettyTable

from extract_model import *


def get_csv(sheets_id: str, sheet: str):
    url = f"https://docs.google.com/spreadsheets/d/{sheets_id}/gviz/tq?tqx=out:csv&sheet={sheet}"
    r = requests.get(url)
    with open(f"files/{sheet}.csv", "wb") as f:
        f.write(r.content)


def load_ac_rounds_from_csv(sheet: str) -> list[ACRound]:
    col_round = 0
    col_name = 1
    col_server = 2
    col_power = 8
    col_members = 9
    col_comment = 12

    ac_rounds: list[ACRound] = []

    with open(f"files/{sheet}.csv") as f:
        lines = f.readlines()
        for line in lines:
            cols = line.split(',')
            for i, col in enumerate(cols):
                cols[i] = col.strip('\"')

            if not cols[col_round].isdigit():
                continue
            round_num = int(cols[col_round])
            opponent = cols[col_name].lower()
            server = cols[col_server]
            power_billions = float(cols[col_power])
            members = cols[col_members]
            comment = ""
            # comment = cols[COL_IDX_COMMENT].strip().lower()
            ac_rounds.append(ACRound(round_num, opponent, server, power_billions, members, [], 0, "", comment))
    return ac_rounds


def write_file(recommendations: Recommendations):
    with open("../src/views/data.ts", 'w') as out:
        json_str = json.dumps(recommendations, indent=2, cls=EnhancedJSONEncoder)
        out.write(f"export const data = {json_str} as any;")


class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)


def print_pretty_table(ac_rounds: list[ACRound], title: str):
    table = PrettyTable()
    table.title = title
    table.field_names = ["Round", "Opponent", "Server", "Power(B)", "Members", "Hero Rec", "Flags Rec", "Comment"]
    for r in ac_rounds:
        table.add_row([r.round, r.opponent, r.server, r.power_billions, r.members, r.recommendation_heroes,
                       r.recommendation_flags, r.comment])
    print(table)
