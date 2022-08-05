import argparse

from .lottery import do_lottery
from .model import load_from_yaml


def entrypoint():
    parser = argparse.ArgumentParser("lotterydraft")
    parser.add_argument(
        "lotteryfile",
        help="YAML file containing the lottery definition.",
        type=str,
        default="lottery.yaml",
        nargs="?"
    )

    args = parser.parse_args()

    lottery = load_from_yaml(args.lotteryfile)
    result = do_lottery(lottery)

    print(result)
