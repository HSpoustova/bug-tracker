import pytest

@pytest.fixture
def valid_bug():
    """Bug name and priority - control""" 
    return {"name": "Rex", "priority": "high"}

@pytest.fixture
def bugs():
    print("\nSETUP: new empty bugs") 
    new_bugs = []
    yield new_bugs
    print(f"\nTEARDOWN: {len(new_bugs)} bug(s), cleaning up")
    new_bugs.clear()