from module.application import Application

from PySide6.QtCore import QThread, Signal


class BaseMultiThreadRunner():
    def __init__(self, window: Application) -> None:
        pass


class BaseWorker(QThread):
    singnal_process = Signal(int)

    def __init__(self) -> None:
        super().__init__()
    
    def singal_update_process(self, process: int):
        self.singal_update_process.emit(int)

    def run(self) -> None:
        pass