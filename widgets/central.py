from PySide6.QtWidgets import QWidget, QHBoxLayout
from widgets.taskManagerWidgets.taskManager import TaskManagerBar

class Central(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()
        layout.addWidget(TaskManagerBar())

        self.setLayout(layout)

