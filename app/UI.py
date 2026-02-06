# UI file
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt
from . import Core
from . import Styles


class AddHabitWidget(QWidget):
    def __init__(self, HabitLogic: Core.HabitLogic, loadHabits: function, parent=None):
        super().__init__()

        self.setParent(parent)
        self.loadHabits = loadHabits

        self.HabitLogic = HabitLogic
        self.setFixedHeight(40)
        self.setStyleSheet("background-color: blue;" "border: 2px solid white;")

        self.mainLayout = QHBoxLayout(self)
        self.habitNameInput = QLineEdit("Enter new habit name", self)
        self.confirmButton = QPushButton("Confirm", self, clicked=self.onConfirm)

        self.habitNameInput.setStyleSheet("background-color: yellow;")
        self.confirmButton.setStyleSheet("background-color: green;")

        self.mainLayout.addWidget(self.habitNameInput)
        self.mainLayout.addWidget(self.confirmButton)

    def onConfirm(self):
        self.HabitLogic.createHabit(self.habitNameInput.text())
        self.habitNameInput.setText("Enter new habit name")
        self.loadHabits()


class EditHabit(QWidget):
    def __init__(self, habitlogic: Core.HabitLogic, loadHabbits: function, parent=None):
        super().__init__()

        self.setParent(parent)
        self.setHidden(True)
        self.setGeometry(0, 0, self.parent().width(), self.parent().height())
        self.setFixedSize(self.parent().width(), self.parent().height())

        self.habitLogic = habitlogic
        self.loadHabits = loadHabbits
        self.currentHabitID = 0

        self.parentLayout = QVBoxLayout(self)

        self.mainWidget = QWidget(self)
        self.mainLayout = QVBoxLayout(self.mainWidget)

        self.upperWidget = QWidget(self.mainWidget)
        self.lowerWidget = QWidget(self.mainWidget)

        self.upperLayout = QVBoxLayout(self.upperWidget)
        self.lowerLayout = QHBoxLayout(self.lowerWidget)

        self.habitNameLabel = QLabel(self.upperWidget)
        self.habitNameLabel.setText("Habit Name")

        self.editNameInput = QLineEdit(self.upperWidget)

        self.confirmButton = QPushButton(
            "confirm",
            self.lowerWidget,
            clicked=lambda: self.onConfirm(self.currentHabitID),
        )
        self.cancelButton = QPushButton(
            "Cancel", self.lowerWidget, clicked=self.onCancel
        )

        self.UIinit()

    def UIinit(self):
        # Styles
        self.setStyleSheet("background-color: blue;")

        self.upperWidget.setStyleSheet("background-color: red;")
        self.lowerWidget.setStyleSheet("background-color: green;")

        self.habitNameLabel.setStyleSheet("Background-color: black;")

        # Widgets
        self.parentLayout.addWidget(self.mainWidget)

        self.mainLayout.addWidget(self.upperWidget)
        self.mainLayout.addWidget(self.lowerWidget)

        self.upperLayout.addWidget(
            self.habitNameLabel,
            alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft,
        )
        self.upperLayout.addWidget(self.editNameInput)

        self.lowerLayout.addWidget(self.confirmButton)
        self.lowerLayout.addWidget(self.cancelButton)

    def loadUI(self, habitID: int):
        self.currentHabitID = habitID
        self.habitNameLabel.setText(
            self.habitLogic.habitData[self.currentHabitID]["Name"]
        )
        self.editNameInput.setText(
            self.habitLogic.habitData[self.currentHabitID]["Name"]
        )
        self.setHidden(False)

    def onCancel(self):
        self.setHidden(True)

    def onConfirm(self, habitID: int):
        self.habitLogic.updateHabit(habitID, self.editNameInput.text())
        self.loadHabits()
        self.setHidden(True)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Habit Tracker")
        self.setGeometry(750, 250, 500, 550)
        self.setFixedSize(500, 550)

        self.HabitLogic = Core.HabitLogic()

        # Main Widget
        self.mainWidget = QWidget(self)
        self.editHabitWidget = EditHabit(self.HabitLogic, self.loadHabits, self)

        self.setCentralWidget(self.mainWidget)
        self.mainLayout = QVBoxLayout(self.mainWidget)

        # top Widget
        self.topWidget = QWidget(self.mainWidget)
        self.topLayout = QHBoxLayout(self.topWidget)

        self.appName = QLabel("Habit Tracker", self.topWidget)

        # Add habit Widget
        self.AddhabitWidget = AddHabitWidget(
            self.HabitLogic, self.loadHabits, self.mainWidget
        )
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

        # /--Alignments
        self.appName.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.topWidget.setStyleSheet("background-color: #222222;")
        self.AddhabitWidget.setStyleSheet("background-color: #222222;")
        self.appName.setStyleSheet(
            "color: white; background-color: red; font-size: 20px; font-weight: bold;"
        )

        # Apply to your Scroll Area or Widget
        self.ScrollArea.setStyleSheet(Styles.scrollbar_stylesheet)
        self.ScrollContent.setStyleSheet("background-color: #222222;")

    def loadLayouts(self):
        # Main Widget
        self.mainLayout.addWidget(self.topWidget)
        self.mainLayout.addWidget(self.AddhabitWidget)
        self.mainLayout.addWidget(self.ScrollArea)
        # /-Alignments

        # Top widget
        self.topLayout.addWidget(self.appName, alignment=Qt.AlignmentFlag.AlignLeft)

    def loadHabits(self):
        self.deleteWidgets()
        for key, value in self.HabitLogic.habitData.items():
            # Create habit widget--
            habitWidget = QLabel(self.ScrollContent)
            habitWidget.setProperty("HabitID", key)
            habitLayout = QHBoxLayout(habitWidget)
            habitWidget.setStyleSheet("background-color: red;")
            habitWidget.setFixedSize(425, 50)
            self.ScrollAreaLayout.addWidget(
                habitWidget, alignment=Qt.AlignmentFlag.AlignTop
            )

            # Habit Title
            habitName = QLabel(habitWidget)

            habitLayout.addWidget(habitName)
            habitName.setText(value["Name"])
            habitName.setAlignment(Qt.AlignmentFlag.AlignCenter)
            habitName.setStyleSheet(
                "background-color: blue;color: white; font-size: 20px; font-weight: bold;"
            )
            habitName.setFixedSize(200, 35)

            # Habit Checkbox
            habitCheckbox = QCheckBox(habitWidget)
            habitLayout.addWidget(habitCheckbox, alignment=Qt.AlignmentFlag.AlignCenter)
            habitCheckbox.setChecked(value["IsCompleted"])
            habitCheckbox.setStyleSheet("background-color: green;")

            # Habit Options
            habitOptions = QToolButton(habitWidget)
            habitLayout.addWidget(habitOptions)
            # habitOptions.setText("...")
            habitOptions.setAutoRaise(True)
            # habitOptions.setCheckable = True

            act_edit = QAction("Edit", habitOptions)
            act_delete = QAction("Delete", habitOptions)
            act_view = QAction("View", habitOptions)

            habitOptionsMenu = QMenu(habitOptions)
            habitOptionsMenu.addAction(act_edit)
            habitOptionsMenu.addSeparator()
            habitOptionsMenu.addAction(act_delete)
            habitOptionsMenu.addSeparator()
            habitOptionsMenu.addAction(act_view)
            habitOptions.setMenu(habitOptionsMenu)

            habitOptions.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)

            # Input Handling

            habitCheckbox.stateChanged.connect(
                lambda state, HabitId=key: self.habitStateChanged(state, HabitId)
            )

            act_edit.triggered.connect(
                lambda state, HabitId=key: self.onEditHabitClicked(state, HabitId)
            )
            act_delete.triggered.connect(
                lambda state, HabitId=key: self.onDeleteHabitClicked(state, HabitId)
            )
            act_view.triggered.connect(self.onHabitClicked)

    def deleteWidgets(self):
        for child in self.ScrollContent.children():
            if isinstance(child, QWidget):
                self.ScrollAreaLayout.removeWidget(child)
                child.setParent(None)
                child.deleteLater()

    def habitStateChanged(self, state, habitID):
        print("habitID")
        if state == Qt.CheckState.Checked.value:
            self.HabitLogic.completeHabit(habitID)
        else:
            self.HabitLogic.unCompleteHabit(habitID)

    def onHabitClicked(self):
        print("Menu Clicked")

    def onEditHabitClicked(self, state=None, HabitID=None):
        print("edit clicked")
        self.editHabitWidget.loadUI(HabitID)
        self.loadHabits()

    def onDeleteHabitClicked(self, state, HabitID):
        print("Delete clicked")
        self.HabitLogic.deleteHabit(HabitID)
        self.loadHabits()

    def onViewHabitClicked(self, state, HabitID):
        print("edit clicked")
        self.loadHabits()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
