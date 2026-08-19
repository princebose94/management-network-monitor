import json
from src.ping import ping_host

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
