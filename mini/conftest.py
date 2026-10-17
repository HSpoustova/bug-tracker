import pytest

@pytest.fixture
def valid_bug():
    """Bug name and priority - control""" 
    return {"name": "Rex", "priority": "high"}