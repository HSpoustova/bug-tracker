from constants import SEVERITY, PRIORITY, NAME_MIN, NAME_MAX


def control_bug(data):
    errors=[]

    name = (data.get("name") or "").strip()

    if not name:
        errors.append("Name is mandatory.")

    elif len(name) < NAME_MIN:
        errors.append("Name must have min. 3 characters.")

    elif len(name) > NAME_MAX:
        errors.append("Name must have max. 100 characters.")

    if data.get("severity") not in SEVERITY:
        errors.append("Choose severity from the list.")

    if data.get("priority") not in PRIORITY:
       errors.append("Choose priority from the list.")


    return errors