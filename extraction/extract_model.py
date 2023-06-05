from dataclasses import dataclass


@dataclass
class ACRound:
    round: int
    opponent: str
    server: str
    power_billions: float
    members: str
    recommendation_heroes: [int]
    recommendation_heroes_sort: int
    recommendation_flags: str
    comment: str


@dataclass
class RecommendationGroup:
    rounds: list[ACRound]
    save: int
    tuck: int


@dataclass
class Recommendations:
    header: str
    additional_strategies: str
    flags_key: dict[str:str]
    lords_elites: RecommendationGroup
    members: RecommendationGroup


@dataclass
class FlagRec:
    rec: str
    rounds: [int]


@dataclass
class Override:
    tuck: bool
    hero: list[int]
    flag: str


def hero_override(hero: list[int], flag: str):
    return Override(False, hero, flag)


def flag_override(flag: str):
    return Override(False, [], flag)


def tuck_override():
    return Override(True, [], "")
