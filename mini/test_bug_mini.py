from bug_mini import control_bug
import pytest

def test_short_name():
    assert control_bug("Al", "medium") == ["Name is too short."]

def test_long_name():
    assert control_bug("Alik a Bella spolu", "low") == ["Name is too long."]

def test_invalid_priority():
    assert control_bug("Alik", "urgent") == ["Invalid priority."]

def test_two_errors():
    assert control_bug("Alik a Bella spolu", "urgent") == ["Name is too long.", "Invalid priority."]


@pytest.mark.parametrize("priority", ["low", "medium", "high"])
def test_valid_priority(priority):
    assert control_bug("Alik", priority) == []