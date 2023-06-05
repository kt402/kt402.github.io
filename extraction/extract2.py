import copy

from extraction.extract_model import *

SAVE = 4
LORD_ELITE_OVERRIDES: dict[int: Override] = {
    1: hero_override(hero=[14, 15], flag='S'),
    12: hero_override(hero=[10, 11], flag='S'),
    16: hero_override(hero=[16, 17], flag='S'),
    23: hero_override(hero=[12], flag='C'),
    11: flag_override(flag='S'),
    6: flag_override(flag='C'),
    15: flag_override(flag='C'),
    22: flag_override(flag='C'),
    21: flag_override(flag='C'),
    4: flag_override(flag='C'),
    2: flag_override(flag='C'),
    5: flag_override(flag='C'),
    17: flag_override(flag='C'),
    3: tuck_override(),
    13: tuck_override(),
    24: tuck_override(),
    25: tuck_override(),
}

MEMBER_OVERRIDES: dict[int: Override] = {
    1: hero_override(hero=[8, 9], flag='S'),
    12: hero_override(hero=[11], flag='C'),
    16: hero_override(hero=[14], flag='C'),
    23: hero_override(hero=[13], flag='C'),
    11: flag_override(flag='C'),
    6: flag_override(flag='S'),
    15: flag_override(flag='S'),
    22: flag_override(flag='C'),
    21: flag_override(flag='C'),
    4: flag_override(flag='C'),
    2: flag_override(flag='C'),
    5: flag_override(flag='C'),
    17: flag_override(flag='C'),
    3: tuck_override(),
    13: tuck_override(),
    24: tuck_override(),
    25: tuck_override(),
}


def calc_2(ac_rounds: list[ACRound]) -> (RecommendationGroup, RecommendationGroup):
    lord_elite_recommendation_group = calc_for_overrides(ac_rounds, LORD_ELITE_OVERRIDES)
    member_recommendation_group = calc_for_overrides(ac_rounds, MEMBER_OVERRIDES)

    return lord_elite_recommendation_group, member_recommendation_group


def calc_for_overrides(ac_rounds: list[ACRound], overrides: dict[int: Override]) -> RecommendationGroup:
    ac_rounds = copy.deepcopy(ac_rounds)
    ac_rounds.sort(key=lambda r: r.power_billions, reverse=True)

    used_heroes: set[int] = set()
    curr_hero = SAVE
    tuck_count = 0

    for rd, o in overrides.items():
        used_heroes.update(o.hero)

    for i, ac_round in enumerate(ac_rounds):
        rd = ac_round.round
        override = None if rd not in overrides else overrides[ac_round.round]

        #
        # Overrides
        #
        if override and override.tuck:
            ac_round.recommendation_heroes = []
            ac_round.recommendation_flags = "-"
            ac_round.comment = "tuck"
            tuck_count += 1
        elif override and override.hero:
            ac_round.recommendation_heroes = override.hero
            ac_round.recommendation_flags = override.flag
        elif override and override.flag == "S":
            curr_hero = next_hero(curr_hero, used_heroes)
            ac_round.recommendation_heroes = [curr_hero]
            curr_hero = next_hero(curr_hero, used_heroes)
            ac_round.recommendation_heroes += [curr_hero]
            ac_round.recommendation_flags = override.flag
        elif override:
            curr_hero = next_hero(curr_hero, used_heroes)
            ac_round.recommendation_heroes += [curr_hero]
            ac_round.recommendation_flags = override.flag

        #
        # Not overrides
        #
        else:
            curr_hero = next_hero(curr_hero, used_heroes)
            ac_round.recommendation_heroes += [curr_hero]
            ac_round.recommendation_flags = "*"

        #
        # Set the hero sort
        #
        if ac_round.recommendation_heroes:
            ac_round.recommendation_heroes_sort = ac_round.recommendation_heroes[0]

        used_heroes.update(ac_round.recommendation_heroes)

    #
    # Calculate hero for tuck rounds
    #
    for i, ac_round in enumerate(ac_rounds):
        if not ac_round.recommendation_heroes:
            curr_hero = next_hero(curr_hero, used_heroes)
            ac_round.recommendation_heroes += [curr_hero]
            ac_round.recommendation_heroes_sort = ac_round.recommendation_heroes[0]

    return RecommendationGroup(ac_rounds, SAVE, tuck_count)


def next_hero(curr_hero: int, used_heroes: set[int]) -> int:
    curr_hero = curr_hero + 1
    while curr_hero in used_heroes:
        curr_hero = curr_hero + 1
    return curr_hero
