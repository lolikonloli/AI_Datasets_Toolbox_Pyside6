from module.main_window import MainWindow
from PySide6.QtWidgets import QFileDialog

import os
import cv2


class ImageTransformer():

    def __init__(self, window: MainWindow) -> None:
        self.window = window

        self.window.ui.bt_read_folder_path.clicked.connect(self.select_image_read_folder)
        self.window.ui.bt_save_folder_path.clicked.connect(self.select_image_save_folder)
        self.window.ui.bt_start_process.clicked.connect(self.start_process)
        # self.window.ui.pb_process.set

    def select_image_read_folder(self):
        self.img_read_path = QFileDialog.getExistingDirectory(self.window, '选择图片文件夹')
        self.window.ui.lb_read_folder_path.setText(self.img_read_path)

    def select_image_save_folder(self):
        self.img_save_path = QFileDialog.getExistingDirectory(self.window, '选择图片文件夹')
        self.window.ui.lb_save_folder_path.setText(self.img_save_path)

    def start_process(self):
        origin = int(self.window.ui.le_pixel_oringin.text())
        target = int(self.window.ui.le_pixel_saveas.text())

        img_read_folderpath = f'G:/datasets/balraj98-cvcclinicdb/PNG/Ground Truth'
        img_save_folderpath = f'G:/datasets/balraj98-cvcclinicdb/PNG/GT_trans'

        img_list = os.listdir(img_read_folderpath)

        threshold = 128
        num_img = len(img_list)
        for i, img_name in enumerate(img_list):
            self.window.ui.pb_process.setValue(int(i/num_img))

            img_path = img_read_folderpath + '/' + img_name
            img_save_path = img_save_folderpath + '/' + img_name

            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            img[img < threshold] = 0
            img[img >= threshold] = 255
            cvimg_transformed = img.copy()
            cvimg_transformed[cvimg_transformed == origin] = target
            cv2.imwrite(img_save_path, cvimg_transformed)