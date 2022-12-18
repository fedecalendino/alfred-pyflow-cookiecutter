import sys

import random
from pyflow import Workflow

from data import FORTUNES


def main(workflow):
    if len(workflow.args) > 0:
        amount = min(10, int(workflow.args[0].lower()))
    else:
        amount = 5

    for fortune in random.sample(FORTUNES, amount):
        numbers = ' '.join(map(str, random.sample(range(1, 100), 6)))

        workflow.new_item(
            title=fortune,
            subtitle=f"Your lucky numbers are: {numbers}",
            arg=fortune,
            copytext=fortune,
            valid=True,
        ).set_icon_file(
            path="./icon.png",
        )


if __name__ == "__main__":
    wf = Workflow()
    wf.run(main)
    wf.send_feedback()
    sys.exit()
