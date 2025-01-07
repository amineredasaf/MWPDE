# import os
# import json
# import subprocess
from questionary import select, checkbox, text, print as qprint
from emoji import emojize



def gui():
    qprint(emojize(":happy: Hey, My name is gui."), style="cyan")