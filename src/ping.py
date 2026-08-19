import subprocess
import time

def ping_host(ip_address):
    """
    Check whether a host is reachable using the system ping command.
    Args:
        ip_address (str): IP address or hostname of the client.
    Returns:
        dict : Connectivity status and response time
    """

    command = ["ping", "-c", "1", "-W", "2", ip_address]

    start_time = time.perf_counter()

    result = subprocess.run(
        command,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    end_time = time.perf_counter()

    if result.returncode == 0:
        latency_ms = round((end_time - start_time) * 1000, 2)

        return {
            "reachable": True,
            "latency_ms": latency_ms
        }
    return {
        "reachable": False,
        "latency_ms": None
    }


#temp code check below

if __name__ == "__main__":
    ip = "10.10.0.215"
    print(ping_host(ip))