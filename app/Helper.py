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
    for key, value in dataDict.items():
        if value["Name"].lower() == habitName.lower():
            print(f"Duplicate habit found: |{key}| - |{value}|")
            searchQuery = key
            habitName = habitName


def dateGetter():
    return datetime.today().strftime("%Y-%m-%d")


if __name__ == "__main__":
    pass
