from constants import SEVERITY, PRIORITY, NAME_MIN, NAME_MAX


def control_bug(data):
    bugs=[]

    name = (data.get("name") or "").strip()

    if not name:
        bugs.append("Name is mandatory.")

    elif len(name) < NAME_MIN:
        bugs.append("Name must have min. 3 characters.")

    elif len(name) > NAME_MAX:
        bugs.append("Name must have max. 100 characters.")

    if data.get("severity") not in SEVERITY:
        bugs.append("Choose severity from the list.")

    if data.get("priority") not in PRIORITY:
        bugs.append("Choose priority from the list.")


    return bugs