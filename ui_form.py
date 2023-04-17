# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(245, 292)
        Widget.setStyleSheet(u"")
        self.gridLayout = QGridLayout(Widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Right_Btn = QPushButton(Widget)
        self.Right_Btn.setObjectName(u"Right_Btn")
        self.Right_Btn.setMinimumSize(QSize(50, 50))
        self.Right_Btn.setSizeIncrement(QSize(0, 0))

        self.gridLayout.addWidget(self.Right_Btn, 0, 0, 1, 1)

        self.Add_btn = QPushButton(Widget)
        self.Add_btn.setObjectName(u"Add_btn")
        self.Add_btn.setMinimumSize(QSize(50, 50))
        self.Add_btn.setAutoFillBackground(False)

        self.gridLayout.addWidget(self.Add_btn, 0, 1, 1, 1)

        self.Record_List = QListWidget(Widget)
        self.Record_List.setObjectName(u"Record_List")
        self.Record_List.setStyleSheet(u"border-style:outset;\n"
"        border-width:3px;\n"
"\n"
"        color:rgb(185, 155, 127);\n"
"        border-radius: 8px;\n"
"        font: \"Arial\";\n"
"        font-size: 23px;\n"
"        border: 2px solid #00b894;")

        self.gridLayout.addWidget(self.Record_List, 1, 0, 1, 2)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"\u865b\u64ec\u53f3\u9375", None))
        self.Right_Btn.setText(QCoreApplication.translate("Widget", u"Right_Down", None))
        self.Add_btn.setText(QCoreApplication.translate("Widget", u"Add", None))
    # retranslateUi

