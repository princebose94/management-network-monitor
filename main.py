from pathlib import Path
from src.reporter import save_report
from src.monitor import load_clients, monitor_clients

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