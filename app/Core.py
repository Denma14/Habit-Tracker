# Logic File
import Storage
import Helper
import time


class Habit:
    def __init__(self, name: str, isCompleted: bool, id: int):
        self.name = name
        self.id = id
        self.isCompleted = isCompleted
        self.dateCreated = Helper.dateGetter()
        self.lastCompleted = None
        self.streak = 0

    @property
    def toDict(self):
        return {
            "Name": self.name,
            "IsCompleted": self.isCompleted,
            "Streak": self.streak,
            "DateCreated": self.dateCreated,
            "LastCompleted": self.lastCompleted,
        }

    @property
    def complete(self):
        self.toDict["IsCompleted"] = True
        self.toDict["LastCompleted"] = Helper.dateGetter()
        if not self.streak:  # Incomplete figuring out how to do this
            self.toDict["Streak"] = self.streak + 1
        return self.toDict

    def unComplete(self):
        self.toDict["IsCompleted"] = False
        return self.toDict


class HabitLogic:
    def __init__(self):
        self.habitData: dict = Storage.loadData()
        self.date = Helper.dateGetter()

    def createHabit(self, habitName):
        newID = Helper.idGenerator(self.habitData)
        newHabit = Habit(
            habitName, False, newID
        )  # New habits are not completed by default
        self.habitData[newID] = newHabit.toDict
        Storage.saveData(self.habitData)
        print(f"Habit |{newID} - {habitName}| created.")

    def deleteHabit(self, habitName):
        habitID, habitName = self.viewHabit(habitName)
        if habitID is None:
            return

        self.habitData.pop(habitID)
        Storage.saveData(self.habitData)
        print(f"Habit |{habitID} - {habitName}| deleted.")

    def updateHabit(self, habitName, newHabitName):
        habitID, habitName = self.viewHabit(habitName)
        if habitID is None:
            return

        self.habitData[habitID]["Name"] = newHabitName
        Storage.saveData(self.habitData)
        print(f"Habit |{habitID} - {habitName}| updated to |{newHabitName}|")

    def viewHabit(self, habitName: str):
        searchQuery = None
        for key, value in self.habitData.items():
            if value["Name"].lower() == habitName.lower():
                searchQuery = value
                print(f"Habit found: |{key} - {value}|")
                return key, value
        if searchQuery is None:
            print(f"{habitName} not found.")
            return None, None

    def viewAllHabits(self):
        for key, value in self.habitData.items():
            print(f"|{key}| - |{value}|")

    def completeHabit(self, habitName):
        habitID, habitName = self.viewHabit(habitName)
        if habitID is None:
            return
        self.habitData[habitID]["IsCompleted"] = True
        Storage.saveData(self.habitData)
        print(f"Habit |{habitID} - {habitName}| marked as completed.")

    def unCompleteHabit(self, habitName):
        habitID, habitName = self.viewHabit(habitName)
        if habitID is None:
            return

        self.habitData[habitID]["IsCompleted"] = False
        Storage.saveData(self.habitData)
        print(f"Habit |{habitID} - {habitName}| marked as incompleted.")


if __name__ == "__main__":
    createHabit = HabitLogic()
    createHabit.completeHabit("Read")
