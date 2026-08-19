import subprocess
from src.ping import ping_host

def test_ping_host_reachable(monkeypatch):
    def mock_run(*args, **kwargs):
        return subprocess.CompletedProcess(
            args=args,
            returncode=0
        )

    monkeypatch.setattr(subprocess, "run", mock_run)

    result = ping_host("192.168.1.1")

    assert result["reachable"] is True
    assert result["latency_ms"] is not None



def test_ping_host_unreachable(monkeypatch):
    def mock_run(*args, **kwargs):
        return subprocess.CompletedProcess(
            args=args,
            returncode=1
        )

    monkeypatch.setattr(subprocess, "run", mock_run)

    result = ping_host("192.168.1.100")

    assert result["reachable"] is False
    assert result["latency_ms"] is None
