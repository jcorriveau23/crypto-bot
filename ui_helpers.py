from PySide2 import QtCore, QtGui, QtWidgets

from ui_styles import Style
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)


def create_label(text='none'):
    label = QtWidgets.QLabel()
    label.setText(text)
    return label


