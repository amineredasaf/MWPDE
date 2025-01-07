import os
import json
from questionary import print as qprint
from emoji import emojize

CONFIG_FILE = "config.json"
VM_CONFIG_FILE = "vm.config.json"

# todo
# parse prediend vm config b7al : boxes, languages, envs
# parse the input like shard folder and done

def load_config():
    try:
        # here my predefind code
        with open(VM_CONFIG_FILE, "r") as f:
            return json.load(f)

    except FileNotFoundError as e:
        qprint(emojize(f":warning:  - File not found: {e}"), style="red")
    except json.JSONDecodeError as e:
        qprint(emojize(f":x:  - JSON Decode Error: {e}"), style="red")
    except Exception as e:
        qprint(emojize(f":information:  - An unexpected error occurred: {e}"), style="red")

if __name__ == "__main__":
    f = load_config()
    f = json.dumps(f, indent=2)
    print(f)