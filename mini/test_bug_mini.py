from bug_mini import control_bug
import pytest

def test_invalid_priority():
    assert control_bug("Alik", "urgent") == ["Invalid priority."]

def test_two_errors():
    assert control_bug("Alik a Bella spolu", "urgent") == ["Name is too long.", "Invalid priority."]


@pytest.mark.parametrize("priority", ["low", "medium", "high"])
def test_valid_priority(priority):
    assert control_bug("Alik", priority) == []

@pytest.mark.parametrize("name, expected", [
    ("Al", ["Name is too short."]),
    ("Rex", []),
    ("Bella Alik",[]),
    ("Bella a Rex", ["Name is too long."]),
    ("   ", ["Name is too short."]),
])
def test_name_length(name, expected):
    assert control_bug(name, "medium") == expected

@pytest.mark.parametrize("priority", ["High", " high ", "LOW"])
def test_priority_cleaned(priority):
    assert control_bug("Rex", priority) == []

@pytest.mark.parametrize("priority", [None, 123])
def test_priority_not_text(priority):
    assert control_bug("Rex", priority) == ["Priority must be text."]

@pytest.mark.parametrize("name", [None, 123])
def test_name_not_text(name):
    assert control_bug(name, "medium") == ["Name must be text."]