from extract1 import *
from extract2 import *
from extraction.extract_model import Recommendations, ACRound, FlagRec

SHEETS_ID = "1Uugy6hzHLDDga6VjaYMBcLdxuX6oxqTI"
SHEET = "JUNE-2023"

ADDITIONAL_STRATEGIES = \
    "Everyone: stronger members - if using weaker than 1.5B hero, use brutality flag. " \
    "other members - if your hero is < 1B, use brutality<br><br>" \
    "Nom: use mostly brutality (your discretion), and feel free to save more heroes" \

FLAGS_KEY = {
    "S": "strategy",
    "C": "courage",
    "*": "your choice, use a flag",
}


def main():
    get_csv(SHEETS_ID, SHEET)
    ac_rounds = load_ac_rounds_from_csv(SHEET)

    # ac_rounds.sort(key=lambda r: r.power_billions, reverse=True)
    # print_pretty_table(ac_rounds, "Sorted by power")

    lord_elite_recs, member_recs = calc_2(ac_rounds)

    lord_elite_recs.rounds.sort(key=lambda r: r.recommendation_heroes_sort)
    print_pretty_table(lord_elite_recs.rounds, "Lords Elites sorted by hero")

    member_recs.rounds.sort(key=lambda r: r.recommendation_heroes_sort)
    print_pretty_table(member_recs.rounds, "Members sorted by hero")

    # ac_rounds_recommendations.sort(key=lambda r: r.round)
    # print_pretty_table(ac_rounds_recommendations, "Sorted by round")

    recommendations = Recommendations(
        header=SHEET,
        additional_strategies=ADDITIONAL_STRATEGIES,
        flags_key=FLAGS_KEY,
        lords_elites=lord_elite_recs,
        members=member_recs,
    )
    write_file(recommendations)


main()



