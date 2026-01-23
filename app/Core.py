# Logic File
import Storage


class HabitLogic:
    def __init__(self):
        pass

    def createHabit(self, habitName):
        data = Storage.loadData()
        newHabit = Habit(habitName)
        data[str(len(data) + 1)] = newHabit.toDict()
        Storage.saveData(data)


class Habit:
    def __init__(self, habitName):
        self.isCompleted = False
        self.habitName = habitName

    def completeHabit(self):
        self.isCompleted = True

    def uncompleteHabit(self):
        self.isCompleted = False

    def toDict(self):
        return {"Habit": self.habitName, "isCompleted": self.isCompleted}


if __name__ == "__main__":
    createHabit = HabitLogic()
    createHabit.createHabit("test1")
