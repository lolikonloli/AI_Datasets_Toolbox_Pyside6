import cv2
from module.application import Application
from PySide6 import QtCore
from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QFileDialog
import shutil
import os


def transform_mat_to_qpixel(img: cv2.Mat, width: int, height: int):
    cv_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    qt_img = QImage(cv_img, cv_img.shape[1], cv_img.shape[0], cv_img.strides[0], QImage.Format_RGB888)
    qt_pixel = QPixmap(qt_img).scaled(width, height, QtCore.Qt.KeepAspectRatio)
    return qt_pixel


def transform_pixel(img: cv2.Mat, input_num: int, output_num: int):
    target = img.copy()
    target[target == input_num] = output_num
    return target

#读取文件夹 并设置到label上
def read_and_set_folder_path(window: Application, messege: str, label: QLabel):
    path = QFileDialog.getExistingDirectory(window, messege)
    label.setText(path)
    return path

def clear_or_create_folder(path: str):
    if os.path.exists(path):
        shutil.rmtree(path)
        os.mkdir(path)
    else:
        os.mkdir(path)
