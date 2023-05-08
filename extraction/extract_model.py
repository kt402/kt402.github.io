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
class Recommendations:
    header: str
    num_heroes_to_save: int
    num_rounds_tucking: int
    num_exception_rounds: int
    additional_strategies: str
    flags_key: dict[str:str]
    rounds: list[ACRound]


@dataclass
class FlagRec:
    rec: str
    rounds: [int]
