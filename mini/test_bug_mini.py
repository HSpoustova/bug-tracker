from bug_mini import control_bug

def test_short_name():
    assert control_bug("Al") == ["Name is too short."]


def test_ok_name():
    assert control_bug("Alik") == []

def test_long_name():
    assert control_bug("Alik a Bella spolu") == ["Name is too long."]

