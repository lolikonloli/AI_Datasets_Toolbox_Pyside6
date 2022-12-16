#pyside6
from PySide6.QtWidgets import QWidget


#ui相关
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader


class MainWindow(QWidget):

    def __init__(self) -> None:
        super().__init__()

        # 加载ui文件
        ui_file = QFile('./page/main_window.ui')
        ui_file.open(QFile.ReadOnly)
        ui_file.close()

        # 创建ui窗口对象
        self.ui = QUiLoader().load(ui_file)