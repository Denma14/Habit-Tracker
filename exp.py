import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QGroupBox,
)
from PyQt6.QtCore import Qt


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QGroupBox Example")
        self.resize(500, 300)

        # Central widget
        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QVBoxLayout(central)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)

        # Create GroupBox
        group = QGroupBox("Add Habit")
        group_layout = QVBoxLayout(group)

        group_layout.addWidget(QLabel("Habit name:"))
        group_layout.addWidget(QPushButton("Save Habit"))

        main_layout.addWidget(group)

        # Optional: Style it to look cleaner
        self.setStyleSheet(
            """
            QGroupBox {
                border: 2px solid #555;
                border-radius: 8px;
                margin-top: 12px;
                font-weight: bold;
            }

            QGroupBox::title {
                subcontrol-origin: margin;
                left: 12px;
                padding: 0 6px 0 6px;
                color: #00aa88;
            }
        """
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
