import random
import base64

from .model import Lottery

DEFAULT_LOTTERY_FILE_NAME = "lottery.yaml"


def encode_choice(choice: str) -> str:
    bytes = choice.encode("utf-8")
    b64_bytes = base64.b64encode(bytes)
    encoded = b64_bytes.decode("utf-8")

    return encoded


def do_lottery(lottery: Lottery):
    result = {}
    for player in lottery.players:
        possible_choices = [
            choice for choice in lottery.choices if choice not in player.bans
        ]

        drafted_choice = random.choice(possible_choices)
        result[player.name] = (
            drafted_choice
            if not lottery.encoded
            else encode_choice(drafted_choice)
        )

    return result
