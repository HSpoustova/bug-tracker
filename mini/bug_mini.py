


NAME_MIN = 3
NAME_MAX = 10
PRIORITIES = ["low", "medium", "high"]
PRIORITY_LEVELS = {"low": 1, "medium": 2, "high": 3}

def control_bug(name, priority):
    if not isinstance(name, str):
        return["Name must be text."]
    if not isinstance(priority, str):
        return ["Priority must be text."]
    name = name.strip()
    priority = priority.strip().lower()
    errors=[]
    if len(name) < NAME_MIN:
        errors.append("Name is too short.")
    if len(name) > NAME_MAX:
        errors.append("Name is too long.")
    if priority not in PRIORITIES:
        errors.append("Invalid priority.")
    return errors

def control_bug_dict(bug):
    name = bug.get("name")
    priority = bug.get("priority")
    return control_bug(name, priority)

def priority_level(priority):
    """It returns namuber of priority: low=1, medium=2, high=3"""
    if priority not in PRIORITY_LEVELS:
        raise ValueError(f"Unknown priority: {priority}")
    return PRIORITY_LEVELS[priority]

def add_bug(bugs, bug):
    errors = control_bug_dict(bug)
    if errors:
        return errors
    bugs.append(bug)
    return[]