# Logic File
import Storage
import Helper
import time


class HabitLogic:
    def __init__(self):
        self.habitData: dict = Storage.loadData()

    def createHabit(self, habitName):
        newHabit = self.toDict(
            habitName, False
        )  # New habits are not completed by default
        newID = Helper.idGenerator(self.habitData)
        self.habitData[newID] = newHabit
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
        self.habitData[habitID]["isCompleted"] = True
        Storage.saveData(self.habitData)
        print(f"Habit |{habitID} - {habitName}| marked as completed.")

    def unCompleteHabit(self, habitName):
        habitID, habitName = self.viewHabit(habitName)
        if habitID is None:
            return

        self.habitData[habitID]["isCompleted"] = False
        Storage.saveData(self.habitData)
        print(f"Habit |{habitID} - {habitName}| marked as incompleted.")

    def toDict(self, habitName, isCompleted):
        return {"Name": habitName, "isCompleted": isCompleted}


if __name__ == "__main__":
    createHabit = HabitLogic()
    createHabit.deleteHabit("Read")
