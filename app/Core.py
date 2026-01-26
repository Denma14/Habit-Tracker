# Logic File
import Storage
import Helper
import time


class Habit:
    def __init__(
        self,
        name: str,
        id: int,
        isCompleted: bool,
        dateCreated: str,
        lastCompleted=None,
    ):
        self.name = name
        self.id = id
        self.isCompleted = isCompleted
        self.dateCreated = dateCreated
        self.lastCompleted = lastCompleted
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

    def complete(self):
        self.isCompleted = True
        self.lastCompleted = Helper.dateGetter()
        if not self.streak:  # Incomplete figuring out how to do this
            self.streak += 1

    def unComplete(self):
        self.isCompleted = False


class HabitLogic:
    def __init__(self):
        self.habitData: dict = Storage.loadData()
        self.date = Helper.dateGetter()

        self.habits = {}
        self.loadHabits()

    def createHabit(self, habitName):
        newID = Helper.idGenerator(self.habitData)
        newHabit = Habit(
            habitName,
            newID,
            False,
            Helper.dateGetter(),
        )  # New habits are not completed by default

        self.habits[newID] = newHabit
        self.habitData[newID] = newHabit.toDict
        Storage.saveData(self.habitData)
        print(f"Habit |{newID} - {habitName}| created.")

    def deleteHabit(self, habitName):
        habitID, habitName = self.viewHabit(habitName)
        if habitID is None:
            return

        self.habitData.pop(habitID)
        self.habits.pop(habitID)
        Storage.saveData(self.habitData)
        print(f"Habit |{habitID} - {habitName}| deleted.")

    def updateHabit(self, habitName, newHabitName):
        habitID, habitName = self.viewHabit(habitName)
        if habitID is None:
            return

        self.habitData[habitID]["Name"] = newHabitName
        self.habits[habitID].name = newHabitName
        Storage.saveData(self.habitData)
        print(f"Habit |{habitID} - {habitName}| updated to |{newHabitName}|")

    def viewHabit(self, habitName: str):
        searchQuery = None
        for key, value in self.habits.items():
            if value.name.lower() == habitName.lower():
                searchQuery = (key, value.name)
                return searchQuery
        if searchQuery is None:
            print(f"|{habitName}| does not exist.")

    def viewAllHabits(self):
        for key, value in self.habitData.items():
            print(f"|{key}| - |{value}|")

    def completeHabit(self, habitName):
        habitID, habitName = self.viewHabit(habitName)
        if habitID is None:
            return
        self.habits[habitID].complete()
        self.habitData[habitID] = self.habits[habitID].toDict
        print(self.habits[habitID].toDict)
        Storage.saveData(self.habitData)
        print(
            f"From CompleteHabit: Habit |{habitID} - {habitName}| marked as completed."
        )

    def unCompleteHabit(self, habitName):
        habitID, habitName = self.viewHabit(habitName)
        if habitID is None:
            return

        self.habits[habitID].unComplete()
        self.habitData[habitID] = self.habits[habitID].toDict
        Storage.saveData(self.habitData)
        print(f"Habit |{habitID} - {habitName}| marked as incompleted.")

    def loadHabits(self):
        for key, value in self.habitData.items():
            habit = Habit(
                value["Name"],
                key,
                value["IsCompleted"],
                value["DateCreated"],
                value["LastCompleted"],
            )
            self.habits[key] = habit


if __name__ == "__main__":
    createHabit = HabitLogic()
    createHabit.createHabit("gym")
