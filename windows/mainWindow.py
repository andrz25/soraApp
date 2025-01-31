from PySide6.QtWidgets import QMainWindow
from widgets.toolBar import ToolBar
from widgets.central import Central


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sora")

        # Settings
        self.resize(800, 600)

        # Toolbar
        self.addToolBar(ToolBar())

        # Central
        self.setCentralWidget(Central())

