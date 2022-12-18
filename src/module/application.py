#pyside6
from PySide6.QtWidgets import QMainWindow
from ui.ui_application import Ui_main


class Application(QMainWindow):

    def __init__(self) -> None:
        super().__init__()

        self.ui = Ui_main()
        self.ui.setupUi(self)
