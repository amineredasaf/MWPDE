# code diali
from utils import gui as g
from utils import cli as c
from utils import config

# extranal code
from questionary import print as qprint
from questionary import select
from emoji import emojize


if __name__ == "__main__":
    config = config.load_config()
    while True:
        choice = select(
            "What do you prefer working with?",
            choices=[
                emojize(":laptop: working GUI."),
                emojize(":pencil: Working With CLI."),
                emojize(":door: Exit"),
            ]
        ).ask()
        
        if choice == emojize(":laptop: working GUI."):
            g.gui()
        elif choice == emojize(":pencil: Working With CLI."):
            c.cli(config)
        elif choice == emojize(":door: Exit"):
            qprint(emojize(":door: Byee"), style="cyan")
            break
        


        
