# UI file
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt, QTimer
from . import Core
from . import Helper
from . import Styles


class AddHabitWidget(QWidget):
    def __init__(
        self,
        HabitLogic: Core.HabitLogic,
        loadHabits: function,
        actionFeedback: function,
        parent=None,
    ):
        super().__init__()

        # self.setParent(parent)
        self.loadHabits = loadHabits
        self.actionFeedback = actionFeedback

        self.HabitLogic = HabitLogic
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setFixedHeight(40)
        self.setStyleSheet("background-color: #222222;" "")

        self.mainLayout = QHBoxLayout(self)
        self.habitNameInput = QLineEdit("Enter new habit name", self)
        self.confirmButton = QPushButton("Confirm", self, clicked=self.onConfirm)

        self.habitNameInput.setStyleSheet("font-weight: bold;")
        self.confirmButton.setStyleSheet("background-color: green;")

        self.mainLayout.addWidget(self.habitNameInput)
        self.mainLayout.addWidget(self.confirmButton)

    def onConfirm(self):
        bool, xdx = self.HabitLogic.createHabit(self.habitNameInput.text())
        print(bool, xdx)
        if not bool:
            self.habitNameInput.setText(xdx)
        else:
            self.habitNameInput.setText("Enter new habit name")
        self.loadHabits()
        self.actionFeedback("Habit created")


class EditHabit(QWidget):
    def __init__(
        self,
        habitlogic: Core.HabitLogic,
        loadHabbits: function,
        actionFeedback: function,
        parent=None,
    ):
        super().__init__()

        self.setParent(parent)
        self.setHidden(True)
        self.setGeometry(0, 0, self.parent().width(), self.parent().height())
        self.setFixedSize(self.parent().width(), self.parent().height())
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self.habitLogic = habitlogic
        self.loadHabits = loadHabbits
        self.actionFeedback = actionFeedback
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
            "Confirm",
            self.lowerWidget,
            clicked=lambda: self.onConfirm(self.currentHabitID),
        )
        self.cancelButton = QPushButton(
            "Cancel", self.lowerWidget, clicked=self.onCancel
        )

        self.UIinit()

    def UIinit(self):
        # Sizes
        self.habitNameLabel.setFixedSize(200, 50)

        self.editNameInput.setFixedSize(300, 50)

        self.confirmButton.setFixedSize(200, 80)
        self.cancelButton.setFixedSize(200, 80)
        # Alignments
        self.habitNameLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.editNameInput.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Styles
        self.setStyleSheet("background-color: #222222;")

        # self.upperWidget.setStyleSheet("background-color: red;")
        # self.lowerWidget.setStyleSheet("background-color: green;")

        self.habitNameLabel.setStyleSheet(
            "Background-color: black; "
            "color: white; "
            "font-size: 20px; "
            "font-weight: bold;"
            "border-radius: 10px;"
            "border: 2px solid white;"
        )
        self.editNameInput.setStyleSheet(
            "Background-color: #303030; "
            "color: white; "
            "font-size: 20px; "
            "font-weight: bold;"
        )
        self.confirmButton.setStyleSheet(
            "background-color: #222222;"
            "font-size: 20px;"
            "font-weight: bold;"
            "border-radius: 10px;"
            "border: 2px solid #22ff22;"
        )
        self.cancelButton.setStyleSheet(
            "background-color: #222222;"
            "font-size: 20px;"
            "font-weight: bold;"
            "border-radius: 10px;"
            "border: 2px solid #ff2222;"
        )

        # Widgets
        self.parentLayout.addWidget(self.mainWidget)

        self.mainLayout.addWidget(self.upperWidget)
        self.mainLayout.addWidget(self.lowerWidget)

        self.upperLayout.addWidget(
            self.habitNameLabel,
            alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter,
        )
        self.upperLayout.addWidget(
            self.editNameInput,
            alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter,
        )

        self.lowerLayout.addWidget(
            self.confirmButton, alignment=Qt.AlignmentFlag.AlignBottom
        )
        self.lowerLayout.addWidget(
            self.cancelButton, alignment=Qt.AlignmentFlag.AlignBottom
        )

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
        self.actionFeedback("Habit updated")


