from constants import SEVERITY, PRIOTRITY, NAME_MIN, NAME_MAX


def control_bug(data):
    bugs=[]

    name = (data.get("name") or "").strip()

    if not name:
        bugs.append("Name is mandatory.")