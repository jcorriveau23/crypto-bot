from main import *
from main import MainWindow

GLOBAL_STATE = 0
GLOBAL_TITLE_BAR = True

count = 1


class UIFunctions(MainWindow):

    # Globals
    GLOBAL_STATE = 0
    GLOBAL_TITLE_BAR = True

    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == 0:
            self.showMaximized()
            GLOBAL_STATE = 1
            self.ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.ui.btn_maximize_restore.setToolTip("Restore")
            self.ui.btn_maximize_restore.setIcon(QtGui.QIcon(u":/16x16/icons/16x16/cil-window-restore.png"))
            self.ui.frame_top_btns.setStyleSheet("background-color: rgb(27, 29, 35)")
            self.ui.frame_size_grip.hide()
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.horizontalLayout.setContentsMargins(10, 10, 10, 10)
            self.ui.btn_maximize_restore.setToolTip("Maximize")
            self.ui.btn_maximize_restore.setIcon(QtGui.QIcon(u":/16x16/icons/16x16/cil-window-maximize.png"))
            self.ui.frame_top_btns.setStyleSheet("background-color: rgba(27, 29, 35, 200)")
            self.ui.frame_size_grip.show()

    @staticmethod
    def return_status():
        return GLOBAL_STATE

    def set_status(self):
        global GLOBAL_STATE
        GLOBAL_STATE = self

    def enable_maximum_size(self, width, height):
        if width != '' and height != '':
            self.setMaximumSize(QSize(width, height))
            self.ui.frame_size_grip.hide()
            self.ui.btn_maximize_restore.hide()

    def toggle_menu(self, max_width, enable):
        if enable:
            # Get width
            width = self.ui.frame_left_menu.width()
            max_extend = max_width
            standard = 70

            # Set max width
            if width == 70:
                width_extended = max_extend
            else:
                width_extended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(300)
            self.animation.setStartValue(width)
            self.animation.setEndValue(width_extended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    def remove_title_bar(status):
        global GLOBAL_TITLE_BAR
        GLOBAL_TITLE_BAR = status

    def label_title(self, text):
        self.ui.label_title_bar_top.setText(text)

    # LABEL DESCRIPTION
    def label_description(self, text):
        self.ui.label_top_info_1.setText(text)

    def add_new_menu(self, name, objName, icon, isTopMenu):
        font = QFont()
        font.setFamily(u"Segoe UI")
        button = QPushButton(str(count), self)
        button.setObjectName(objName)
        size_policy_3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        size_policy_3.setHorizontalStretch(0)
        size_policy_3.setVerticalStretch(0)
        size_policy_3.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
        button.setSizePolicy(size_policy_3)
        button.setMinimumSize(QSize(0, 70))
        button.setLayoutDirection(Qt.LeftToRight)
        button.setFont(font)
        button.setStyleSheet(Style.style_bt_standard.replace('ICON_REPLACE', icon))
        button.setText(name)
        button.setToolTip(name)
        button.clicked.connect(self.button)

        if isTopMenu:
            self.ui.layout_menus.addWidget(button)
        else:
            self.ui.layout_menu_bottom.addWidget(button)

    @staticmethod
    def select_menu(get_style):
        select = get_style + ("QPushButton { border-right: 7px solid rgb(44, 49, 60); }")
        return select

    @staticmethod
    def deselect_menu(get_style):
        deselect = get_style.replace("QPushButton { border-right: 7px solid rgb(44, 49, 60); }", "")
        return deselect

    def reset_style(self, widget):
        for w in self.ui.frame_left_menu.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(UIFunctions.deselect_menu(w.styleSheet()))

    def label_page(self, text):
        new_text = '| ' + text.upper()
        self.ui.label_top_info_2.setText(new_text)

    def user_icon(self, initials_tooltip, icon, show_hide):
        if show_hide:

            self.ui.label_user_icon.setText(initials_tooltip)

            if icon:
                style = self.ui.label_user_icon.styleSheet()
                set_icon = "QLabel { background-image: " + icon + "; }"
                self.ui.label_user_icon.setStyleSheet(style + set_icon)
                self.ui.label_user_icon.setText('')
                self.ui.label_user_icon.setToolTip(initials_tooltip)
        else:
            self.ui.label_user_icon.hide()

    def ui_definitions(self):
        def double_click_maximize_restore(event):
            # IF DOUBLE CLICK CHANGE STATUS
            if event.type() == QtCore.QEvent.MouseButtonDblClick:
                QtCore.QTimer.singleShot(250, lambda: UIFunctions.maximize_restore(self))

        if GLOBAL_TITLE_BAR:
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
            self.ui.frame_label_top_btns.mouseDoubleClickEvent = double_click_maximize_restore
        else:
            self.ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.ui.frame_label_top_btns.setContentsMargins(8, 0, 0, 5)
            self.ui.frame_label_top_btns.setMinimumHeight(42)
            self.ui.frame_icon_top_bar.hide()
            self.ui.frame_btns_right.hide()
            self.ui.frame_size_grip.hide()

        # Drop shadow effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.frame_main.setGraphicsEffect(self.shadow)

        # Resize window
        self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

        # Minimize
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())

        # Maximize / Restore
        self.ui.btn_maximize_restore.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        # Close application
        self.ui.btn_close.clicked.connect(lambda: self.close())

