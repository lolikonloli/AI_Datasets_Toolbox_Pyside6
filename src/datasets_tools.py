#pyside6
from PySide6.QtWidgets import QApplication

#ui
import sys
from qt_material import apply_stylesheet

#module
from module.image_viewer import ImageViewer
from module.image_transformer_grayscale import ImageTransformerGrayscale
from module.main_window import MainWindow

#main
app = QApplication(sys.argv)

window = MainWindow()
image_transformer_grayscale = ImageTransformerGrayscale(window)
image_viewer = ImageViewer(window)

apply_stylesheet(app, theme='dark_teal.xml')

window.ui.show()
app.exec()