# Logic File
from . import Storage
from . import Helper
import time


class Habit:
    def __init__(
        self,
        name: str,
        id: int,
        isCompleted: bool,
        dateCreated: str,
        streak: int = 0,
        lastCompleted=None,
    ):
        self.name = name
        self.id = id
        self.isCompleted = isCompleted
        self.dateCreated = dateCreated
        self.lastCompleted = lastCompleted
        self.streak = streak

    @property
    def toDict(self):
        return {
            "Name": self.name,
            "IsCompleted": self.isCompleted,
            "Streak": self.streak,
            "DateCreated": self.dateCreated,
            "LastCompleted": self.lastCompleted,
        }

    def complete(self):
        self.isCompleted = True
        self.lastCompleted = Helper.dateGetter("today")
        if not self.streak:  # Incomplete figuring out how to do this
            self.streak += 1

    def unComplete(self):
        self.isCompleted = False


class HabitLogic:
    def __init__(self):
        self.habitData: dict = Storage.loadData()
        # self.date = Helper.dateGetter()

        self.habits = {}
        self.loadHabits()
        self.checkdate()

    def createHabit(self, habitName=None):
        if not habitName:
            return
        print(habitName)
        newID = Helper.idGenerator(self.habitData)
        newHabit = Habit(
            Helper.duplicateChecker(self.habits, habitName),
            newID,
            False,
            Helper.dateGetter("today"),
            0,
        )  # New habits are not completed by default

        self.habits[newID] = newHabit
        self.habitData[newID] = newHabit.toDict
        Storage.saveData(self.habitData)
        print(f"Habit |{newID} - {habitName}| created.")

    def deleteHabit(self, HabitID: int):
        print(f"Habit |{HabitID} - {self.habitData[HabitID]["Name"]}| deleted.")
        self.habitData.pop(HabitID)
        self.habits.pop(HabitID)
        Storage.saveData(self.habitData)

    def updateHabit(self, HabitID, newHabitName):
        self.habitData[HabitID]["Name"] = newHabitName
        self.habits[HabitID].name = newHabitName
        Storage.saveData(self.habitData)
        print(
            f"Habit |{HabitID} - {self.habitData[HabitID]["Name"]}| updated to |{newHabitName}|"
        )

    def viewHabit(self, HabitID: int):
        searchQuery = None
        for key, value in self.habits.items():
            if key == HabitID:
                searchQuery = (key, value.name)
                return searchQuery
        if searchQuery is None:
            print(f"|{HabitID}| does not exist.")
            return

    def viewAllHabits(self):
        for key, value in self.habitData.items():
            print(f"|{key}| - |{value}|")

    def completeHabit(self, HabitID):
        if self.habits[HabitID].lastCompleted == Helper.dateGetter("yesterday"):
            self.habits[HabitID].streak += 1
        else:
            self.habits[HabitID].streak = 1
        self.habits[HabitID].complete()
        self.habitData[HabitID] = self.habits[HabitID].toDict
        print(self.habits[HabitID].toDict)
        Storage.saveData(self.habitData)
        print(f"From CompleteHabit: Habit |{HabitID} - {HabitID}| marked as completed.")

    def unCompleteHabit(self, HabitID):
        self.habits[HabitID].unComplete()
        self.habitData[HabitID] = self.habits[HabitID].toDict
        Storage.saveData(self.habitData)
        print(f"Habit |{HabitID} - {HabitID}| marked as incompleted.")

    def checkdate(self):
        for key, value in self.habits.items():
            if value.lastCompleted != Helper.dateGetter("today"):
                self.habits[key].unComplete()
                self.habitData[key] = self.habits[key].toDict
                Storage.saveData(self.habitData)

    def loadHabits(self):
        for key, value in self.habitData.items():
            habit = Habit(
                value["Name"],
                key,
                value["IsCompleted"],
                value["DateCreated"],
                value["Streak"],
                value["LastCompleted"],
            )
            self.habits[key] = habit


if __name__ == "__main__":
    createHabit = HabitLogic()
    createHabit.createHabit("gym")
