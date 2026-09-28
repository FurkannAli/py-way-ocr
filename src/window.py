# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(421, 265)
        font = QFont()
        font.setPointSize(12)
        Form.setFont(font)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(9)
        self.label.setFont(font1)

        self.horizontalLayout.addWidget(self.label)

        self.combo_lang = QComboBox(Form)
        self.combo_lang.addItem("")
        self.combo_lang.addItem("")
        self.combo_lang.addItem("")
        self.combo_lang.setObjectName(u"combo_lang")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_lang.sizePolicy().hasHeightForWidth())
        self.combo_lang.setSizePolicy(sizePolicy)
        self.combo_lang.setMaximumSize(QSize(150, 16777215))
        self.combo_lang.setFont(font1)

        self.horizontalLayout.addWidget(self.combo_lang)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.horizontalLayout.addWidget(self.label_2)

        self.combo_psm = QComboBox(Form)
        self.combo_psm.addItem("")
        self.combo_psm.setObjectName(u"combo_psm")
        self.combo_psm.setFont(font1)

        self.horizontalLayout.addWidget(self.combo_psm)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_capture = QPushButton(Form)
        self.btn_capture.setObjectName(u"btn_capture")

        self.horizontalLayout_2.addWidget(self.btn_capture)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.text_result = QTextEdit(Form)
        self.text_result.setObjectName(u"text_result")

        self.verticalLayout_3.addWidget(self.text_result)


        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_copy = QPushButton(Form)
        self.btn_copy.setObjectName(u"btn_copy")
        self.btn_copy.setFont(font1)

        self.horizontalLayout_4.addWidget(self.btn_copy)

        self.lbl_status = QLabel(Form)
        self.lbl_status.setObjectName(u"lbl_status")
        self.lbl_status.setFont(font1)
        self.lbl_status.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.lbl_status)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"py-way-ocr", None))
        self.label.setText(QCoreApplication.translate("Form", u"Language:", None))
        self.combo_lang.setItemText(0, QCoreApplication.translate("Form", u"English (eng)", None))
        self.combo_lang.setItemText(1, QCoreApplication.translate("Form", u"Japanese (jpn)", None))
        self.combo_lang.setItemText(2, QCoreApplication.translate("Form", u"Chinese Simplified (chi_sim)", None))

        self.label_2.setText(QCoreApplication.translate("Form", u"PSM:", None))
        self.combo_psm.setItemText(0, QCoreApplication.translate("Form", u"6 (Single Block)", None))

        self.btn_capture.setText(QCoreApplication.translate("Form", u"Capture", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Extracted Text:", None))
        self.btn_copy.setText(QCoreApplication.translate("Form", u"Copy to clipboard", None))
        self.lbl_status.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

