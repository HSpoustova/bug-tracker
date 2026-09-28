import pytest




@pytest.fixture

def valid_bug():
    return {
        "name": "Ligon fails with 500",
        "steps": "1. Open /login\n2. Enter password\n3. Click Log in",
        "expected": "Redirect to dashboard",
        "actual":"Eroror 500",
        "severity": "critical",
        "priority": "high"
    }

