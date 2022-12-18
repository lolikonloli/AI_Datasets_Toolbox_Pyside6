from module.main_window import MainWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import QThread, Signal
import random
import os
import shutil

import module.utils as utils


class ImageTransformerDatasetSplit():

    def __init__(self, window: MainWindow) -> None:
        self.window = window
        self.window.ui.bt_read_img_folder_path_p3.clicked.connect(self.get_read_img_folder)
        self.window.ui.bt_read_gt_folder_path_p3.clicked.connect(self.get_read_gt_folder)
        self.window.ui.bt_save_folder_path_p3.clicked.connect(self.get_save_folder)
        self.window.ui.bt_start_process_p3.clicked.connect(self.start_process)

    def get_read_img_folder(self):
        self.read_img_folder_path = utils.read_and_set_folder_path(self.window, '选择读取的文件夹',
                                                               self.window.ui.bt_read_img_folder_path_p3)
    def get_read_gt_folder(self):
        self.read_gt_folder_path = utils.read_and_set_folder_path(self.window, '选择读取的文件夹',
                                                               self.window.ui.bt_read_gt_folder_path_p3)

    def get_save_folder(self):
        self.save_folder_path = utils.read_and_set_folder_path(self.window, '选择保存的文件夹',
                                                               self.window.ui.lb_save_folder_path_p3)

    def update_process(self, progress: int):
        self.window.ui.pb_process_p3.setValue(progress)


    def start_process(self):
        self.train_radio = float(self.window.ui.le_train_radio.text())
        assert self.train_radio > 0 and self.train_radio < 1, QMessageBox.critical(self.window, '警告', '请输入0-1之间的1位小数')

        self.image_transformer_dataset_thread = ImageTransformerDatasetSplitThread(self.read_img_folder_path,
                                                                                   self.read_gt_folder_path,
                                                                                   self.save_folder_path,
                                                                                   self.train_radio)
        self.image_transformer_dataset_thread.singal_update_pb_process_p3.connect(self.update_process)
        self.image_transformer_dataset_thread.start()


class ImageTransformerDatasetSplitThread(QThread):
    singal_update_pb_process_p3 = Signal(int)

    def __init__(self, read_img_folder_path: str, read_gt_folder_path: str, save_folder_path: str, train_radio: float) -> None:
        self.read_img_folder_path = read_img_folder_path
        self.read_gt_folder_path = read_gt_folder_path
        self.save_folder_path = save_folder_path
        self.train_radio = train_radio
        super().__init__()

    def run(self) -> None:
        train_save_path = self.save_folder_path + '/' + 'train'
        val_save_path = self.save_folder_path + '/' + 'val'
        utils.clear_or_create_folder(train_save_path)
        utils.clear_or_create_folder(val_save_path)

        train_img_path = train_save_path + '/' + 'img'
        train_gt_path = train_save_path + '/' + 'gt'

        val_img_path = val_save_path + '/' + 'img'
        val_gt_path = val_save_path + '/' + 'gt'

        os.mkdir(train_img_path)
        os.mkdir(train_gt_path)
        os.mkdir(val_img_path)
        os.mkdir(val_gt_path)

        img_name_list = os.listdir(self.read_img_folder_path)
        random.shuffle(img_name_list)

        proportion = int(self.train_radio * len(img_name_list))
        train_list = img_name_list[:proportion]
        val_list = img_name_list[proportion:]

        process = 1
        num_img = len(img_name_list)

        for img_name in train_list:
            img_path = self.read_img_folder_path + '/' + img_name
            gt_path = self.read_gt_folder_path + '/' + img_name

            save_img_path = train_img_path + '/' + img_name
            save_gt_path = train_gt_path + '/' + img_name

            shutil.copy(img_path, save_img_path)
            shutil.copy(gt_path, save_gt_path)


            process += 1
            self.singal_update_pb_process_p3.emit(int(100 * process / num_img))

        for img_name in val_list:
            img_path = self.read_img_folder_path + '/' + img_name
            gt_path = self.read_gt_folder_path + '/' + img_name

            save_img_path = val_img_path + '/' + img_name
            save_gt_path = val_gt_path + '/' + img_name

            shutil.copy(img_path, save_img_path)
            shutil.copy(gt_path, save_gt_path)

            process += 1
            self.singal_update_pb_process_p3.emit(int(100 * process / num_img))
