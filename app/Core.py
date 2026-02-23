# Logic File
from . import Storage
from . import Helper
import time


class Habit:
    def __init__(
        self,
        name: str,
        id: int,
        dateCreated: str,
        completedDates: list = [],
        streak: int = 0,
    ):
        self.name = name
        self.id = id
        self.dateCreated = dateCreated
        self.completedDates = completedDates
        self.streak = streak

    @property
    def toDict(self):
        return {
            "Name": self.name,
            "Streak": self.streak,
            "DateCreated": self.dateCreated,
            "CompletedDates": self.completedDates,
        }

    def getStreak(self):
        self.streak = 0
        if max(self.completedDates) == Helper.dateGetter(1):
            counter = 1
            while Helper.dateGetter(counter) in self.completedDates:
                self.streak += 1
                counter += 1
        else:
            counter = 0
            while Helper.dateGetter(counter) in self.completedDates:
                self.streak += 1
                counter += 1

    def complete(
        self, date
    ):  # already defaulted in the complete function in HabitLogic
        if date not in self.completedDates:
            self.completedDates.append(date)
            self.getStreak()

    def unComplete(self, date):
        if date in self.completedDates:
            self.completedDates.remove(date)
            self.getStreak()


class HabitLogic:
    def __init__(self):
        self.habitData: dict = Storage.loadData()
        # self.date = Helper.dateGetter()

        self.habits = {}
        self.loadHabits()

    def createHabit(self, habitName=None):
        bool, xdx = Helper.nameValidator(habitName, self.habits)
        if not bool:
            return bool, xdx
        else:
            print(xdx)
            newID = Helper.idGenerator(self.habitData)
            newHabit = Habit(
                xdx,
                newID,
                Helper.dateGetter(),  # how far from today e.g 0 for today and 1 for yesterday
            )  # New habits are not completed by default

            self.habits[newID] = newHabit
            self.habitData[newID] = newHabit.toDict
            Storage.saveData(self.habitData)
            print(f"Habit |{newID} - {xdx}| created.")
            return bool, xdx

    def deleteHabit(self, HabitID: int):
        print(f"Habit |{HabitID} - {self.habitData[HabitID]["Name"]}| deleted.")
        self.habitData.pop(HabitID)
        self.habits.pop(HabitID)
        Storage.saveData(self.habitData)

    def updateHabit(self, HabitID, newHabitName):
        self.habitData[HabitID]["Name"] = newHabitName
        self.habits[HabitID].name = newHabitName
        print(
            f"Habit |{HabitID} - {self.habitData[HabitID]["Name"]}| updated to |{newHabitName}|"
        )
        Storage.saveData(self.habitData)

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

    def completeHabit(self, HabitID, date=Helper.dateGetter()):
        self.habits[HabitID].complete(date)
        self.habitData[HabitID] = self.habits[HabitID].toDict
        print(self.habits[HabitID].toDict)
        Storage.saveData(self.habitData)
        print(f"From CompleteHabit: Habit |{HabitID} - {HabitID}| marked as completed.")

    def unCompleteHabit(self, HabitID, date=Helper.dateGetter()):
        self.habits[HabitID].unComplete(date)
        self.habitData[HabitID] = self.habits[HabitID].toDict
        Storage.saveData(self.habitData)
        print(f"Habit |{HabitID} - {HabitID}| marked as incompleted.")

    def loadHabits(self):
        for key, value in self.habitData.items():
            habit = Habit(
                value["Name"],
                key,
                value["DateCreated"],
                value["CompletedDates"],
                value["Streak"],
            )
            self.habits[key] = habit


if __name__ == "__main__":
    createHabit = HabitLogic()
    createHabit.createHabit("gym")
