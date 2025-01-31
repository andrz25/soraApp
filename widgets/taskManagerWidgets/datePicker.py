from PySide6.QtWidgets import QWidget, QHBoxLayout, QComboBox, QLabel
class DatePicker(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()

        label = QLabel("Set Date: ")

        date = QComboBox()
        month = QComboBox()
        year = QComboBox()

        layout.addWidget(label)
        layout.addWidget(date)
        layout.addWidget(month)
        layout.addWidget(year)

        self.setLayout(layout)