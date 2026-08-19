# Management Network Monitor

A small Python-based network monitoring tool that checks the reachability
and response time of configured network clients.

## Features

- Monitor multiple network clients
- Check host reachability using ICMP ping
- Measure approximate ping latency
- Load client configuration from JSON
- Generate a JSON network status report
- Basic automated testing using pytest

## Project Structure

management-network-monitor/
│
├── config/
│   └── clients.json
│
├── reports/
│   └── .gitkeep
│
├── src/
│   ├── __init__.py
│   ├── ping.py
│   ├── monitor.py
│   └── reporter.py
│
├── tests/
│   └── test_ping.py
│
├── main.py
├── pytest.ini
├── requirements.txt
└── README.md

## Configuration

Clients are configured in:

`config/clients.json`

Example:

```json
{
    "clients": [
        {
            "name": "lab-pc-1",
            "ip": "192.168.1.101"
        },
        {
            "name": "lab-pc-2",
            "ip": "192.168.1.102"
        }
    ]
}

## Running the Monitor

Create and activate a virtual environment:

python3 -m venv .venv
source .venv/bin/activate

Install development dependencies:

python -m pip install -r requirements.txt

Run the application:

python3 main.py

Example output:

{'name': 'lab-pc-1', 'host': '192.168.1.101', 'reachable': True, 'latency_ms': <value>}
{'name': 'lab-pc-2', 'host': '192.168.1.102', 'reachable': True, 'latency_ms': <value>}

Report saved successfully!

The generated report is stored at:

reports/network_status.json

Generated reports are excluded from Git using .gitignore.

## Running Tests

Run:

pytest

The current test suite verifies the reachable and unreachable
behaviour of the ping function.

## What I Learned

This project was created as a hands-on exercise in:

- Python project structure
- Modular Python development
- JSON configuration
- Virtual environments
- Git and GitHub workflow
- .gitignore
- Unit testing with pytest
- Generating structured JSON reports