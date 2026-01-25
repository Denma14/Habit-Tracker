# Helper file
from datetime import datetime


def idGenerator(dataDict: dict):
    id = None
    if len(dataDict) == 0:
        id = 1
    else:
        lastID = max(int(key) for key in dataDict.keys())
        id = lastID + 1
    print(id)
    return id


def duplicateChecker(dataDict: dict, habitName: str):  # Incomplete
    searchQuery = None
    duplicateNumber = 0
    for key, value in dataDict.items():
        duplicateNumber += 1
    for key, value in dataDict.items():
        if value.name.lower() == habitName.lower():
            print(f"Duplicate habit found: |{key}| - |{value}|")
            searchQuery = key

            value.name = f"{habitName} ({duplicateNumber})"
            return value.name
    if searchQuery is None:
        return habitName


def dateGetter():
    return datetime.today().strftime("%Y-%m-%d")


if __name__ == "__main__":
    pass
