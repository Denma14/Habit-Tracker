# Logic File
import Storage
import time


class HabitLogic:
    def __init__(self):
        self.habitData: dict = Storage.loadData()

    def createHabit(self, habitName):
        newHabit = self.toDict(
            habitName, False
        )  # New habits are not completed by default
        newID = str(len(self.habitData) + 1)
        self.habitData[newID] = newHabit
        Storage.saveData(self.habitData)
        print(f"Habit |{newID} - {habitName}| created.")

    def deleteHabit(self, habitName):
        habitID, habitName = self.viewHabit(habitName)
        self.habitData.pop(habitID)
        Storage.saveData(self.habitData)
        print(f"Habit |{habitID} - {habitName}| deleted.")

    def updateHabit(self, habitName, newHabitName):
        habitID, habitName = self.viewHabit(habitName)
        self.habitData[habitID]["Name"] = newHabitName
        Storage.saveData(self.habitData)

    def viewHabit(self, habitName: str):
        searchQuery = None
        for key, value in self.habitData.items():
            if value["Name"].lower() == habitName.lower():
                searchQuery = value
                print(f"Habit found: |{key} - {value}|")
                return key, value
        if searchQuery is None:
            print("Habit not found.")

    def completeHabit(self, habitName):
        habitID, habitName = self.viewHabit(habitName)
        self.habitData[habitID]["isCompleted"] = True
        Storage.saveData(self.habitData)
        print(f"Habit |{habitID} - {habitName}| marked as completed.")

    def unCompleteHabit(self, habitName):
        habitID, habitName = self.viewHabit(habitName)
        self.habitData[habitID]["isCompleted"] = False
        Storage.saveData(self.habitData)
        print(f"Habit |{habitID} - {habitName}| marked as incompleted.")

    def toDict(self, habitName, isCompleted):
        return {"Name": habitName, "isCompleted": isCompleted}


if __name__ == "__main__":
    createHabit = HabitLogic()
    createHabit.createHabit("Test1")
    time.sleep(1)
    createHabit.viewHabit("Test1")
    time.sleep(1)
    createHabit.updateHabit("Test1", "Test 2")
    time.sleep(1)
    createHabit.completeHabit("Test 2")
    time.sleep(1)
    createHabit.unCompleteHabit("Test 2")
    time.sleep(1)
    createHabit.deleteHabit("Test 2")
