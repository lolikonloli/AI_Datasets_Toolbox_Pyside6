from module.application import Application
from PySide6.QtWidgets import QFileDialog

import os
import cv2

from PySide6 import QtCore
from PySide6.QtCore import QThread



class ImageTransformerGrayscale():

    def __init__(self, window: Application) -> None:
        self.window = window

        self.window.ui.bt_read_folder_path.clicked.connect(self.select_image_read_folder)
        self.window.ui.bt_save_folder_path.clicked.connect(self.select_image_save_folder)
        self.window.ui.bt_start_process.clicked.connect(self.start_process)

    def select_image_read_folder(self):
        self.img_read_path = QFileDialog.getExistingDirectory(self.window, '选择图片文件夹')
        self.window.ui.lb_read_folder_path.setText(self.img_read_path)

    def select_image_save_folder(self):
        self.img_save_path = QFileDialog.getExistingDirectory(self.window, '选择图片文件夹')
        self.window.ui.lb_save_folder_path.setText(self.img_save_path)

    def start_process(self):
        origin = int(self.window.ui.le_pixel_oringin.text())
        target = int(self.window.ui.le_pixel_saveas.text())

        self.image_transformer_thread = ImageTransformerThread(origin, target, self.img_read_path, self.img_save_path)
        self.image_transformer_thread.singal_update_pb_process.connect(self.update_process)

        self.image_transformer_thread.start()

    def update_process(self, progress: int):
        print('update_progress')
        self.window.ui.pb_process.setValue(progress)


class ImageTransformerThread(QThread):
    singal_update_pb_process = QtCore.Signal(int)

    def __init__(self, origin, target, img_read_folderpath, img_save_folderpath) -> None:
        self.origin = origin
        self.target = target
        self.img_read_folderpath = img_read_folderpath
        self.img_save_folderpath = img_save_folderpath
        super().__init__()

    def run(self) -> None:
        img_list = os.listdir(self.img_read_folderpath)

        threshold = 128
        num_img = len(img_list)

        for i, img_name in enumerate(img_list):
            img_path = self.img_read_folderpath + '/' + img_name
            img_save_path = self.img_save_folderpath + '/' + img_name

            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            img[img < threshold] = 0
            img[img >= threshold] = 255
            cvimg_transformed = img.copy()
            cvimg_transformed[cvimg_transformed == self.origin] = self.target
            cv2.imwrite(img_save_path, cvimg_transformed)

            self.singal_update_pb_process.emit(int(100 * (i+1) / num_img))
