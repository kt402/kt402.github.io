from dataclasses import dataclass
from typing import Optional


@dataclass
class Recommendation:
    tuck: bool
    heroes: list[int]
    heroes_sort: int
    flags: str


@dataclass
class ACRoundSheet:
    round: int
    opponent: str
    server: str
    power_billions: float
    members: str
    rec_group_1: Recommendation
    rec_group_2: Recommendation


@dataclass
class ACRoundRec:
    round: int
    opponent: str
    server: str
    power_billions: float
    members: str
    rec: Recommendation


@dataclass
class RecommendationGroup:
    name: str
    rounds: list[ACRoundRec]
    save: int
    tuck: int


@dataclass
class Recommendations:
    header: str
    additional_strategies: str
    flags_key: dict[str:str]
    rec_group_1: RecommendationGroup
    rec_group_2: Optional[RecommendationGroup]


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
