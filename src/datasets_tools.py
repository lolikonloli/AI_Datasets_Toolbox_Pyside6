#pyside6
from PySide6.QtWidgets import QApplication
from qt_material import apply_stylesheet

from module.application import Application
from module.runner_image_viewer import ImageViewer
from module.runner_image_transformer_grayscale import ImageTransformerGrayscale
from module.runner_image_transformer_dataset_split import ImageTransformerDatasetSplit

if __name__ == '__main__':
    q_appication = QApplication()

    app = Application()
    apply_stylesheet(app, theme='dark_teal.xml')

    image_viewer = ImageViewer(app)
    image_transformer_grayscale = ImageTransformerGrayscale(app)
    image_transformer_dataset_split = ImageTransformerDatasetSplit(app)

    app.show()

    q_appication.exec()