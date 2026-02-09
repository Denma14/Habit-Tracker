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
    duplicateNumber = 0
    for key, value in dataDict.items():
        if habitName.lower() in value.name.lower():
            print(f"Duplicate habit found: |{key}| - |{value}|")
            searchQuery = key

            duplicateNumber += 1
    if searchQuery:
        return f"{habitName} ({duplicateNumber})"
    elif not searchQuery:
        return habitName


def nameValidator(name: str):  # Incomplete
    pass


def dateGetter(when: str = None):
    if when == "today":
        return datetime.today().strftime("%Y-%m-%d")
    elif when == "yesterday":
        yesterday = datetime.today() - timedelta(days=1)
        return yesterday.strftime("%Y-%m-%d")


if __name__ == "__main__":
    pass
