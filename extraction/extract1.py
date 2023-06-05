from extract_util import *
from extraction.extract_model import Recommendations, ACRound, FlagRec

NUM_HEROES_TO_SAVE = 4
NUM_ROUNDS_TO_TUCK = 7

EXCEPTION_ROUNDS = {
    1: ["S"],
}

FLAGS_RECS = [
    FlagRec("S", [22, 10, 19, 6]),
    FlagRec("C", [11, 24, 9, 7, 20, 5, 25, 21, 23]),
]
DEFAULT_FLAG_REC = "*"


def calc_1(ac_rounds: list[ACRound]) -> list[ACRound]:
    flag_lookup = flag_rec_lookup()
    hero = NUM_HEROES_TO_SAVE + 1

    for i, ac_round in enumerate(ac_rounds):
        if ac_round.round in EXCEPTION_ROUNDS:
            exception_round_flag = EXCEPTION_ROUNDS[ac_round.round][0]
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


def flag_rec_lookup() -> dict[int: str]:
    lookup: dict[int: str] = {}
    for flag_rec in FLAGS_RECS:
        for rd in flag_rec.rounds:
            lookup[rd] = flag_rec.rec
    return lookup

