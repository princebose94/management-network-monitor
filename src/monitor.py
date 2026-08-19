import json
#from pathlib import Path
from src.ping import ping_host
from src.reporter import save_report

def load_clients(config_file):
    with open(config_file, "r") as file:
        config = json.load(file)
    return config["clients"]

def monitor_clients(clients):
    results = []

    for client in clients:
        name = client["name"]
        host = client["ip"]

        ping_result = ping_host(host)

        result = {
            "name": name,
            "host": host,
            **ping_result
        }

        results.append(result)

    return results


#temp codeblock here.
"""

def main():
    config_file = Path("config/clients.json")
    output_file = Path("reports/network_status.json")

    clients = load_clients(config_file)
    results = monitor_clients(clients)

    for result in results:
        print(result)

    save_report(results, output_file)
    print("Report saved successfully!")


if __name__ == "__main__":
    main()

"""