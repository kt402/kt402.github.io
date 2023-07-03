import dataclasses
import json
import requests
from prettytable import PrettyTable
from functools import reduce

from extract_model import *


def get_csv(sheets_id: str, sheet: str):
    url = f"https://docs.google.com/spreadsheets/d/{sheets_id}/gviz/tq?tqx=out:csv&sheet={sheet}"
    r = requests.get(url)
    with open(f"files/{sheet}.csv", "wb") as f:
        f.write(r.content)


def load_rec(tuck: bool, heroes_txt: str, flags: str) -> Recommendation:
    heroes = []
    if heroes_txt:
        heroes = list(map(int, heroes_txt.split(',')))
    return Recommendation(
        tuck=tuck,
        heroes=heroes,
        heroes_sort=heroes[0] if heroes else 999,
        flags=flags,
    )


def is_float(string):
    if string.replace(".", "").isnumeric():
        return True
    else:
        return False


def load_ac_rounds_from_csv(sheet: str) -> list[ACRoundSheet]:
    col_round = 0
    col_name = 1
    col_server = 2
    col_power = 3
    col_members = 4
    col_rec_tuck = 5
    col_rec_1_heroes = 6
    col_rec_1_flags = 7
    col_rec_2_heroes = 8
    col_rec_2_flags = 9

    ac_rounds: list[ACRoundSheet] = []

    with open(f"files/{sheet}.csv") as f:
        lines = f.readlines()
        for line in lines:
            cols_split_by_quote = line.split('"')
            cols = []
            for i, col in enumerate(cols_split_by_quote):
                if i % 2 == 1:
                    cols.append(col)

            # Only process lines that have Opponent KP information
            if len(cols) < col_power or not is_float(cols[col_power]):
                continue

            round_num = int(cols[col_round])
            opponent = cols[col_name].lower()
            server = cols[col_server]
            power_billions = float(cols[col_power])
            members = cols[col_members]
            tuck = True if cols[col_rec_tuck].lower() == "y" else False

            g1 = load_rec(tuck, cols[col_rec_1_heroes], cols[col_rec_1_flags])
            g2 = load_rec(tuck, cols[col_rec_2_heroes], cols[col_rec_2_flags])

            ac_rounds.append(ACRoundSheet(
                round=round_num,
                opponent=opponent,
                server=server,
                power_billions=power_billions,
                members=members,
                rec_group_1=g1,
                rec_group_2=g2,
            ))
    return ac_rounds


def get_rec_group(name: str, ac_rounds: list[ACRoundSheet], group_func: callable) -> \
        RecommendationGroup:
    rounds = list(map(lambda r: ACRoundRec(r.round, r.opponent, r.server, r.power_billions, r.members,
                                           group_func(r)), ac_rounds))
    save = 999
    for rd in rounds:
        save = save if len(rd.rec.heroes) == 0 else min(save, rd.rec.heroes[0] - 1)
    tuck = len(list(filter(lambda r: r.rec.tuck, rounds)))
    return RecommendationGroup(
        name=name,
        rounds=rounds,
        save=save,
        tuck=tuck,
    )


def get_rec_groups(ac_rounds: list[ACRoundSheet], group_1_name: str, group_2_name: Optional[str] = None) -> \
        (RecommendationGroup, RecommendationGroup | None):

    has_group_2 = False
    for rd in ac_rounds:
        if rd.rec_group_2.heroes:
            has_group_2 = True

    g1 = get_rec_group(group_1_name, ac_rounds, lambda r: r.rec_group_1)
    g2 = None if not has_group_2 else get_rec_group(group_2_name, ac_rounds, lambda r: r.rec_group_2)

    return g1, g2


def write_file(recommendations: Recommendations):
    with open("../src/views/data.ts", 'w') as out:
        json_str = json.dumps(recommendations, indent=2, cls=EnhancedJSONEncoder)
        out.write(f"export const data = {json_str} as any;")


class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)


def print_pretty_table(ac_rounds: list[ACRoundSheet | ACRoundRec], title: str):
    from_sheet = True if isinstance(ac_rounds[0], ACRoundSheet) else False

    table = PrettyTable()
    table.title = title
    base_field_names = ["Round", "Opponent", "Server", "Power(B)", "Members"]

    if from_sheet:
        table.field_names = base_field_names + ["Tuck", "Rec 1 Heroes", "Rec 1 Flags", "Rec 2 Heroes", "Rec 2 Flags"]
    else:
        table.field_names = base_field_names + ["Tuck", "Rec Heroes", "Rec Flags"]

    for r in ac_rounds:
        row = [r.round, r.opponent, r.server, r.power_billions, r.members]
        if from_sheet:
            g1 = r.rec_group_1
            g2 = r.rec_group_2
            row += [g1.tuck, g1.heroes, g1.flags]
            if g2:
                row += [g2.heroes, g2.flags]
            else:
                row += ["", ""]
        else:
            recs = r.rec
            row += [recs.tuck, recs.heroes, recs.flags]

        table.add_row(row)

    print(table)
