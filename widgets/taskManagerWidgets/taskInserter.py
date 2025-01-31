from PySide6.QtWidgets import QLineEdit, QWidget, QHBoxLayout, QLabel

class TaskInserter(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()

        label = QLabel("Add Task: ")

        line_input = QLineEdit(self)

        layout.addWidget(label)
        layout.addWidget(line_input)

        # Input
        line_input.returnPressed.connect(print)

        self.setLayout(layout)


