from bug_mini import control_bug, control_bug_dict, priority_level
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


class TestBugDict:
    def test_valid(self, valid_bug):
        assert control_bug_dict(valid_bug) == []

    def test_short_name(self, valid_bug):
        valid_bug["name"] = "Al"              
        assert control_bug_dict(valid_bug) == ["Name is too short."]

    def test_missing_name(self, valid_bug):
        del valid_bug["name"] 
        assert control_bug_dict(valid_bug) == ["Name must be text."]
    
    def test_missing_priority(self, valid_bug):
        del valid_bug["priority"]
        assert control_bug_dict(valid_bug) == ["Priority must be text."]
   
    def test_empty(self):
        assert control_bug_dict({}) == ["Name must be text."]
    
    def test_invalid_priority_dict(self, valid_bug):
        valid_bug["priority"] = "urgent"
        assert control_bug_dict(valid_bug) == ["Invalid priority."]


class TestPriorityLevel:

    @pytest.mark.parametrize("priority, level", [
        ("low", 1),
        ("medium", 2),
        ("high", 3),
    ])
    def test_level(self, priority, level):
        assert priority_level(priority) == level       

    def test_unknown_priority(self):
        with pytest.raises(ValueError):                
            priority_level("urgent")
        
    def test_unknown_priority_message(self):
        with pytest.raises(ValueError, match="urgent"):
            priority_level("urgent")