# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QWidget)

class Ui_main(object):
    def setupUi(self, main):
        if not main.objectName():
            main.setObjectName(u"main")
        main.resize(852, 563)
        self.centralwidget = QWidget(main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.image_show = QWidget()
        self.image_show.setObjectName(u"image_show")
        self.gridLayout_3 = QGridLayout(self.image_show)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.bt_previous = QPushButton(self.image_show)
        self.bt_previous.setObjectName(u"bt_previous")
        self.bt_previous.setMaximumSize(QSize(60, 60))
        font = QFont()
        font.setFamilies([u"Adobe \u9ed1\u4f53 Std R"])
        font.setPointSize(10)
        font.setBold(False)
        self.bt_previous.setFont(font)

        self.horizontalLayout_6.addWidget(self.bt_previous)

        self.lb_image_show_oringin = QLabel(self.image_show)
        self.lb_image_show_oringin.setObjectName(u"lb_image_show_oringin")
        self.lb_image_show_oringin.setMinimumSize(QSize(320, 320))
        self.lb_image_show_oringin.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_6.addWidget(self.lb_image_show_oringin)

        self.inf_4 = QLabel(self.image_show)
        self.inf_4.setObjectName(u"inf_4")
        self.inf_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.inf_4)

        self.lb_image_show_transformed = QLabel(self.image_show)
        self.lb_image_show_transformed.setObjectName(u"lb_image_show_transformed")
        self.lb_image_show_transformed.setMinimumSize(QSize(320, 320))
        self.lb_image_show_transformed.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_6.addWidget(self.lb_image_show_transformed)

        self.bt_next = QPushButton(self.image_show)
        self.bt_next.setObjectName(u"bt_next")
        self.bt_next.setMaximumSize(QSize(60, 60))
        font1 = QFont()
        font1.setFamilies([u"Adobe \u9ed1\u4f53 Std R"])
        font1.setPointSize(10)
        self.bt_next.setFont(font1)

        self.horizontalLayout_6.addWidget(self.bt_next)


        self.gridLayout_3.addLayout(self.horizontalLayout_6, 3, 1, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.bt_read_image_path = QPushButton(self.image_show)
        self.bt_read_image_path.setObjectName(u"bt_read_image_path")

        self.horizontalLayout_5.addWidget(self.bt_read_image_path)

        self.lb_image_path = QLabel(self.image_show)
        self.lb_image_path.setObjectName(u"lb_image_path")

        self.horizontalLayout_5.addWidget(self.lb_image_path)


        self.gridLayout_3.addLayout(self.horizontalLayout_5, 1, 1, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.inf_2 = QLabel(self.image_show)
        self.inf_2.setObjectName(u"inf_2")

        self.horizontalLayout_7.addWidget(self.inf_2)

        self.le_image_pixel_oringin = QLineEdit(self.image_show)
        self.le_image_pixel_oringin.setObjectName(u"le_image_pixel_oringin")

        self.horizontalLayout_7.addWidget(self.le_image_pixel_oringin)

        self.inf_3 = QLabel(self.image_show)
        self.inf_3.setObjectName(u"inf_3")

        self.horizontalLayout_7.addWidget(self.inf_3)

        self.le_image_pixel_saveas = QLineEdit(self.image_show)
        self.le_image_pixel_saveas.setObjectName(u"le_image_pixel_saveas")

        self.horizontalLayout_7.addWidget(self.le_image_pixel_saveas)


        self.gridLayout_3.addLayout(self.horizontalLayout_7, 2, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_4, 0, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 5, 1, 1, 1)

        self.bt_reflash_image = QPushButton(self.image_show)
        self.bt_reflash_image.setObjectName(u"bt_reflash_image")

        self.gridLayout_3.addWidget(self.bt_reflash_image, 4, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 3, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 3, 2, 1, 1)

        self.tabWidget.addTab(self.image_show, "")
        self.pixel_transform = QWidget()
        self.pixel_transform.setObjectName(u"pixel_transform")
        self.gridLayout_2 = QGridLayout(self.pixel_transform)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.inf_5 = QLabel(self.pixel_transform)
        self.inf_5.setObjectName(u"inf_5")

        self.horizontalLayout_4.addWidget(self.inf_5)

        self.le_pixel_oringin = QLineEdit(self.pixel_transform)
        self.le_pixel_oringin.setObjectName(u"le_pixel_oringin")

        self.horizontalLayout_4.addWidget(self.le_pixel_oringin)

        self.inf = QLabel(self.pixel_transform)
        self.inf.setObjectName(u"inf")

        self.horizontalLayout_4.addWidget(self.inf)

        self.le_pixel_saveas = QLineEdit(self.pixel_transform)
        self.le_pixel_saveas.setObjectName(u"le_pixel_saveas")

        self.horizontalLayout_4.addWidget(self.le_pixel_saveas)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 1, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.bt_read_folder_path = QPushButton(self.pixel_transform)
        self.bt_read_folder_path.setObjectName(u"bt_read_folder_path")

        self.horizontalLayout.addWidget(self.bt_read_folder_path)

        self.lb_read_folder_path = QLabel(self.pixel_transform)
        self.lb_read_folder_path.setObjectName(u"lb_read_folder_path")

        self.horizontalLayout.addWidget(self.lb_read_folder_path)


        self.gridLayout_2.addLayout(self.horizontalLayout, 3, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.bt_save_folder_path = QPushButton(self.pixel_transform)
        self.bt_save_folder_path.setObjectName(u"bt_save_folder_path")

        self.horizontalLayout_2.addWidget(self.bt_save_folder_path)

        self.lb_save_folder_path = QLabel(self.pixel_transform)
        self.lb_save_folder_path.setObjectName(u"lb_save_folder_path")

        self.horizontalLayout_2.addWidget(self.lb_save_folder_path)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 4, 1, 1, 1)

        self.pb_process = QProgressBar(self.pixel_transform)
        self.pb_process.setObjectName(u"pb_process")
        self.pb_process.setEnabled(True)
        self.pb_process.setValue(0)

        self.gridLayout_2.addWidget(self.pb_process, 5, 1, 1, 1)

        self.bt_start_process = QPushButton(self.pixel_transform)
        self.bt_start_process.setObjectName(u"bt_start_process")

        self.gridLayout_2.addWidget(self.bt_start_process, 6, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 7, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 3, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 3, 0, 1, 1)

        self.tabWidget.addTab(self.pixel_transform, "")
        self.datasets_split = QWidget()
        self.datasets_split.setObjectName(u"datasets_split")
        self.gridLayout_4 = QGridLayout(self.datasets_split)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_6, 4, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.inf_6 = QLabel(self.datasets_split)
        self.inf_6.setObjectName(u"inf_6")

        self.horizontalLayout_3.addWidget(self.inf_6)

        self.le_train_radio = QLineEdit(self.datasets_split)
        self.le_train_radio.setObjectName(u"le_train_radio")
        self.le_train_radio.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.le_train_radio)


        self.gridLayout_4.addLayout(self.horizontalLayout_3, 4, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_5, 4, 2, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.bt_save_folder_path_p3 = QPushButton(self.datasets_split)
        self.bt_save_folder_path_p3.setObjectName(u"bt_save_folder_path_p3")

        self.horizontalLayout_9.addWidget(self.bt_save_folder_path_p3)

        self.lb_save_folder_path_p3 = QLabel(self.datasets_split)
        self.lb_save_folder_path_p3.setObjectName(u"lb_save_folder_path_p3")

        self.horizontalLayout_9.addWidget(self.lb_save_folder_path_p3)


        self.gridLayout_4.addLayout(self.horizontalLayout_9, 3, 1, 1, 1)

        self.pb_process_p3 = QProgressBar(self.datasets_split)
        self.pb_process_p3.setObjectName(u"pb_process_p3")
        self.pb_process_p3.setValue(0)

        self.gridLayout_4.addWidget(self.pb_process_p3, 5, 1, 1, 1)

        self.bt_start_process_p3 = QPushButton(self.datasets_split)
        self.bt_start_process_p3.setObjectName(u"bt_start_process_p3")

        self.gridLayout_4.addWidget(self.bt_start_process_p3, 6, 1, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.bt_read_img_folder_path_p3 = QPushButton(self.datasets_split)
        self.bt_read_img_folder_path_p3.setObjectName(u"bt_read_img_folder_path_p3")

        self.horizontalLayout_8.addWidget(self.bt_read_img_folder_path_p3)

        self.lb_read_img_folder_path_p3 = QLabel(self.datasets_split)
        self.lb_read_img_folder_path_p3.setObjectName(u"lb_read_img_folder_path_p3")

        self.horizontalLayout_8.addWidget(self.lb_read_img_folder_path_p3)


        self.gridLayout_4.addLayout(self.horizontalLayout_8, 1, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_6, 0, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_5, 7, 1, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.bt_read_gt_folder_path_p3 = QPushButton(self.datasets_split)
        self.bt_read_gt_folder_path_p3.setObjectName(u"bt_read_gt_folder_path_p3")

        self.horizontalLayout_10.addWidget(self.bt_read_gt_folder_path_p3)

        self.lb_read_gt_folder_path_p3 = QLabel(self.datasets_split)
        self.lb_read_gt_folder_path_p3.setObjectName(u"lb_read_gt_folder_path_p3")

        self.horizontalLayout_10.addWidget(self.lb_read_gt_folder_path_p3)


        self.gridLayout_4.addLayout(self.horizontalLayout_10, 2, 1, 1, 1)

        self.tabWidget.addTab(self.datasets_split, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        main.setCentralWidget(self.centralwidget)

        self.retranslateUi(main)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(main)
    # setupUi

    def retranslateUi(self, main):
        main.setWindowTitle(QCoreApplication.translate("main", u"MainWindow", None))
        self.bt_previous.setText(QCoreApplication.translate("main", u"\u2190", None))
        self.lb_image_show_oringin.setText("")
        self.inf_4.setText(QCoreApplication.translate("main", u"\u2192", None))
        self.lb_image_show_transformed.setText("")
        self.bt_next.setText(QCoreApplication.translate("main", u"\u2192", None))
        self.bt_read_image_path.setText(QCoreApplication.translate("main", u"\u8bfb\u53d6\u56fe\u7247", None))
        self.lb_image_path.setText(QCoreApplication.translate("main", u"\u8bfb\u53d6\u56fe\u7247\u8def\u5f84", None))
        self.inf_2.setText(QCoreApplication.translate("main", u"\u7070\u5ea6\u56fe\u50cf\u7d20\u6620\u5c04", None))
        self.inf_3.setText(QCoreApplication.translate("main", u"\u2192", None))
        self.bt_reflash_image.setText(QCoreApplication.translate("main", u"\u5237\u65b0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.image_show), QCoreApplication.translate("main", u"\u56fe\u7247\u67e5\u770b", None))
        self.inf_5.setText(QCoreApplication.translate("main", u"\u50cf\u7d20\u6620\u5c04", None))
        self.inf.setText(QCoreApplication.translate("main", u"\u2192", None))
        self.bt_read_folder_path.setText(QCoreApplication.translate("main", u"\u8bfb\u53d6\u6587\u4ef6\u5939", None))
        self.lb_read_folder_path.setText(QCoreApplication.translate("main", u"\u8bfb\u53d6\u8def\u5f84", None))
        self.bt_save_folder_path.setText(QCoreApplication.translate("main", u"\u4fdd\u5b58\u6587\u4ef6\u5939", None))
        self.lb_save_folder_path.setText(QCoreApplication.translate("main", u"\u4fdd\u5b58\u8def\u5f84", None))
        self.bt_start_process.setText(QCoreApplication.translate("main", u"\u5f00\u59cb\u8f6c\u6362", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pixel_transform), QCoreApplication.translate("main", u"\u7070\u5ea6\u56fe\u50cf\u7d20\u66ff\u6362", None))
        self.inf_6.setText(QCoreApplication.translate("main", u"\u8bad\u7ec3\u96c6\u6bd4\u4f8b", None))
        self.le_train_radio.setInputMask("")
        self.le_train_radio.setText("")
        self.le_train_radio.setPlaceholderText(QCoreApplication.translate("main", u"example:0.8", None))
        self.bt_save_folder_path_p3.setText(QCoreApplication.translate("main", u"\u4fdd\u5b58\u6587\u4ef6\u5939", None))
        self.lb_save_folder_path_p3.setText(QCoreApplication.translate("main", u"\u4fdd\u5b58\u8def\u5f84", None))
        self.bt_start_process_p3.setText(QCoreApplication.translate("main", u"\u5f00\u59cb\u8f6c\u6362", None))
        self.bt_read_img_folder_path_p3.setText(QCoreApplication.translate("main", u"\u8bfb\u53d6\u56fe\u7247\u6587\u4ef6\u5939", None))
        self.lb_read_img_folder_path_p3.setText(QCoreApplication.translate("main", u"\u8bfb\u53d6\u8def\u5f84", None))
        self.bt_read_gt_folder_path_p3.setText(QCoreApplication.translate("main", u"\u8bfb\u53d6\u6807\u7b7e\u6587\u4ef6\u5939", None))
        self.lb_read_gt_folder_path_p3.setText(QCoreApplication.translate("main", u"\u8bfb\u53d6\u8def\u5f84", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.datasets_split), QCoreApplication.translate("main", u"\u6570\u636e\u96c6\u5212\u5206", None))
    # retranslateUi

