from PySide6.QtWidgets import QFileDialog
import PySide6.QtWidgets as QtWidgets

from module.application import Application
import module.utils as utils

from loguru import logger
import cv2
import os


class ImageViewer():

    def __init__(self, window: Application) -> None:
        self.window = window
        self.window.ui.bt_read_image_path.clicked.connect(self.show_image)
        self.window.ui.bt_previous.clicked.connect(self.change_previous_image)
        self.window.ui.bt_next.clicked.connect(self.change_next_image)

    def show_image(self):
        # logger.debug('bt_read_image_path clicked')
        img_path = QFileDialog.getOpenFileName(self.window, '选择图片')[0]

        if img_path is '':
            return

        #get img_name for change img when push button
        self.get_image_id(img_path)

        self.show_one_img(img_path)

    def change_previous_image(self):
        self.index = self.index - 1
        if self.index < 0:
            self.index = self.num_img - 1

        img_name = self.img_name_list[self.index]

        img_path = self.img_follder_path + '/' + img_name

        self.show_one_img(img_path)

    def change_next_image(self):
        self.index = self.index + 1
        if self.index >= self.num_img:
            self.index = 0

        img_name = self.img_name_list[self.index]

        img_path = self.img_follder_path + '/' + img_name

        self.show_one_img(img_path)

    def get_image_id(self, img_path: str):
        self.img_follder_path, img_name = os.path.split(img_path)

        self.img_name_list = os.listdir(self.img_follder_path)
        self.index = self.img_name_list.index(img_name)

        self.num_img = len(self.img_name_list)

    def show_one_img(self, img_path: str):
        # logger.debug(self.index)
        #set img_path in label
        self.window.ui.lb_image_path.setText(img_path)

        #set image in two label
        cv_img = cv2.imread(img_path)
        qt_pixel_oringin = utils.transform_mat_to_qpixel(cv_img, self.window.ui.lb_image_show_oringin.width(),
                                                         self.window.ui.lb_image_show_oringin.height())
        self.window.ui.lb_image_show_oringin.setPixmap(qt_pixel_oringin)

        cv_img_transformed = utils.transform_pixel(cv_img, 0, 124)

        qt_pixel_transformed = utils.transform_mat_to_qpixel(cv_img_transformed,
                                                             self.window.ui.lb_image_show_transformed.width(),
                                                             self.window.ui.lb_image_show_transformed.height())
        self.window.ui.lb_image_show_transformed.setPixmap(qt_pixel_transformed)
