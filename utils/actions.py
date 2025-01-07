from questionary import select
import config

def select_box(config):
    if isinstance(config["BOX_LIST"], dict):
        box_choices = [
            # {"name": f"{details['BOX']} ({details['BOX_VERSION']})", "value": key}
            {"name": f"{details['BOX']}", "value": key}
            for key, details in config["BOX_LIST"].items()
        ]
        
        choice = select(
            "What Box Do You Want?",
            choices=box_choices
        ).ask()

        # Get the selected box key and use it to get the details
        selected_box_details = config["BOX_LIST"][choice]
        
        # Display the selected box
        print(f"Selected box: {selected_box_details['BOX']}")
        print(f"Version: {selected_box_details['BOX_VERSION']}")
    else:
        print("BOX_LIST is not loaded correctly!")

if __name__ == "__main__":
    config = config.load_config()  # Assuming the configuration is loaded from a file
    select_box(config)
