# Helper file
from datetime import datetime, timedelta


def idGenerator(dataDict: dict):
    id = None
    if len(dataDict) == 0:
        id = 1
    else:
        lastID = max(int(key) for key in dataDict.keys())
        id = lastID + 1
    # print(id)
    return id


def duplicateChecker(dataDict: dict, habitName: str):  # To be removed from the app
    searchQuery = None
    for key, value in dataDict.items():
        if habitName.lower() in value.name.lower():
            print(f"Duplicate habit found: |{key}| - |{value}|")
            searchQuery = key
    if searchQuery:
        return f"{habitName} {searchQuery}"
    elif not searchQuery:
        return habitName


def nameValidator(name: str, habitDict: dict):  # Incomplete
    name = name.strip()
    Invalidlist = [
        "Enter new habit name",
        "Name cannot be empty.",
        "Invalid Name",
        "Name cannot be longer than 20 characters.",
        "Name already exists.",
    ]
    if not name:
        return False, Invalidlist[1]
    elif name in Invalidlist:
        return False, Invalidlist[2]
    elif len(name) > 20:
        return False, Invalidlist[3]
    else:
        for key, value in habitDict.items():
            if name.lower() in value.name.lower():
                return False, Invalidlist[4]
            else:
                return True, name


def dateGetter(when: str = None):
    if when == "today":
        return datetime.today().strftime("%Y-%m-%d")
    elif when == "yesterday":
        yesterday = datetime.today() - timedelta(days=1)
        return yesterday.strftime("%Y-%m-%d")


if __name__ == "__main__":
    pass
