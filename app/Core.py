# Logic File
import Storage
import time


class HabitLogic:
    def __init__(self):
        self.habitData: dict = Storage.loadData()

    def createHabit(self, habitName):
        data = Storage.loadData()
        newHabit = self.toDict(
            habitName, False
        )  # New habits are not completed by default
        data[str(len(data) + 1)] = newHabit
        Storage.saveData(data)

    def deleteHabit(self, habitName):
        habitID, habitName = self.viewHabit(habitName)

    def updateHabit(self, habitName):
        habitID, habitName = self.viewHabit(habitName)

    @property
    def viewHabit(self, habitName: str):
        for key, value in self.habitData.items():
            if value["Name"].lower() == habitName.lower():
                return key, value
            else:
                print("Habit not found.")

    def completeHabit(self, habitName):
        habitID, habitName = self.viewHabit(habitName)
        self.habitData[habitID]["isCompleted"] = True
        Storage.saveData(self.habitData)
        print(self.habitData[habitID])

    def unCompleteHabit(self, habitName):
        habitID, habitName = self.viewHabit(habitName)
        self.habitData[habitID]["isCompleted"] = False
        Storage.saveData(self.habitData)
        print(self.habitData[habitID])

    def toDict(self, habitName, isCompleted):
        return {"Name": habitName, "isCompleted": isCompleted}


if __name__ == "__main__":
    createHabit = HabitLogic()
    createHabit.createHabit("HabitTest")
    createHabit.viewHabit("HabitTest")
    time.sleep(1)
    createHabit.completeHabit("HabitTest")
    time.sleep(1)
    createHabit.unCompleteHabit("HabitTest")
