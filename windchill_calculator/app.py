import sys

from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QDoubleSpinBox,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QSpinBox,
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Windchill Calculator")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(320, 240)

        layout = QVBoxLayout()
        title_label = QLabel("Wind Chill Calculator")

        # Temperature input
        temp_layout = QHBoxLayout()
        temp_label = QLabel("Temperature: ")
        temp_spinbox = QSpinBox()
        temp_spinbox.setSuffix(" °F")
        temp_spinbox.setMaximum(50)
        temp_layout.addWidget(temp_label)
        temp_layout.addWidget(temp_spinbox)

        # Money Input
        money_layout = QHBoxLayout()
        money_label = QLabel("Money Amount: ")
        money_spinbox = QDoubleSpinBox()
        money_spinbox.setPrefix("$ ")
        money_spinbox.setDecimals(2)
        money_spinbox.setMinimum(0.0)
        money_layout.addWidget(money_label)
        money_layout.addWidget(money_spinbox)

        # add widgets & layouts to main layout
        layout.addWidget(title_label)
        layout.addLayout(temp_layout)
        layout.addLayout(money_layout)

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. 
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
app.setStyle("Fusion")
window = MainWindow()
window.show()

app.exec()
