# Logic File
import Storage


class HabitLogic:
    def __init__(self):
        self.habitData = Storage.loadData()

    def createHabit(self, habitName):
        data = Storage.loadData()
        newHabit = self.toDict(
            habitName, False
        )  # New habits are not completed by default
        data[str(len(data) + 1)] = newHabit
        Storage.saveData(data)

    def deleteHabit(self, habitName):
        pass

    def updateHabit(self, habitName):
        pass

    def completeHabit(self, habitName):
        pass

    def toDict(self, habitName, isCompleted):
        return {"Name": habitName, "isCompleted": isCompleted}


if __name__ == "__main__":
    createHabit = HabitLogic()
    createHabit.createHabit("Habit3")
