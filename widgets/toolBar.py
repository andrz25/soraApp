from PySide6.QtCore import QTextStream
from PySide6.QtWidgets import QToolBar, QHBoxLayout, QWidget, QSizePolicy


class ToolBar(QToolBar):
    def __init__(self):
        super().__init__()

        self.setMovable(False)

        # Style
        self.setStyleSheet("""
                background-color: white;
                color: black;
                """)

        # Layout
        layout = QHBoxLayout()

        # Actions

        # Focus
        self.addAction("Focus")

        # Progress
        self.addAction("Progress")

        # Notification
        self.addAction("Notifications")

        # About
        self.addAction("About")

        # Settings
        self.addAction("Settings")

        #

