# UI file
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont, QFontDatabase
from PyQt6.QtCore import Qt
import Core
import Styles


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Habit Tracker")
        self.setGeometry(750, 250, 500, 550)
        self.setFixedSize(500, 550)

        self.Logic = Core.HabitLogic()

        # Main Widget
        self.mainWidget = QWidget(self)
        self.setCentralWidget(self.mainWidget)
        self.mainLayout = QVBoxLayout(self.mainWidget)

        # top Widget
        self.topWidget = QWidget(self.mainWidget)
        self.topLayout = QVBoxLayout(self.topWidget)

        self.ScrollArea = QScrollArea(self.topWidget)
        self.topLayout.addWidget(self.ScrollArea)
        self.ScrollArea.setWidgetResizable(True)
        self.ScrollContent = QWidget(self.ScrollArea)

        self.ScrollAreaLayout = QVBoxLayout(self.ScrollContent)
        self.ScrollArea.setWidget(self.ScrollContent)

        self.loadStyles()
        self.loadLayouts()
        self.addWidgets()

    def loadStyles(self):
        # Main Widget
        self.mainWidget.setStyleSheet("background-color: #000000;")

        # Top widget
        self.topWidget.setStyleSheet("background-color: #222222;")

        # Apply to your Scroll Area or Widget
        self.ScrollArea.setStyleSheet(Styles.scrollbar_stylesheet)

    def loadLayouts(self):
        # Main Widget
        self.mainLayout.addWidget(self.topWidget)

        # Top widget

    def addWidgets(self):
        for i in range(1, 11):
            newWidget = QWidget(self.topWidget)
            self.ScrollAreaLayout.addWidget(newWidget)
            newWidget.setStyleSheet("background-color: red;")
            newWidget.setFixedSize(450, 50)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
