from PySide6.QtWidgets import QWidget, QVBoxLayout
from widgets.taskManagerWidgets.taskInserter import TaskInserter
from widgets.taskManagerWidgets.datePicker import DatePicker
from widgets.taskManagerWidgets.taskList import TaskList

class TaskManagerBar(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()

        # Insert Task
        task_inserter = TaskInserter()

        # Date
        date_picker = DatePicker()

        # Task List
        task_list = TaskList()

        # Add Widgets

        main_layout.addWidget(task_inserter)
        main_layout.addWidget(date_picker)
        main_layout.addWidget(task_list)

        self.setLayout(main_layout)
