# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'simplino_widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 650)
        Form.setMinimumSize(QSize(800, 650))
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_main = QFrame(Form)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"/* LINE EDIT */\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"	border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
""
                        "	border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"	border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63"
                        ", 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* CHECKBOX */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
"}\n"
"\n"
"/* RADIO BUTTON */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius"
                        ": 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* COMBOBOX */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb("
                        "85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:verti"
                        "cal {\n"
"    background-color: rgb(85, 170, 255);\n"
"	border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 65))
        self.frame_top.setMaximumSize(QSize(16777215, 65))
        self.frame_top.setStyleSheet(u"background-color: transparent;")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.frame_top)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 16777215))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_3.addWidget(self.frame_toggle)

        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setStyleSheet(u"background: transparent;")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top_btns = QFrame(self.frame_top_right)
        self.frame_top_btns.setObjectName(u"frame_top_btns")
        self.frame_top_btns.setMaximumSize(QSize(16777215, 42))
        self.frame_top_btns.setStyleSheet(u"background-color: rgba(27, 29, 35, 200)")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy)
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.frame_icon_top_bar = QFrame(self.frame_label_top_btns)
        self.frame_icon_top_bar.setObjectName(u"frame_icon_top_bar")
        self.frame_icon_top_bar.setMaximumSize(QSize(30, 30))
        self.frame_icon_top_bar.setStyleSheet(u"background: transparent;\n"
"background-image: url(:/16x16/icons/16x16/cil-terminal.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"")
        self.frame_icon_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_icon_top_bar.setFrameShadow(QFrame.Raised)
        self.frame_icon_top_bar_2 = QFrame(self.frame_icon_top_bar)
        self.frame_icon_top_bar_2.setObjectName(u"frame_icon_top_bar_2")
        self.frame_icon_top_bar_2.setGeometry(QRect(0, 0, 30, 30))
        self.frame_icon_top_bar_2.setMaximumSize(QSize(30, 30))
        self.frame_icon_top_bar_2.setStyleSheet(u"background: transparent;\n"
"background-image: url(:/16x16/icons/16x16/cil-terminal.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"")
        self.frame_icon_top_bar_2.setFrameShape(QFrame.StyledPanel)
        self.frame_icon_top_bar_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_icon_top_bar)

        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_title_bar_top.setFont(font)
        self.label_title_bar_top.setStyleSheet(u"background: transparent;\n"
"")

        self.horizontalLayout_10.addWidget(self.label_title_bar_top)


        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)

        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        sizePolicy.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy)
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy1)
        self.btn_minimize.setMinimumSize(QSize(40, 0))
        self.btn_minimize.setMaximumSize(QSize(40, 16777215))
        self.btn_minimize.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.btn_minimize)

        self.btn_maximize_restore = QPushButton(self.frame_btns_right)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        sizePolicy1.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy1)
        self.btn_maximize_restore.setMinimumSize(QSize(40, 0))
        self.btn_maximize_restore.setMaximumSize(QSize(40, 16777215))
        self.btn_maximize_restore.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize_restore.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.btn_maximize_restore)

        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy1.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy1)
        self.btn_close.setMinimumSize(QSize(40, 0))
        self.btn_close.setMaximumSize(QSize(40, 16777215))
        self.btn_close.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.btn_close)


        self.horizontalLayout_4.addWidget(self.frame_btns_right, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_top_btns)

        self.frame_top_info = QFrame(self.frame_top_right)
        self.frame_top_info.setObjectName(u"frame_top_info")
        self.frame_top_info.setMaximumSize(QSize(16777215, 65))
        self.frame_top_info.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_top_info.setFrameShape(QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.label_top_info_1 = QLabel(self.frame_top_info)
        self.label_top_info_1.setObjectName(u"label_top_info_1")
        self.label_top_info_1.setMinimumSize(QSize(100, 0))
        self.label_top_info_1.setMaximumSize(QSize(16777215, 15))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        self.label_top_info_1.setFont(font1)
        self.label_top_info_1.setStyleSheet(u"color: rgb(98, 103, 111); ")

        self.horizontalLayout_8.addWidget(self.label_top_info_1)

        self.label_top_info_2 = QLabel(self.frame_top_info)
        self.label_top_info_2.setObjectName(u"label_top_info_2")
        self.label_top_info_2.setMinimumSize(QSize(0, 0))
        self.label_top_info_2.setMaximumSize(QSize(250, 20))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setBold(True)
        font2.setWeight(75)
        self.label_top_info_2.setFont(font2)
        self.label_top_info_2.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_top_info_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_top_info_2)


        self.verticalLayout_2.addWidget(self.frame_top_info)


        self.horizontalLayout_3.addWidget(self.frame_top_right)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy2)
        self.frame_center.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.frame_center)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy3)
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_menus = QFrame(self.frame_left_menu)
        self.frame_menus.setObjectName(u"frame_menus")
        self.frame_menus.setFrameShape(QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QFrame.Raised)
        self.layout_menus = QVBoxLayout(self.frame_menus)
        self.layout_menus.setSpacing(0)
        self.layout_menus.setObjectName(u"layout_menus")
        self.layout_menus.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_menus, 0, Qt.AlignTop)

        self.frame_extra_menus = QFrame(self.frame_left_menu)
        self.frame_extra_menus.setObjectName(u"frame_extra_menus")
        sizePolicy3.setHeightForWidth(self.frame_extra_menus.sizePolicy().hasHeightForWidth())
        self.frame_extra_menus.setSizePolicy(sizePolicy3)
        self.frame_extra_menus.setFrameShape(QFrame.NoFrame)
        self.frame_extra_menus.setFrameShadow(QFrame.Raised)
        self.layout_menu_bottom = QVBoxLayout(self.frame_extra_menus)
        self.layout_menu_bottom.setSpacing(10)
        self.layout_menu_bottom.setObjectName(u"layout_menu_bottom")
        self.layout_menu_bottom.setContentsMargins(0, 0, 0, 25)

        self.verticalLayout_5.addWidget(self.frame_extra_menus, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_content_right = QFrame(self.frame_center)
        self.frame_content_right.setObjectName(u"frame_content_right")
        self.frame_content_right.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.frame_content_right.setFrameShape(QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_content_right)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_content = QFrame(self.frame_content_right)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_content)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_10 = QVBoxLayout(self.page_home)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_6 = QLabel(self.page_home)
        self.label_6.setObjectName(u"label_6")
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(28)
        self.label_6.setFont(font3)
        self.label_6.setStyleSheet(u"")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_6)

        self.label = QLabel(self.page_home)
        self.label.setObjectName(u"label")
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(20)
        self.label.setFont(font4)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label)

        self.stackedWidget.addWidget(self.page_home)
        self.page_virtual_agent = QWidget()
        self.page_virtual_agent.setObjectName(u"page_virtual_agent")
        self.page_virtual_agent.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_12 = QVBoxLayout(self.page_virtual_agent)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.calculate_button = QPushButton(self.page_virtual_agent)
        self.calculate_button.setObjectName(u"calculate_button")

        self.gridLayout_3.addWidget(self.calculate_button, 5, 0, 1, 1)

        self.start_price_text_input = QLineEdit(self.page_virtual_agent)
        self.start_price_text_input.setObjectName(u"start_price_text_input")

        self.gridLayout_3.addWidget(self.start_price_text_input, 1, 1, 1, 1)

        self.nb_buy_text_input = QLineEdit(self.page_virtual_agent)
        self.nb_buy_text_input.setObjectName(u"nb_buy_text_input")

        self.gridLayout_3.addWidget(self.nb_buy_text_input, 2, 1, 1, 1)

        self.label_2 = QLabel(self.page_virtual_agent)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_3 = QLabel(self.page_virtual_agent)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_5 = QLabel(self.page_virtual_agent)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 2, 2, 1, 1)

        self.pair_comboBox = QComboBox(self.page_virtual_agent)
        self.pair_comboBox.setObjectName(u"pair_comboBox")

        self.gridLayout_3.addWidget(self.pair_comboBox, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 3, 6, 1)

        self.label_4 = QLabel(self.page_virtual_agent)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 3, 0, 1, 1)

        self.drop_poucent_text_input = QLineEdit(self.page_virtual_agent)
        self.drop_poucent_text_input.setObjectName(u"drop_poucent_text_input")

        self.gridLayout_3.addWidget(self.drop_poucent_text_input, 3, 1, 1, 1)

        self.label_7 = QLabel(self.page_virtual_agent)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)

        self.label_27 = QLabel(self.page_virtual_agent)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_3.addWidget(self.label_27, 4, 0, 1, 1)

        self.percent_more_buy_label = QLineEdit(self.page_virtual_agent)
        self.percent_more_buy_label.setObjectName(u"percent_more_buy_label")

        self.gridLayout_3.addWidget(self.percent_more_buy_label, 4, 1, 1, 1)


        self.verticalLayout_12.addLayout(self.gridLayout_3)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.Buy_asset_label = QLabel(self.page_virtual_agent)
        self.Buy_asset_label.setObjectName(u"Buy_asset_label")

        self.gridLayout_4.addWidget(self.Buy_asset_label, 3, 2, 1, 1)

        self.stop_button = QPushButton(self.page_virtual_agent)
        self.stop_button.setObjectName(u"stop_button")

        self.gridLayout_4.addWidget(self.stop_button, 6, 1, 1, 1)

        self.label_10 = QLabel(self.page_virtual_agent)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_4.addWidget(self.label_10, 5, 0, 1, 1)

        self.Possible_sell = QLabel(self.page_virtual_agent)
        self.Possible_sell.setObjectName(u"Possible_sell")

        self.gridLayout_4.addWidget(self.Possible_sell, 5, 1, 1, 1)

        self.Pairing_label = QLabel(self.page_virtual_agent)
        self.Pairing_label.setObjectName(u"Pairing_label")

        self.gridLayout_4.addWidget(self.Pairing_label, 0, 1, 1, 1)

        self.Sell_order_filled_label = QLabel(self.page_virtual_agent)
        self.Sell_order_filled_label.setObjectName(u"Sell_order_filled_label")

        self.gridLayout_4.addWidget(self.Sell_order_filled_label, 2, 1, 1, 1)

        self.Buy_Qty_label = QLabel(self.page_virtual_agent)
        self.Buy_Qty_label.setObjectName(u"Buy_Qty_label")

        self.gridLayout_4.addWidget(self.Buy_Qty_label, 3, 1, 1, 1)

        self.start_button = QPushButton(self.page_virtual_agent)
        self.start_button.setObjectName(u"start_button")

        self.gridLayout_4.addWidget(self.start_button, 6, 0, 1, 1)

        self.label_9 = QLabel(self.page_virtual_agent)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_4.addWidget(self.label_9, 0, 0, 1, 1)

        self.label_11 = QLabel(self.page_virtual_agent)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_4.addWidget(self.label_11, 3, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 0, 3, 7, 1)

        self.label_15 = QLabel(self.page_virtual_agent)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_4.addWidget(self.label_15, 2, 0, 1, 1)

        self.Buy_order_filled_label = QLabel(self.page_virtual_agent)
        self.Buy_order_filled_label.setObjectName(u"Buy_order_filled_label")

        self.gridLayout_4.addWidget(self.Buy_order_filled_label, 1, 1, 1, 1)

        self.label_12 = QLabel(self.page_virtual_agent)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_4.addWidget(self.label_12, 1, 0, 1, 1)

        self.label_26 = QLabel(self.page_virtual_agent)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_4.addWidget(self.label_26, 4, 0, 1, 1)

        self.invested_label = QLabel(self.page_virtual_agent)
        self.invested_label.setObjectName(u"invested_label")

        self.gridLayout_4.addWidget(self.invested_label, 4, 1, 1, 1)

        self.sell_asset_label_2 = QLabel(self.page_virtual_agent)
        self.sell_asset_label_2.setObjectName(u"sell_asset_label_2")

        self.gridLayout_4.addWidget(self.sell_asset_label_2, 4, 2, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.sell_asset_label = QLabel(self.page_virtual_agent)
        self.sell_asset_label.setObjectName(u"sell_asset_label")

        self.gridLayout_5.addWidget(self.sell_asset_label, 4, 2, 1, 1)

        self.start_price_label = QLabel(self.page_virtual_agent)
        self.start_price_label.setObjectName(u"start_price_label")

        self.gridLayout_5.addWidget(self.start_price_label, 0, 1, 1, 1)

        self.price_pairing_label_2 = QLabel(self.page_virtual_agent)
        self.price_pairing_label_2.setObjectName(u"price_pairing_label_2")

        self.gridLayout_5.addWidget(self.price_pairing_label_2, 2, 2, 1, 1)

        self.label_19 = QLabel(self.page_virtual_agent)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_5.addWidget(self.label_19, 5, 0, 1, 1)

        self.label_13 = QLabel(self.page_virtual_agent)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_5.addWidget(self.label_13, 1, 0, 1, 1)

        self.bid_price_label = QLabel(self.page_virtual_agent)
        self.bid_price_label.setObjectName(u"bid_price_label")

        self.gridLayout_5.addWidget(self.bid_price_label, 3, 1, 1, 1)

        self.gain_label = QLabel(self.page_virtual_agent)
        self.gain_label.setObjectName(u"gain_label")

        self.gridLayout_5.addWidget(self.gain_label, 4, 1, 1, 1)

        self.price_pairing_label_3 = QLabel(self.page_virtual_agent)
        self.price_pairing_label_3.setObjectName(u"price_pairing_label_3")

        self.gridLayout_5.addWidget(self.price_pairing_label_3, 3, 2, 1, 1)

        self.label_17 = QLabel(self.page_virtual_agent)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_5.addWidget(self.label_17, 3, 0, 1, 1)

        self.label_14 = QLabel(self.page_virtual_agent)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_5.addWidget(self.label_14, 0, 0, 1, 1)

        self.label_18 = QLabel(self.page_virtual_agent)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_5.addWidget(self.label_18, 4, 0, 1, 1)

        self.label_16 = QLabel(self.page_virtual_agent)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_5.addWidget(self.label_16, 2, 0, 1, 1)

        self.price_label = QLabel(self.page_virtual_agent)
        self.price_label.setObjectName(u"price_label")

        self.gridLayout_5.addWidget(self.price_label, 1, 1, 1, 1)

        self.ask_price_label = QLabel(self.page_virtual_agent)
        self.ask_price_label.setObjectName(u"ask_price_label")

        self.gridLayout_5.addWidget(self.ask_price_label, 2, 1, 1, 1)

        self.price_pairing_label = QLabel(self.page_virtual_agent)
        self.price_pairing_label.setObjectName(u"price_pairing_label")

        self.gridLayout_5.addWidget(self.price_pairing_label, 1, 2, 1, 1)

        self.price_pairing_label_4 = QLabel(self.page_virtual_agent)
        self.price_pairing_label_4.setObjectName(u"price_pairing_label_4")

        self.gridLayout_5.addWidget(self.price_pairing_label_4, 0, 2, 1, 1)

        self.start_time_label = QLabel(self.page_virtual_agent)
        self.start_time_label.setObjectName(u"start_time_label")

        self.gridLayout_5.addWidget(self.start_time_label, 5, 1, 1, 3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_3, 0, 3, 5, 1)


        self.gridLayout_4.addLayout(self.gridLayout_5, 0, 4, 7, 1)


        self.verticalLayout_12.addLayout(self.gridLayout_4)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.sell_filled_Qty_label = QLabel(self.page_virtual_agent)
        self.sell_filled_Qty_label.setObjectName(u"sell_filled_Qty_label")

        self.gridLayout_6.addWidget(self.sell_filled_Qty_label, 2, 6, 1, 1)

        self.buy_qty_label = QLabel(self.page_virtual_agent)
        self.buy_qty_label.setObjectName(u"buy_qty_label")

        self.gridLayout_6.addWidget(self.buy_qty_label, 1, 3, 1, 1)

        self.Buy_asset_label_3 = QLabel(self.page_virtual_agent)
        self.Buy_asset_label_3.setObjectName(u"Buy_asset_label_3")

        self.gridLayout_6.addWidget(self.Buy_asset_label_3, 2, 4, 1, 1)

        self.label_24 = QLabel(self.page_virtual_agent)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_6.addWidget(self.label_24, 2, 2, 1, 1)

        self.Buy_asset_label_5 = QLabel(self.page_virtual_agent)
        self.Buy_asset_label_5.setObjectName(u"Buy_asset_label_5")

        self.gridLayout_6.addWidget(self.Buy_asset_label_5, 2, 7, 1, 1)

        self.label_25 = QLabel(self.page_virtual_agent)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_6.addWidget(self.label_25, 2, 5, 1, 1)

        self.buy_filled_Qty_label = QLabel(self.page_virtual_agent)
        self.buy_filled_Qty_label.setObjectName(u"buy_filled_Qty_label")

        self.gridLayout_6.addWidget(self.buy_filled_Qty_label, 1, 6, 1, 1)

        self.label_20 = QLabel(self.page_virtual_agent)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_6.addWidget(self.label_20, 1, 0, 1, 1)

        self.Buy_order_ID_label = QLabel(self.page_virtual_agent)
        self.Buy_order_ID_label.setObjectName(u"Buy_order_ID_label")

        self.gridLayout_6.addWidget(self.Buy_order_ID_label, 1, 1, 1, 1)

        self.Buy_asset_label_2 = QLabel(self.page_virtual_agent)
        self.Buy_asset_label_2.setObjectName(u"Buy_asset_label_2")

        self.gridLayout_6.addWidget(self.Buy_asset_label_2, 1, 4, 1, 1)

        self.Buy_asset_label_4 = QLabel(self.page_virtual_agent)
        self.Buy_asset_label_4.setObjectName(u"Buy_asset_label_4")

        self.gridLayout_6.addWidget(self.Buy_asset_label_4, 1, 7, 1, 1)

        self.label_21 = QLabel(self.page_virtual_agent)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_6.addWidget(self.label_21, 2, 0, 1, 1)

        self.label_22 = QLabel(self.page_virtual_agent)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_6.addWidget(self.label_22, 1, 2, 1, 1)

        self.sell_qty_label = QLabel(self.page_virtual_agent)
        self.sell_qty_label.setObjectName(u"sell_qty_label")

        self.gridLayout_6.addWidget(self.sell_qty_label, 2, 3, 1, 1)

        self.label_23 = QLabel(self.page_virtual_agent)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_6.addWidget(self.label_23, 1, 5, 1, 1)

        self.Sell_order_ID_label = QLabel(self.page_virtual_agent)
        self.Sell_order_ID_label.setObjectName(u"Sell_order_ID_label")

        self.gridLayout_6.addWidget(self.Sell_order_ID_label, 2, 1, 1, 1)

        self.label_28 = QLabel(self.page_virtual_agent)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_6.addWidget(self.label_28, 0, 0, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_6, 0, 8, 3, 1)


        self.verticalLayout_12.addLayout(self.gridLayout_6)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_30 = QLabel(self.page_virtual_agent)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_7.addWidget(self.label_30, 0, 0, 1, 1)

        self.Simplino_calcul_table = QTableWidget(self.page_virtual_agent)
        if (self.Simplino_calcul_table.columnCount() < 4):
            self.Simplino_calcul_table.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.Simplino_calcul_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.Simplino_calcul_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.Simplino_calcul_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.Simplino_calcul_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.Simplino_calcul_table.rowCount() < 16):
            self.Simplino_calcul_table.setRowCount(16)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font1);
        self.Simplino_calcul_table.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.Simplino_calcul_table.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.Simplino_calcul_table.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.Simplino_calcul_table.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.Simplino_calcul_table.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.Simplino_calcul_table.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.Simplino_calcul_table.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.Simplino_calcul_table.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.Simplino_calcul_table.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.Simplino_calcul_table.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.Simplino_calcul_table.setVerticalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.Simplino_calcul_table.setVerticalHeaderItem(11, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.Simplino_calcul_table.setVerticalHeaderItem(12, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.Simplino_calcul_table.setVerticalHeaderItem(13, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.Simplino_calcul_table.setVerticalHeaderItem(14, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.Simplino_calcul_table.setVerticalHeaderItem(15, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.Simplino_calcul_table.setItem(0, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.Simplino_calcul_table.setItem(0, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.Simplino_calcul_table.setItem(0, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.Simplino_calcul_table.setItem(0, 3, __qtablewidgetitem23)
        self.Simplino_calcul_table.setObjectName(u"Simplino_calcul_table")
        sizePolicy2.setHeightForWidth(self.Simplino_calcul_table.sizePolicy().hasHeightForWidth())
        self.Simplino_calcul_table.setSizePolicy(sizePolicy2)
        palette = QPalette()
        brush = QBrush(QColor(210, 210, 210, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(39, 44, 54, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.Simplino_calcul_table.setPalette(palette)
        self.Simplino_calcul_table.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.Simplino_calcul_table.setFrameShape(QFrame.NoFrame)
        self.Simplino_calcul_table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.Simplino_calcul_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.Simplino_calcul_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Simplino_calcul_table.setAlternatingRowColors(False)
        self.Simplino_calcul_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.Simplino_calcul_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.Simplino_calcul_table.setShowGrid(True)
        self.Simplino_calcul_table.setGridStyle(Qt.SolidLine)
        self.Simplino_calcul_table.setSortingEnabled(False)
        self.Simplino_calcul_table.horizontalHeader().setVisible(False)
        self.Simplino_calcul_table.horizontalHeader().setCascadingSectionResizes(True)
        self.Simplino_calcul_table.horizontalHeader().setDefaultSectionSize(200)
        self.Simplino_calcul_table.horizontalHeader().setStretchLastSection(True)
        self.Simplino_calcul_table.verticalHeader().setVisible(False)
        self.Simplino_calcul_table.verticalHeader().setCascadingSectionResizes(False)
        self.Simplino_calcul_table.verticalHeader().setHighlightSections(False)
        self.Simplino_calcul_table.verticalHeader().setStretchLastSection(True)

        self.gridLayout_7.addWidget(self.Simplino_calcul_table, 1, 0, 1, 1)

        self.label_29 = QLabel(self.page_virtual_agent)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_7.addWidget(self.label_29, 0, 1, 1, 1)

        self.Order_filled_tab = QTableWidget(self.page_virtual_agent)
        if (self.Order_filled_tab.columnCount() < 4):
            self.Order_filled_tab.setColumnCount(4)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.Order_filled_tab.setHorizontalHeaderItem(0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.Order_filled_tab.setHorizontalHeaderItem(1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.Order_filled_tab.setHorizontalHeaderItem(2, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.Order_filled_tab.setHorizontalHeaderItem(3, __qtablewidgetitem27)
        if (self.Order_filled_tab.rowCount() < 16):
            self.Order_filled_tab.setRowCount(16)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setFont(font1);
        self.Order_filled_tab.setVerticalHeaderItem(0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.Order_filled_tab.setVerticalHeaderItem(1, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.Order_filled_tab.setVerticalHeaderItem(2, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.Order_filled_tab.setVerticalHeaderItem(3, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.Order_filled_tab.setVerticalHeaderItem(4, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.Order_filled_tab.setVerticalHeaderItem(5, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.Order_filled_tab.setVerticalHeaderItem(6, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.Order_filled_tab.setVerticalHeaderItem(7, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.Order_filled_tab.setVerticalHeaderItem(8, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.Order_filled_tab.setVerticalHeaderItem(9, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.Order_filled_tab.setVerticalHeaderItem(10, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.Order_filled_tab.setVerticalHeaderItem(11, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.Order_filled_tab.setVerticalHeaderItem(12, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.Order_filled_tab.setVerticalHeaderItem(13, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.Order_filled_tab.setVerticalHeaderItem(14, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.Order_filled_tab.setVerticalHeaderItem(15, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.Order_filled_tab.setItem(0, 0, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.Order_filled_tab.setItem(0, 1, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.Order_filled_tab.setItem(0, 2, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.Order_filled_tab.setItem(0, 3, __qtablewidgetitem47)
        self.Order_filled_tab.setObjectName(u"Order_filled_tab")
        sizePolicy2.setHeightForWidth(self.Order_filled_tab.sizePolicy().hasHeightForWidth())
        self.Order_filled_tab.setSizePolicy(sizePolicy2)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.Order_filled_tab.setPalette(palette1)
        self.Order_filled_tab.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.Order_filled_tab.setFrameShape(QFrame.NoFrame)
        self.Order_filled_tab.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.Order_filled_tab.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.Order_filled_tab.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Order_filled_tab.setAlternatingRowColors(False)
        self.Order_filled_tab.setSelectionMode(QAbstractItemView.SingleSelection)
        self.Order_filled_tab.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.Order_filled_tab.setShowGrid(True)
        self.Order_filled_tab.setGridStyle(Qt.SolidLine)
        self.Order_filled_tab.setSortingEnabled(False)
        self.Order_filled_tab.horizontalHeader().setVisible(False)
        self.Order_filled_tab.horizontalHeader().setCascadingSectionResizes(True)
        self.Order_filled_tab.horizontalHeader().setDefaultSectionSize(200)
        self.Order_filled_tab.horizontalHeader().setStretchLastSection(True)
        self.Order_filled_tab.verticalHeader().setVisible(False)
        self.Order_filled_tab.verticalHeader().setCascadingSectionResizes(False)
        self.Order_filled_tab.verticalHeader().setHighlightSections(False)
        self.Order_filled_tab.verticalHeader().setStretchLastSection(True)

        self.gridLayout_7.addWidget(self.Order_filled_tab, 1, 1, 1, 1)


        self.verticalLayout_12.addLayout(self.gridLayout_7)

        self.stackedWidget.addWidget(self.page_virtual_agent)
        self.page_history = QWidget()
        self.page_history.setObjectName(u"page_history")
        self.table_history = QTableWidget(self.page_history)
        if (self.table_history.columnCount() < 4):
            self.table_history.setColumnCount(4)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.table_history.setHorizontalHeaderItem(0, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.table_history.setHorizontalHeaderItem(1, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.table_history.setHorizontalHeaderItem(2, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.table_history.setHorizontalHeaderItem(3, __qtablewidgetitem51)
        if (self.table_history.rowCount() < 16):
            self.table_history.setRowCount(16)
        __qtablewidgetitem52 = QTableWidgetItem()
        __qtablewidgetitem52.setFont(font1);
        self.table_history.setVerticalHeaderItem(0, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.table_history.setVerticalHeaderItem(1, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.table_history.setVerticalHeaderItem(2, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.table_history.setVerticalHeaderItem(3, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.table_history.setVerticalHeaderItem(4, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.table_history.setVerticalHeaderItem(5, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.table_history.setVerticalHeaderItem(6, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.table_history.setVerticalHeaderItem(7, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.table_history.setVerticalHeaderItem(8, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.table_history.setVerticalHeaderItem(9, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.table_history.setVerticalHeaderItem(10, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.table_history.setVerticalHeaderItem(11, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.table_history.setVerticalHeaderItem(12, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.table_history.setVerticalHeaderItem(13, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.table_history.setVerticalHeaderItem(14, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.table_history.setVerticalHeaderItem(15, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.table_history.setItem(0, 0, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.table_history.setItem(0, 1, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.table_history.setItem(0, 2, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.table_history.setItem(0, 3, __qtablewidgetitem71)
        self.table_history.setObjectName(u"table_history")
        self.table_history.setGeometry(QRect(0, 280, 1006, 419))
        sizePolicy2.setHeightForWidth(self.table_history.sizePolicy().hasHeightForWidth())
        self.table_history.setSizePolicy(sizePolicy2)
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.table_history.setPalette(palette2)
        self.table_history.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.table_history.setFrameShape(QFrame.NoFrame)
        self.table_history.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.table_history.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table_history.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_history.setAlternatingRowColors(False)
        self.table_history.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_history.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_history.setShowGrid(True)
        self.table_history.setGridStyle(Qt.SolidLine)
        self.table_history.setSortingEnabled(False)
        self.table_history.horizontalHeader().setVisible(False)
        self.table_history.horizontalHeader().setCascadingSectionResizes(True)
        self.table_history.horizontalHeader().setDefaultSectionSize(200)
        self.table_history.horizontalHeader().setStretchLastSection(True)
        self.table_history.verticalHeader().setVisible(False)
        self.table_history.verticalHeader().setCascadingSectionResizes(False)
        self.table_history.verticalHeader().setHighlightSections(False)
        self.table_history.verticalHeader().setStretchLastSection(True)
        self.btn_import_history = QPushButton(self.page_history)
        self.btn_import_history.setObjectName(u"btn_import_history")
        self.btn_import_history.setGeometry(QRect(40, 70, 150, 30))
        self.btn_import_history.setMinimumSize(QSize(150, 30))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(9)
        self.btn_import_history.setFont(font5)
        self.btn_import_history.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/16x16/icons/16x16/cil-reload.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_import_history.setIcon(icon3)
        self.stackedWidget.addWidget(self.page_history)
        self.page_wallet = QWidget()
        self.page_wallet.setObjectName(u"page_wallet")
        self.frame_icon_top_bar_3 = QFrame(self.page_wallet)
        self.frame_icon_top_bar_3.setObjectName(u"frame_icon_top_bar_3")
        self.frame_icon_top_bar_3.setGeometry(QRect(630, 290, 30, 30))
        self.frame_icon_top_bar_3.setMaximumSize(QSize(30, 30))
        self.frame_icon_top_bar_3.setStyleSheet(u"background: transparent;\n"
"background-image: url(:/16x16/icons/16x16/ceat;\n"
"")
        self.frame_icon_top_bar_3.setFrameShape(QFrame.StyledPanel)
        self.frame_icon_top_bar_3.setFrameShadow(QFrame.Raised)
        self.table_wallet = QTableWidget(self.page_wallet)
        self.table_wallet.setObjectName(u"table_wallet")
        self.table_wallet.setGeometry(QRect(10, 90, 1151, 451))
        sizePolicy2.setHeightForWidth(self.table_wallet.sizePolicy().hasHeightForWidth())
        self.table_wallet.setSizePolicy(sizePolicy2)
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.table_wallet.setPalette(palette3)
        self.table_wallet.setAutoFillBackground(True)
        self.table_wallet.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.table_wallet.setFrameShape(QFrame.NoFrame)
        self.table_wallet.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.table_wallet.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table_wallet.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_wallet.setAlternatingRowColors(False)
        self.table_wallet.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_wallet.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_wallet.setShowGrid(True)
        self.table_wallet.setGridStyle(Qt.SolidLine)
        self.table_wallet.setSortingEnabled(False)
        self.table_wallet.horizontalHeader().setVisible(False)
        self.table_wallet.horizontalHeader().setCascadingSectionResizes(True)
        self.table_wallet.horizontalHeader().setDefaultSectionSize(200)
        self.table_wallet.horizontalHeader().setStretchLastSection(True)
        self.table_wallet.verticalHeader().setVisible(False)
        self.table_wallet.verticalHeader().setCascadingSectionResizes(False)
        self.table_wallet.verticalHeader().setHighlightSections(False)
        self.table_wallet.verticalHeader().setStretchLastSection(True)
        self.btn_wallet_refresh = QPushButton(self.page_wallet)
        self.btn_wallet_refresh.setObjectName(u"btn_wallet_refresh")
        self.btn_wallet_refresh.setGeometry(QRect(20, 20, 150, 30))
        self.btn_wallet_refresh.setMinimumSize(QSize(150, 30))
        self.btn_wallet_refresh.setFont(font5)
        self.btn_wallet_refresh.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.btn_wallet_refresh.setIcon(icon3)
        self.stackedWidget.addWidget(self.page_wallet)
        self.page_trade = QWidget()
        self.page_trade.setObjectName(u"page_trade")
        self.label_8 = QLabel(self.page_trade)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(0, 30, 882, 288))
        self.label_8.setFont(font3)
        self.label_8.setStyleSheet(u"")
        self.label_8.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_trade)
        self.page_widgets = QWidget()
        self.page_widgets.setObjectName(u"page_widgets")
        self.verticalLayout_6 = QVBoxLayout(self.page_widgets)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame = QFrame(self.page_widgets)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border-radius: 5px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.frame)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_8.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_7.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit = QLineEdit(self.frame_content_wid_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.frame_content_wid_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        self.pushButton.setFont(font5)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/16x16/icons/16x16/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon4)

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_7.addWidget(self.frame_content_wid_1)


        self.verticalLayout_15.addWidget(self.frame_div_content_1)


        self.verticalLayout_6.addWidget(self.frame)

        self.frame_2 = QFrame(self.page_widgets)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 150))
        self.frame_2.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox = QCheckBox(self.frame_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)

        self.radioButton = QRadioButton(self.frame_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.radioButton, 0, 1, 1, 1)

        self.verticalSlider = QSlider(self.frame_2)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setStyleSheet(u"")
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalSlider, 0, 2, 3, 1)

        self.verticalScrollBar = QScrollBar(self.frame_2)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalScrollBar, 0, 4, 3, 1)

        self.scrollArea = QScrollArea(self.frame_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollArea {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 218, 218))
        self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(200, 200))
        self.plainTextEdit.setStyleSheet(u"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"}\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.horizontalLayout_11.addWidget(self.plainTextEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 5, 3, 1)

        self.comboBox = QComboBox(self.frame_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font5)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setFrame(True)

        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 2)

        self.horizontalScrollBar = QScrollBar(self.frame_2)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy4)
        self.horizontalScrollBar.setStyleSheet(u"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"")
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalScrollBar, 1, 3, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.frame_2)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setStyleSheet(u"QCommandLinkButton {	\n"
"	color: rgb(85, 170, 255);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(210, 210, 210);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(210, 210, 210);\n"
"	background-color: rgb(52, 58, 71);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/16x16/icons/16x16/cil-link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton.setIcon(icon5)

        self.gridLayout_2.addWidget(self.commandLinkButton, 1, 6, 1, 1)

        self.horizontalSlider = QSlider(self.frame_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider, 2, 0, 1, 2)


        self.verticalLayout_11.addLayout(self.gridLayout_2)


        self.verticalLayout_6.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.page_widgets)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 150))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.frame_3)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem72 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem75)
        if (self.tableWidget.rowCount() < 16):
            self.tableWidget.setRowCount(16)
        __qtablewidgetitem76 = QTableWidgetItem()
        __qtablewidgetitem76.setFont(font1);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem85)
        __qtablewidgetitem86 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem88)
        __qtablewidgetitem89 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem89)
        __qtablewidgetitem90 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem90)
        __qtablewidgetitem91 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem92)
        __qtablewidgetitem93 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem93)
        __qtablewidgetitem94 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem94)
        __qtablewidgetitem95 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem95)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy2.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy2)
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.tableWidget.setPalette(palette4)
        self.tableWidget.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_12.addWidget(self.tableWidget)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.page_widgets)

        self.verticalLayout_9.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.frame_content)

        self.frame_grip = QFrame(self.frame_content_right)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(0, 25))
        self.frame_grip.setMaximumSize(QSize(16777215, 25))
        self.frame_grip.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.frame_label_bottom = QFrame(self.frame_grip)
        self.frame_label_bottom.setObjectName(u"frame_label_bottom")
        self.frame_label_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.label_credits = QLabel(self.frame_label_bottom)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setFont(font1)
        self.label_credits.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.horizontalLayout_7.addWidget(self.label_credits)

        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setMaximumSize(QSize(100, 16777215))
        self.label_version.setFont(font1)
        self.label_version.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_version)


        self.horizontalLayout_6.addWidget(self.frame_label_bottom)

        self.frame_size_grip = QFrame(self.frame_grip)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMaximumSize(QSize(20, 20))
        self.frame_size_grip.setStyleSheet(u"QSizeGrip {\n"
"	background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_size_grip)


        self.verticalLayout_4.addWidget(self.frame_grip)


        self.horizontalLayout_2.addWidget(self.frame_content_right)


        self.verticalLayout.addWidget(self.frame_center)


        self.horizontalLayout.addWidget(self.frame_main)


        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_title_bar_top.setText(QCoreApplication.translate("Form", u"Simplino", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("Form", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize_restore.setToolTip(QCoreApplication.translate("Form", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize_restore.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("Form", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label_top_info_1.setText(QCoreApplication.translate("Form", u"C:\\Program Files\\Blender Foundation\\Blender 2.82", None))
        self.label_top_info_2.setText(QCoreApplication.translate("Form", u"| HOME", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Binance Bot - Cryptocurrency Exchange", None))
        self.label.setText(QCoreApplication.translate("Form", u"Version v0.0.1", None))
        self.calculate_button.setText(QCoreApplication.translate("Form", u"Calculate", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"start price", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"nb buy", None))
        self.label_5.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"% drop", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Available pairs", None))
        self.label_27.setText(QCoreApplication.translate("Form", u"% More buy", None))
        self.Buy_asset_label.setText(QCoreApplication.translate("Form", u"-", None))
        self.stop_button.setText(QCoreApplication.translate("Form", u"Stop", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Possible sells", None))
        self.Possible_sell.setText(QCoreApplication.translate("Form", u"0", None))
        self.Pairing_label.setText(QCoreApplication.translate("Form", u"-", None))
        self.Sell_order_filled_label.setText(QCoreApplication.translate("Form", u"0", None))
        self.Buy_Qty_label.setText(QCoreApplication.translate("Form", u"0", None))
        self.start_button.setText(QCoreApplication.translate("Form", u"Start", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Pairing", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Buy Qty", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Sell order filled", None))
        self.Buy_order_filled_label.setText(QCoreApplication.translate("Form", u"0", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Buy order filled", None))
        self.label_26.setText(QCoreApplication.translate("Form", u"Invest", None))
        self.invested_label.setText(QCoreApplication.translate("Form", u"0", None))
        self.sell_asset_label_2.setText(QCoreApplication.translate("Form", u"-", None))
        self.sell_asset_label.setText(QCoreApplication.translate("Form", u"-", None))
        self.start_price_label.setText(QCoreApplication.translate("Form", u"-", None))
        self.price_pairing_label_2.setText(QCoreApplication.translate("Form", u"-", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"Start time", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Current price", None))
        self.bid_price_label.setText(QCoreApplication.translate("Form", u"-", None))
        self.gain_label.setText(QCoreApplication.translate("Form", u"-", None))
        self.price_pairing_label_3.setText(QCoreApplication.translate("Form", u"-", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Bid price", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"start price", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"profit if sailing all now", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Ask price", None))
        self.price_label.setText(QCoreApplication.translate("Form", u"-", None))
        self.ask_price_label.setText(QCoreApplication.translate("Form", u"-", None))
        self.price_pairing_label.setText(QCoreApplication.translate("Form", u"-", None))
        self.price_pairing_label_4.setText(QCoreApplication.translate("Form", u"-", None))
        self.start_time_label.setText(QCoreApplication.translate("Form", u"-", None))
        self.sell_filled_Qty_label.setText(QCoreApplication.translate("Form", u"-", None))
        self.buy_qty_label.setText(QCoreApplication.translate("Form", u"-", None))
        self.Buy_asset_label_3.setText(QCoreApplication.translate("Form", u"-", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"Qty", None))
        self.Buy_asset_label_5.setText(QCoreApplication.translate("Form", u"-", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"Qty filled", None))
        self.buy_filled_Qty_label.setText(QCoreApplication.translate("Form", u"-", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"Buy order ID", None))
        self.Buy_order_ID_label.setText(QCoreApplication.translate("Form", u"-", None))
        self.Buy_asset_label_2.setText(QCoreApplication.translate("Form", u"-", None))
        self.Buy_asset_label_4.setText(QCoreApplication.translate("Form", u"-", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"Sell order ID", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"Qty", None))
        self.sell_qty_label.setText(QCoreApplication.translate("Form", u"-", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"Qty filled", None))
        self.Sell_order_ID_label.setText(QCoreApplication.translate("Form", u"-", None))
        self.label_28.setText(QCoreApplication.translate("Form", u"Open Orders", None))
        self.label_30.setText(QCoreApplication.translate("Form", u"Prevision", None))
        ___qtablewidgetitem = self.Simplino_calcul_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"0", None));
        ___qtablewidgetitem1 = self.Simplino_calcul_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"1", None));
        ___qtablewidgetitem2 = self.Simplino_calcul_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"2", None));
        ___qtablewidgetitem3 = self.Simplino_calcul_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"3", None));
        ___qtablewidgetitem4 = self.Simplino_calcul_table.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem5 = self.Simplino_calcul_table.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem6 = self.Simplino_calcul_table.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem7 = self.Simplino_calcul_table.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem8 = self.Simplino_calcul_table.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem9 = self.Simplino_calcul_table.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem10 = self.Simplino_calcul_table.verticalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem11 = self.Simplino_calcul_table.verticalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem12 = self.Simplino_calcul_table.verticalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem13 = self.Simplino_calcul_table.verticalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem14 = self.Simplino_calcul_table.verticalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem15 = self.Simplino_calcul_table.verticalHeaderItem(11)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem16 = self.Simplino_calcul_table.verticalHeaderItem(12)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem17 = self.Simplino_calcul_table.verticalHeaderItem(13)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem18 = self.Simplino_calcul_table.verticalHeaderItem(14)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem19 = self.Simplino_calcul_table.verticalHeaderItem(15)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("Form", u"New Row", None));

        __sortingEnabled = self.Simplino_calcul_table.isSortingEnabled()
        self.Simplino_calcul_table.setSortingEnabled(False)
        ___qtablewidgetitem20 = self.Simplino_calcul_table.item(0, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("Form", u"Test", None));
        ___qtablewidgetitem21 = self.Simplino_calcul_table.item(0, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("Form", u"Text", None));
        ___qtablewidgetitem22 = self.Simplino_calcul_table.item(0, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("Form", u"Cell", None));
        ___qtablewidgetitem23 = self.Simplino_calcul_table.item(0, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("Form", u"Line", None));
        self.Simplino_calcul_table.setSortingEnabled(__sortingEnabled)

        self.label_29.setText(QCoreApplication.translate("Form", u"Order filled", None))
        ___qtablewidgetitem24 = self.Order_filled_tab.horizontalHeaderItem(0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("Form", u"0", None));
        ___qtablewidgetitem25 = self.Order_filled_tab.horizontalHeaderItem(1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("Form", u"1", None));
        ___qtablewidgetitem26 = self.Order_filled_tab.horizontalHeaderItem(2)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("Form", u"2", None));
        ___qtablewidgetitem27 = self.Order_filled_tab.horizontalHeaderItem(3)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("Form", u"3", None));
        ___qtablewidgetitem28 = self.Order_filled_tab.verticalHeaderItem(0)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem29 = self.Order_filled_tab.verticalHeaderItem(1)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem30 = self.Order_filled_tab.verticalHeaderItem(2)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem31 = self.Order_filled_tab.verticalHeaderItem(3)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem32 = self.Order_filled_tab.verticalHeaderItem(4)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem33 = self.Order_filled_tab.verticalHeaderItem(5)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem34 = self.Order_filled_tab.verticalHeaderItem(6)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem35 = self.Order_filled_tab.verticalHeaderItem(7)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem36 = self.Order_filled_tab.verticalHeaderItem(8)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem37 = self.Order_filled_tab.verticalHeaderItem(9)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem38 = self.Order_filled_tab.verticalHeaderItem(10)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem39 = self.Order_filled_tab.verticalHeaderItem(11)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem40 = self.Order_filled_tab.verticalHeaderItem(12)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem41 = self.Order_filled_tab.verticalHeaderItem(13)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem42 = self.Order_filled_tab.verticalHeaderItem(14)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem43 = self.Order_filled_tab.verticalHeaderItem(15)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("Form", u"New Row", None));

        __sortingEnabled1 = self.Order_filled_tab.isSortingEnabled()
        self.Order_filled_tab.setSortingEnabled(False)
        ___qtablewidgetitem44 = self.Order_filled_tab.item(0, 0)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("Form", u"Test", None));
        ___qtablewidgetitem45 = self.Order_filled_tab.item(0, 1)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("Form", u"Text", None));
        ___qtablewidgetitem46 = self.Order_filled_tab.item(0, 2)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("Form", u"Cell", None));
        ___qtablewidgetitem47 = self.Order_filled_tab.item(0, 3)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("Form", u"Line", None));
        self.Order_filled_tab.setSortingEnabled(__sortingEnabled1)

        ___qtablewidgetitem48 = self.table_history.horizontalHeaderItem(0)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("Form", u"0", None));
        ___qtablewidgetitem49 = self.table_history.horizontalHeaderItem(1)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("Form", u"1", None));
        ___qtablewidgetitem50 = self.table_history.horizontalHeaderItem(2)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("Form", u"2", None));
        ___qtablewidgetitem51 = self.table_history.horizontalHeaderItem(3)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("Form", u"3", None));
        ___qtablewidgetitem52 = self.table_history.verticalHeaderItem(0)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem53 = self.table_history.verticalHeaderItem(1)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem54 = self.table_history.verticalHeaderItem(2)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem55 = self.table_history.verticalHeaderItem(3)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem56 = self.table_history.verticalHeaderItem(4)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem57 = self.table_history.verticalHeaderItem(5)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem58 = self.table_history.verticalHeaderItem(6)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem59 = self.table_history.verticalHeaderItem(7)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem60 = self.table_history.verticalHeaderItem(8)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem61 = self.table_history.verticalHeaderItem(9)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem62 = self.table_history.verticalHeaderItem(10)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem63 = self.table_history.verticalHeaderItem(11)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem64 = self.table_history.verticalHeaderItem(12)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem65 = self.table_history.verticalHeaderItem(13)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem66 = self.table_history.verticalHeaderItem(14)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem67 = self.table_history.verticalHeaderItem(15)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("Form", u"New Row", None));

        __sortingEnabled2 = self.table_history.isSortingEnabled()
        self.table_history.setSortingEnabled(False)
        ___qtablewidgetitem68 = self.table_history.item(0, 0)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("Form", u"Test", None));
        ___qtablewidgetitem69 = self.table_history.item(0, 1)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("Form", u"Text", None));
        ___qtablewidgetitem70 = self.table_history.item(0, 2)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("Form", u"Cell", None));
        ___qtablewidgetitem71 = self.table_history.item(0, 3)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("Form", u"Line", None));
        self.table_history.setSortingEnabled(__sortingEnabled2)

        self.btn_import_history.setText(QCoreApplication.translate("Form", u"Import history", None))
        self.btn_wallet_refresh.setText(QCoreApplication.translate("Form", u"Refresh", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Trade", None))
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("Form", u"BLENDER INSTALLATION", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Your Password", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Open Blender", None))
        self.labelVersion_3.setText(QCoreApplication.translate("Form", u"Ex: C:Program FilesBlender FoundationBlender 2.82 blender.exe", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"CheckBox", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"RadioButton", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"Test 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"Test 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"Test 3", None))

        self.commandLinkButton.setText(QCoreApplication.translate("Form", u"CommandLinkButton", None))
        self.commandLinkButton.setDescription(QCoreApplication.translate("Form", u"Open External Link", None))
        ___qtablewidgetitem72 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("Form", u"0", None));
        ___qtablewidgetitem73 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("Form", u"1", None));
        ___qtablewidgetitem74 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("Form", u"2", None));
        ___qtablewidgetitem75 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("Form", u"3", None));
        ___qtablewidgetitem76 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem77 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem78 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem79 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem80 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem81 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem82 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem83 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem84 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem85 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem86 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem87 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem88 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem88.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem89 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem89.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem90 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem90.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem91 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem91.setText(QCoreApplication.translate("Form", u"New Row", None));

        __sortingEnabled3 = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem92 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem92.setText(QCoreApplication.translate("Form", u"Test", None));
        ___qtablewidgetitem93 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem93.setText(QCoreApplication.translate("Form", u"Text", None));
        ___qtablewidgetitem94 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem94.setText(QCoreApplication.translate("Form", u"Cell", None));
        ___qtablewidgetitem95 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem95.setText(QCoreApplication.translate("Form", u"Line", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled3)

        self.label_credits.setText(QCoreApplication.translate("Form", u"Binance Bot - Cryptocurrency Exchange", None))
        self.label_version.setText(QCoreApplication.translate("Form", u"v0.0.1", None))
    # retranslateUi

