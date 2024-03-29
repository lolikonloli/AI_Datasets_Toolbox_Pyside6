from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import QThread, Signal

import random
import os
import shutil

from module.application import Application
import module.utils as utils


class MultiRunnerDatasetSplit():

    def __init__(self, window: Application) -> None:
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

        radio = self.window.ui.p3_le_radio.text()
        self.radio = (float(i) for i in radio.split(' '))

        self.image_transformer_dataset_thread = ImageTransformerDatasetSplitThread(self.read_img_folder_path,
                                                                                   self.read_gt_folder_path,
                                                                                   self.save_folder_path, self.radio)
        self.image_transformer_dataset_thread.singal_update_pb_process_p3.connect(self.update_process)
        self.image_transformer_dataset_thread.start()


class ImageTransformerDatasetSplitThread(QThread):
    singal_update_pb_process_p3 = Signal(int)

    def __init__(self, read_img_folder_path: str, read_gt_folder_path: str, save_folder_path: str,
                 radio: tuple) -> None:
        self.read_img_folder_path = read_img_folder_path
        self.read_gt_folder_path = read_gt_folder_path
        self.save_folder_path = save_folder_path
        self.radio = radio
        super().__init__()

    def run(self) -> None:
        train_save_path = self.save_folder_path + '/' + 'train'
        val_save_path = self.save_folder_path + '/' + 'val'
        test_save_path = self.save_folder_path + '/' + 'test'
        utils.clear_or_create_folder(train_save_path)
        utils.clear_or_create_folder(val_save_path)
        utils.clear_or_create_folder(test_save_path)

        train_img_path = train_save_path + '/' + 'img'
        train_gt_path = train_save_path + '/' + 'gt'

        val_img_path = val_save_path + '/' + 'img'
        val_gt_path = val_save_path + '/' + 'gt'

        test_img_path = test_save_path + '/' + 'img'
        test_gt_path = test_save_path + '/' + 'gt'

        os.mkdir(train_img_path)
        os.mkdir(train_gt_path)
        os.mkdir(val_img_path)
        os.mkdir(val_gt_path)
        os.mkdir(test_img_path)
        os.mkdir(test_gt_path)

        img_name_list = os.listdir(self.read_img_folder_path)
        random.shuffle(img_name_list)

        train, val, test = self.radio
        proportion_train_val = int(train * len(img_name_list))
        proportion_val_test = int((train + val) * len(img_name_list))
        train_list = img_name_list[:proportion_train_val]
        val_list = img_name_list[proportion_train_val:proportion_val_test]
        test_list = img_name_list[proportion_val_test:]

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

        for img_name in test_list:
            img_path = self.read_img_folder_path + '/' + img_name
            gt_path = self.read_gt_folder_path + '/' + img_name

            save_img_path = test_img_path + '/' + img_name
            save_gt_path = test_gt_path + '/' + img_name

            shutil.copy(img_path, save_img_path)
            shutil.copy(gt_path, save_gt_path)

            process += 1
            self.singal_update_pb_process_p3.emit(int(100 * process / num_img))
