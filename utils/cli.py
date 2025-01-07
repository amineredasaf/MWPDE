# import os
# import json
# import subprocess
from questionary import select, checkbox, text, print as qprint
from emoji import emojize


def cli(config):
    qprint(emojize(config), style="cyan")
