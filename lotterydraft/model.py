import yaml
from yaml.loader import SafeLoader
from pydantic import BaseModel
from typing import List


class Player(BaseModel):
    name: str
    bans: List[str] = []


class Lottery(BaseModel):
    choices: List[str]
    players: List[Player]
    encoded: bool = False


def load_from_yaml(path: str) -> Lottery:
    with open(path) as f:
        data = yaml.load(f, Loader=SafeLoader)

    model = Lottery(**data)

    return model
