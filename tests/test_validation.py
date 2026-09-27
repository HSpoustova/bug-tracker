import pytest

from validation import control_bug


def test_valid_bug_has_no_errors(valid_bug):
    assert control_bug(valid_bug) == []

def test_missing_name():
    errors = control_bug({"severity": "low", "priority": "low"})
    assert "Name is mandatory." in errors

def test_name_of_only_spaces_is_empty():
    errors = control_bug({"name": "  ", "severity": "low", "priority": "low"})
    assert "Name is mandatory." in errors

@pytest.mark.parametrize(
    "length, passes"
    [(2, False), (3, False), (100, True), (101, False)],
    ids=["2-below", "3-min", "100-max", "101-above"],
)

def test_name_length(length, passes):
    data = {"name": "a" * length, "severity": "low", "priority": "low"}
    assert (control_bug(data) == []) == passes


@pytest.mark.parametrize("severity", ["", "Critical", "blocker", None])
def test_invalid_severity(severity):
    data = {"name": "Bug", "severity": severity, "priority": "high"}
    assert "Choose severity from the list." in control_bug(data)

def test_several_errors_at_once():
    assert len(control_bug({})) == 3