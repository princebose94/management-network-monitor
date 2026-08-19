import json

def save_report(results, output_file):
    with open(output_file, "w") as file:
        json.dump(results, file, indent=4)

