


NAME_MIN = 3
NAME_MAX = 10
PRIORITIES = ["low", "medium", "high"]

def control_bug(name, priority):
    if not isinstance(name, str):
        return["Name must be text."]
    name = name.strip()
    errors=[]
    if len(name) < NAME_MIN:
        errors.append("Name is too short.")
    if len(name) > NAME_MAX:
        errors.append("Name is too long.")
    if priority not in PRIORITIES:
        errors.append("Invalid priority.")
    return errors