class ViewHabit(QWidget):
    def __init__(self, habitlogic: Core.HabitLogic, loadHabbits: function, parent=None):
        super().__init__()

        self.setParent(parent)
        self.setHidden(True)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

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

        self.upperLayout = QHBoxLayout(self.upperWidget)
        self.lowerLayout = QVBoxLayout(self.lowerWidget)

        self.habitNameLabel = QLabel(self.upperWidget)
        self.habitNameLabel.setText("Habit Name")

        self.streakLabel = QLabel("Streak", self.upperWidget)

        self.backButton = QPushButton("Back", self.upperWidget, clicked=self.onBack)

        self.UIinit()

    def UIinit(self):
        self.setStyleSheet("background-color: blue;")

        self.upperWidget.setStyleSheet("background-color: red;")
        self.lowerWidget.setStyleSheet("background-color: yellow;")
        self.habitNameLabel.setStyleSheet("Background-color: black;")

        self.upperWidget.setFixedHeight(50)
        self.habitNameLabel.setFixedHeight(30)

        self.parentLayout.addWidget(self.mainWidget)

        self.mainLayout.addWidget(self.upperWidget)
        self.mainLayout.addWidget(self.lowerWidget)

        self.upperLayout.addWidget(
            self.streakLabel, alignment=Qt.AlignmentFlag.AlignLeft
        )
        self.upperLayout.addWidget(
            self.habitNameLabel,
            alignment=Qt.AlignmentFlag.AlignHCenter,
        )
        self.upperLayout.addWidget(
            self.backButton, alignment=Qt.AlignmentFlag.AlignRight
        )

    def onBack(self):
        self.setHidden(True)

    def loadUI(self, habitID: int):
        self.currentHabitID = habitID
        self.habitNameLabel.setText(
            self.habitLogic.habitData[self.currentHabitID]["Name"]
        )
        self.streakLabel.setText(
            f"Streak: {self.habitLogic.habitData[self.currentHabitID]['Streak']}"
        )
        self.loadDates(self.currentHabitID)
        self.setHidden(False)

    def loadDates(self, habitID: int):
        self.currentHabitID = habitID
        self.deleteWidgets()
        for i in range(14):
            newDate = QLabel(
                Helper.dateGetter(i, "abbr"), self.lowerWidget
            )  # abbr = abbrieviation
            newDate.date = Helper.dateGetter(i)
            if (
                newDate.date
                in self.habitLogic.habitData[self.currentHabitID]["CompletedDates"]
            ):
                newDate.setStyleSheet("Background-color: green;")
            else:
                newDate.setStyleSheet("Background-color: red;")
            self.lowerLayout.addWidget(newDate)

    def deleteWidgets(self):
        for child in self.lowerWidget.children():
            if isinstance(child, QWidget):
                self.lowerLayout.removeWidget(child)
                child.setParent(None)
                child.deleteLater()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Habit Tracker")
        self.setGeometry(750, 250, 500, 550)
        self.setFixedSize(500, 550)

        self.HabitLogic = Core.HabitLogic()

        # Main Widget
        self.mainWidget = QWidget(self)
        self.editHabitWidget = EditHabit(
            self.HabitLogic, self.loadHabits, self.actionFeedback, self
        )
        self.viewHabitWidget = ViewHabit(self.HabitLogic, self.loadHabits, self)

        self.setCentralWidget(self.mainWidget)
        self.mainLayout = QVBoxLayout(self.mainWidget)

        # top Widget
        self.topWidget = QWidget(self.mainWidget)
        self.topLayout = QHBoxLayout(self.topWidget)
        self.appName = QLabel("Habit Tracker", self.topWidget)

        # Add habit Widget
        self.AddhabitWidget = AddHabitWidget(
            self.HabitLogic, self.loadHabits, self.actionFeedback, self.mainWidget
        )

        # Scroll Area
        self.ScrollArea = QScrollArea(self.mainWidget)
        # elf.topLayout.addWidget(self.ScrollArea)
        self.ScrollArea.setWidgetResizable(True)
        self.ScrollContent = QWidget(self.ScrollArea)

        self.ScrollAreaLayout = QVBoxLayout(self.ScrollContent)
        self.ScrollAreaLayout.setContentsMargins(5, 10, 5, 10)
        self.ScrollAreaLayout.setSpacing(5)
        self.ScrollAreaLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        # self.ScrollAreaLayout.addStretch(1)  # <-- important

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
        self.appName.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")

        print(self.AddhabitWidget.styleSheet())
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
        self.topLayout.addWidget(self.appName, alignment=Qt.AlignmentFlag.AlignCenter)

    def loadHabits(self):
        self.deleteWidgets()
        self.dateBarInit()

        for key, value in self.HabitLogic.habitData.items():
            # Instances --
            habitWidget = QLabel(self.ScrollContent)
            habitWidgetRight = QLabel(habitWidget)
            habitWidgetLeft = QLabel(habitWidget)

            habitName = QLabel(value["Name"], habitWidgetLeft)

            habitOptions = QToolButton(habitWidget)

            act_edit = QAction("Edit", habitOptions)
            act_delete = QAction("Delete", habitOptions)
            act_view = QAction("View", habitOptions)

            habitOptionsMenu = QMenu(habitOptions)

            # Layouts --
            habitLayout = QHBoxLayout(habitWidget)
            habitWidgetRightLayout = QHBoxLayout(habitWidgetRight)
            habitwidgetLeftLayout = QHBoxLayout(habitWidgetLeft)

            # Properties --
            habitWidget.setProperty("HabitID", key)

            # Styles --
            habitWidget.setFixedSize(450, 50)
            habitName.setFixedHeight(30)
            habitwidgetLeftLayout.setContentsMargins(0, 0, 0, 0)

            habitWidget.setStyleSheet("background-color: #171616; border-radius: 5px;")
            habitName.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")

            # habitWidgetLeft.setStyleSheet("background-color: #222222;")
            # habitWidgetRight.setStyleSheet("background-color: #222222;")

            # Layout handling
            self.ScrollAreaLayout.insertWidget(
                self.ScrollAreaLayout.count(),
                habitWidget,
                alignment=Qt.AlignmentFlag.AlignHCenter,
            )
            habitLayout.addWidget(habitWidgetLeft)
            habitLayout.addWidget(habitWidgetRight)

            habitwidgetLeftLayout.addWidget(
                habitName, alignment=Qt.AlignmentFlag.AlignTop
            )

            habitLayout.addWidget(habitOptions)

            for i in range(4):
                newCheckbox = QCheckBox(habitWidgetRight)
                newCheckbox.setFixedSize(20, 20)
                habitWidgetRightLayout.addWidget(newCheckbox)
                newCheckbox.setProperty("Date", Helper.dateGetter(i))
                if newCheckbox.property("Date") in value["CompletedDates"]:
                    newCheckbox.setCheckState(Qt.CheckState.Checked)
                else:
                    newCheckbox.setCheckState(Qt.CheckState.Unchecked)
                newCheckbox.stateChanged.connect(
                    lambda state, checkbox=newCheckbox, HabitId=key, date=newCheckbox.property(
                        "Date"
                    ): self.habitStateChanged(
                        state, checkbox, HabitId, date
                    )
                )

            # Habit Options

            # habitOptions.setText("...")
            habitOptions.setAutoRaise(True)
            # habitOptions.setCheckable = True

            habitOptionsMenu.addAction(act_edit)
            habitOptionsMenu.addSeparator()
            habitOptionsMenu.addAction(act_delete)
            habitOptionsMenu.addSeparator()
            habitOptionsMenu.addAction(act_view)
            habitOptions.setMenu(habitOptionsMenu)

            habitOptions.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)

            # Input Handling

            act_edit.triggered.connect(
                lambda state, HabitId=key: self.onEditHabitClicked(state, HabitId)
            )
            act_delete.triggered.connect(
                lambda state, HabitId=key: self.onDeleteHabitClicked(state, HabitId)
            )
            act_view.triggered.connect(
                lambda state, HabitId=key: self.onViewHabitClicked(state, HabitId)
            )

    def deleteWidgets(self):
        # remove everything except the final stretch item (if you add one)
        while self.ScrollAreaLayout.count() > 0:
            item = self.ScrollAreaLayout.takeAt(0)
            w = item.widget()
            if w:
                w.deleteLater()

    def dateBarInit(self):
        dateWidget = QWidget(self.ScrollContent)
        self.ScrollAreaLayout.insertWidget(
            self.ScrollAreaLayout.count(),  # index before the stretch
            dateWidget,
            alignment=Qt.AlignmentFlag.AlignHCenter,
        )
        dateWidgetLayout = QHBoxLayout(dateWidget)
        dateWidgetLayout.setAlignment(Qt.AlignmentFlag.AlignRight)
        dateWidgetLayout.setContentsMargins(0, 0, 60, 0)
        dateWidgetLayout.setSpacing(15)
        # dateWidget.setStyleSheet("background-color: yellow;")
        dateWidget.setFixedSize(450, 20)

        for i in range(4):
            newDate = QLabel(dateWidget)
            newDate.setText(Helper.dateGetter(i, "day"))
            newDate.setFixedSize(27, 20)
            newDate.setStyleSheet("font-weight: bold; color: white;")
            dateWidgetLayout.addWidget(newDate, alignment=Qt.AlignmentFlag.AlignRight)

    def habitStateChanged(self, state, checkbox: QCheckBox, habitID, date):
        print(habitID, date)

        if state == Qt.CheckState.Checked.value:
            self.HabitLogic.completeHabit(habitID, date)
            checkbox.setStyleSheet("background-color: green;")
        else:
            self.HabitLogic.unCompleteHabit(habitID, date)
            checkbox.setStyleSheet("background-color: #171616;")

    def actionFeedback(self, message: str = "Action completed"):
        messageLabel = QLabel(message, self.mainWidget)
        messageLabel.setStyleSheet(
            "color: green; font-weight: bold; background-color: yellow;"
        )
        self.mainLayout.insertWidget(
            2, messageLabel, alignment=Qt.AlignmentFlag.AlignTop
        )
        QTimer.singleShot(3000, lambda: self.mainLayout.removeWidget(messageLabel))

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
        self.actionFeedback("Habit deleted")

    def onViewHabitClicked(self, state, HabitID):
        print("View clicked")
        self.viewHabitWidget.loadUI(HabitID)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
