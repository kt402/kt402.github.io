from dataclasses import dataclass


@dataclass
class ACRound:
    round: int
    opponent: str
    server: str
    power_billions: float
    recommendation_hero: int
    recommendation_flags: str


@dataclass
class Recommendations:
    num_heroes_to_save: int
    num_rounds_tucking: int
    additional_strategies: str
    flags_key: dict[str:str]
    rounds: list[ACRound]
