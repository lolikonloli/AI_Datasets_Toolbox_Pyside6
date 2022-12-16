from PySide6.QtWidgets import QFileDialog

from module.main_window import MainWindow
import module.utils as utils

from loguru import logger
import cv2


class ImageViewer():

    def __init__(self, window: MainWindow) -> None:
        self.window = window
        self.window.ui.bt_read_image_path.clicked.connect(self.show_image)

    def show_image(self):
        logger.debug('bt_read_image_path clicked')
        image_path = QFileDialog.getOpenFileName(self.window, '选择图片')[0]

        cv_img = cv2.imread(image_path)

        qt_pixel_oringin = utils.transform_mat_to_qpixel(cv_img, self.window.ui.lb_image_show_oringin.width(),
                                                         self.window.ui.lb_image_show_oringin.height())
        self.window.ui.lb_image_show_oringin.setPixmap(qt_pixel_oringin)

        cv_img_transformed = utils.transform_pixel(cv_img, 0, 124)

        qt_pixel_transformed = utils.transform_mat_to_qpixel(cv_img_transformed,
                                                             self.window.ui.lb_image_show_transformed.width(),
                                                             self.window.ui.lb_image_show_transformed.height())
        self.window.ui.lb_image_show_transformed.setPixmap(qt_pixel_transformed)
