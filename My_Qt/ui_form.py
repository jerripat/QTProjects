# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(657, 600)
        font = QFont()
        font.setPointSize(12)
        Widget.setFont(font)
        self.pushButton = self._extracted_from_setupUi_8(Widget, u"pushButton", 110, 160)

        self.button_1 = self._extracted_from_setupUi_8(Widget, u"button_1", 230, 350)
        self.label_1 = QLabel(Widget)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setGeometry(QRect(190, 280, 231, 20))
        font1 = QFont()
        font1.setPointSize(18)
        self.label_1.setFont(font1)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)

    # TODO Rename this here and in `setupUi`
    def _extracted_from_setupUi_8(self, Widget, arg1, arg2, arg3):
        result = QPushButton(Widget)
        result.setObjectName(arg1)
        result.setGeometry(QRect(arg2, arg3, 99, 27))
        return result
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"PushButton", None))
        self.button_1.setText(QCoreApplication.translate("Widget", u"Push Me", None))
        self.label_1.setText(QCoreApplication.translate("Widget", u"Hello World", None))
    # retranslateUi
