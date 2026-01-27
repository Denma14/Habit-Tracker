# UI file
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont, QFontDatabase
from PyQt6.QtCore import Qt
from . import Core
from . import Styles


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Habit Tracker")
        self.setGeometry(750, 250, 500, 550)
        self.setFixedSize(500, 550)

        self.HabitLogic = Core.HabitLogic()

        # Main Widget
        self.mainWidget = QWidget(self)
        self.setCentralWidget(self.mainWidget)
        self.mainLayout = QVBoxLayout(self.mainWidget)

        # top Widget
        self.topWidget = QWidget(self.mainWidget)
        self.topLayout = QHBoxLayout(self.topWidget)

        self.appName = QLabel("Habit Tracker", self.topWidget)
        self.addHabitButton = QPushButton(
            "Add Habit", self.topWidget, clicked=self.addHabit
        )

        self.addHabitDialog = QDialog(self)
        # Scroll Area

        self.ScrollArea = QScrollArea(self.mainWidget)
        # elf.topLayout.addWidget(self.ScrollArea)
        self.ScrollArea.setWidgetResizable(True)
        self.ScrollContent = QWidget(self.ScrollArea)

        self.ScrollAreaLayout = QVBoxLayout(self.ScrollContent)
        self.ScrollArea.setWidget(self.ScrollContent)

        self.loadStyles()
        self.loadLayouts()
        self.loadHabits()

    def loadStyles(self):
        # Main Widget
        self.mainWidget.setStyleSheet("background-color: #000000;")

        # Top widget
        # /--Sizes
        self.topWidget.setFixedHeight(40)  # default is 40
        self.appName.setFixedSize(150, 30)
        self.addHabitButton.setFixedSize(100, 30)

        # /--Alignments
        self.appName.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.topWidget.setStyleSheet("background-color: #222222;")
        self.appName.setStyleSheet(
            "color: white; background-color: red; font-size: 20px; font-weight: bold;"
        )

        # Apply to your Scroll Area or Widget
        self.ScrollArea.setStyleSheet(Styles.scrollbar_stylesheet)
        self.ScrollContent.setStyleSheet("background-color: #222222;")

    def loadLayouts(self):
        # Main Widget
        self.mainLayout.addWidget(self.topWidget)
        self.mainLayout.addWidget(self.ScrollArea)
        # /-Alignments

        # Top widget
        self.topLayout.addWidget(self.appName, alignment=Qt.AlignmentFlag.AlignLeft)
        self.topLayout.addWidget(
            self.addHabitButton, alignment=Qt.AlignmentFlag.AlignCenter
        )

    def addWidgets(self):
        for i in range(1, 11):
            newWidget = QWidget(self.topWidget)
            self.ScrollAreaLayout.addWidget(newWidget)
            newWidget.setStyleSheet("background-color: red;")
            newWidget.setFixedSize(425, 50)

    def loadHabits(self):
        self.deleteWidgets()
        for key, value in self.HabitLogic.habitData.items():
            # Create habit widget--
            habitWidget = QWidget(self.ScrollContent)
            habitLayout = QHBoxLayout(habitWidget)
            habitWidget.setStyleSheet("background-color: red;")
            habitWidget.setFixedSize(425, 50)
            self.ScrollAreaLayout.addWidget(habitWidget)

            # Habit Title
            habitName = QLabel(habitWidget)

            habitLayout.addWidget(habitName)
            habitName.setText(value["Name"])
            habitName.setAlignment(Qt.AlignmentFlag.AlignCenter)
            habitName.setStyleSheet(
                "background-color: blue;color: white; font-size: 20px; font-weight: bold;"
            )
            habitName.setFixedSize(200, 50)

            # Habit Checkbox
            habitCheckbox = QCheckBox(habitWidget)
            habitLayout.addWidget(habitCheckbox, alignment=Qt.AlignmentFlag.AlignCenter)
            habitCheckbox.setChecked(value["IsCompleted"])
            habitCheckbox.setStyleSheet("background-color: green;")
            habitCheckbox.stateChanged.connect(
                lambda state, name=value["Name"]: self.habitStateChanged(state, name)
            )

    def deleteWidgets(self):
        for child in self.ScrollContent.children():
            if isinstance(child, QWidget):
                self.ScrollAreaLayout.removeWidget(child)
                child.setParent(None)
                child.deleteLater()

    def addHabit(self):
        print("Add Habit clicked!")
        if self.addHabitDialog.exec():
            self.HabitDialogInit()
        self.HabitLogic.createHabit("cook")
        self.loadHabits()

    def HabitDialogInit(self):
        self.addHabitDialog.setWindowTitle("Add New Habit")
        self.addHabitDialog.setGeometry(800, 300, 300, 150)
        self.addHabitDialog.setFixedSize(300, 150)

    def habitStateChanged(self, state, habitName):
        if state == Qt.CheckState.Checked.value:
            self.HabitLogic.completeHabit(habitName)
        else:
            self.HabitLogic.unCompleteHabit(habitName)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
