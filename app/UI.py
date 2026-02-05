# UI file
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt
from . import Core
from . import Styles


class AddHabitDialog(QDialog):
    def __init__(self, HabitLogic: Core.HabitLogic, parent=None):
        super().__init__()

        self.HabitLogic = HabitLogic

        self.setWindowTitle("Add New Habit")
        self.setGeometry(50, 50, 150, 150)
        self.setFixedSize(300, 150)

        self.dialogMainWidget = QWidget(self)
        self.dialogMainWidget.setFixedSize(300, 150)

        self.upperDialogWidget = QWidget(self.dialogMainWidget)
        self.lowerDialogWidget = QWidget(self.dialogMainWidget)

        self.dialogMainLayout = QVBoxLayout(self.dialogMainWidget)
        # self.dialogLayout = QVBoxLayout(self.addHabitDialog)
        self.upperDialogLayout = QHBoxLayout(self.upperDialogWidget)
        self.lowerDialogLayout = QHBoxLayout(self.lowerDialogWidget)

        self.habitNameInput = QLineEdit("Enter Habit Name", self.upperDialogWidget)
        self.dialogConfirmButton = QPushButton("Add Habit", self.lowerDialogWidget)
        self.dialogCancelButton = QPushButton("Cancel", self.lowerDialogWidget)

        self.dialogMainLayout.addWidget(
            self.upperDialogWidget, alignment=Qt.AlignmentFlag.AlignCenter
        )
        self.dialogMainLayout.addWidget(
            self.lowerDialogWidget, alignment=Qt.AlignmentFlag.AlignCenter
        )
        self.upperDialogLayout.addWidget(
            self.habitNameInput, alignment=Qt.AlignmentFlag.AlignCenter
        )
        self.lowerDialogLayout.addWidget(self.dialogConfirmButton)
        self.lowerDialogLayout.addWidget(self.dialogCancelButton)

        self.dialogConfirmButton.clicked.connect(self.confirmAddHabit)
        self.dialogCancelButton.clicked.connect(self.close)

    def confirmAddHabit(self):
        self.HabitLogic.createHabit(self.habitNameInput.text())
        self.close()

    def addHabit(self):
        print(self.habitNameInput.text())


class EditHabit(QWidget):
    def __init__(self, habitlogic: Core.HabitLogic, parent=None):
        super().__init__()

        self.setParent(parent)
        self.setHidden(True)
        self.setGeometry(0, 0, self.parent().width(), self.parent().height())
        self.setFixedSize(self.parent().width(), self.parent().height())

        self.habitLogic = habitlogic

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

        self.confirmButton = QPushButton("confirm", self.lowerWidget)
        self.cancelButton = QPushButton("Cancel", self.lowerWidget)

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
        self.habitNameLabel.setText(self.habitLogic.habitData[habitID]["Name"])
        self.editNameInput.setText(self.habitLogic.habitData[habitID]["Name"])
        self.setHidden(False)

        # self.confirmButton.clicked.connect(lambda: self.onConfirm(habitID))
        # self.cancelButton.clicked.connect(self.onCancel)

    def onCancel(self):
        self.setHidden(True)

    def onConfirm(self, habitID: int, loadHabits: function):
        self.habitLogic.updateHabit(habitID, self.editNameInput.text())
        # loadHabits()
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
        self.editHabitWidget = EditHabit(self.HabitLogic, self)
        self.setCentralWidget(self.mainWidget)
        self.mainLayout = QVBoxLayout(self.mainWidget)

        # top Widget
        self.topWidget = QWidget(self.mainWidget)
        self.topLayout = QHBoxLayout(self.topWidget)

        self.appName = QLabel("Habit Tracker", self.topWidget)
        self.addHabitButton = QPushButton(
            "Add Habit", self.topWidget, clicked=self.onAddHabitClicked
        )

        self.addDialog = AddHabitDialog(self.HabitLogic, self)

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
                lambda state, key=habitWidget.property(
                    "HabitID"
                ): self.habitStateChanged(state, key)
            )

            act_edit.triggered.connect(
                lambda state, key=habitWidget.property(
                    "HabitID"
                ): self.onEditHabitClicked(state, key)
            )
            act_delete.triggered.connect(
                lambda state, key=habitWidget.property(
                    "HabitID"
                ): self.onDeleteHabitClicked(state, key)
            )
            act_view.triggered.connect(self.onHabitClicked)

    def deleteWidgets(self):
        for child in self.ScrollContent.children():
            if isinstance(child, QWidget):
                self.ScrollAreaLayout.removeWidget(child)
                child.setParent(None)
                child.deleteLater()

    def onAddHabitClicked(self):
        self.addDialog.exec()
        self.loadHabits()

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
        self.editHabitWidget.confirmButton.clicked.connect(
            lambda: self.editHabitWidget.onConfirm(HabitID, self.loadHabits)
        )
        self.editHabitWidget.cancelButton.clicked.connect(self.editHabitWidget.onCancel)

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
