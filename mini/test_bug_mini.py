from bug_mini import control_bug
import pytest



class TestName:

    @pytest.mark.parametrize("name, expected", [
        ("Al", ["Name is too short."]),
        ("Rex", []),
        ("Bella Alik",[]),
        ("Bella a Rex", ["Name is too long."]),
        ("   ", ["Name is too short."]),
        ])

    def test_length(self, name, expected):
        assert control_bug(name, "medium") == expected

    @pytest.mark.parametrize("name", [None, 123])
    def test_name_not_text(self, name):
        assert control_bug(name, "medium") == ["Name must be text."]


class TestPriority:

    
    @pytest.mark.parametrize("priority", ["High", " high ", "LOW"])
    def test_priority_cleaned(self, priority):
        assert control_bug("Rex", priority) == []
    
    @pytest.mark.parametrize("priority", ["low", "medium", "high"])
    def test_valid_priority(self, priority):
        assert control_bug("Alik", priority) == []

    def test_invalid_priority(self):
        assert control_bug("Alik", "urgent") == ["Invalid priority."]

    @pytest.mark.parametrize("priority", [None, 123])
    def test_priority_not_text(self, priority):
        assert control_bug("Rex", priority) == ["Priority must be text."]

def test_two_errors():
    assert control_bug("Alik a Bella spolu", "urgent") == ["Name is too long.", "Invalid priority."]