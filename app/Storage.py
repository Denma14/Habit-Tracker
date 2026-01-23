# Storage file
import json

DATABASE_PATH: str = "app/Habit_Data.json"


def loadData():
    with open(DATABASE_PATH, "r") as f:  # Change back to Habit_Data.json
        data = json.load(f)
        return data


def saveData(data):
    with open(DATABASE_PATH, "w") as f:
        json.dump(data, f, indent=4)


if __name__ == "__main__":
    pass
