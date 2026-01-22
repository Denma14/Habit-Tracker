# Logic File
import Storage


class HabitLogic:
    def __init__(self):
        pass


class Habit:
    def __init__(self, habitName):
        self.isCompleted = False
        self.habitName = habitName

    def completeHabit(self):
        self.isCompleted = True

    def uncompleteHabit(self):
        self.isCompleted = False


if __name__ == "__main__":
    pass
