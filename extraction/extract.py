from datetime import datetime
from extract_util import *
from extraction.extract_model import Recommendations, ACRoundSheet, ACRoundRec, FlagRec

SHEETS_ID = "1Uugy6hzHLDDga6VjaYMBcLdxuX6oxqTI"
SHEET = datetime.now().strftime("%m-%Y")

ADDITIONAL_STRATEGIES = ""

FLAGS_KEY = {
    "S": "strategy",
    "C": "courage",
    "*": "your choice, use a flag",
}


def main():
    get_csv(SHEETS_ID, SHEET)
    ac_rounds = load_ac_rounds_from_csv(SHEET)
    rec_group_1, rec_group_2 = get_rec_groups(ac_rounds, "All", None)

    pp_sort_by_round("", ac_rounds)
    # pp_sort_by_power("", ac_rounds)

    pp_sort_by_round("", rec_group_1.rounds)
    # pp_sort_by_power("", rec_group_1.rounds)
    # pp_sort_by_hero("", rec_group_1.rounds)

    recommendations = Recommendations(
        header=SHEET,
        additional_strategies=ADDITIONAL_STRATEGIES,
        flags_key=FLAGS_KEY,
        rec_group_1=rec_group_1,
        rec_group_2=rec_group_2,
    )

    write_file(recommendations)


def pp_sort_by_power(name: str, ac_rounds: list[ACRoundSheet | ACRoundRec]):
    ac_rounds.sort(key=lambda r: r.power_billions, reverse=True)
    print_pretty_table(ac_rounds, f"{name} sorted by power")


def pp_sort_by_round(name: str, ac_rounds: list[ACRoundSheet | ACRoundRec]):
    ac_rounds.sort(key=lambda r: r.round)
    print_pretty_table(ac_rounds, f"{name} sorted by round")


def pp_sort_by_hero(name: str, ac_rounds: list[ACRoundRec]):
    ac_rounds.sort(key=lambda r: r.rec.heroes_sort)
    print_pretty_table(ac_rounds, f"{name} sorted by hero")



main()



