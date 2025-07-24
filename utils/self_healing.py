import json
import random

def heal_selectors():
    print("Attempting to heal selectors based on AI suggestions...")
    with open("selectors.json") as f:
        selectors = json.load(f)

    selectors["submit"] = random.choice(["#submitBtn", "button[type='submit']", ".btn-login"])

    with open("selectors.json", "w") as f:
        json.dump(selectors, f, indent=2)
