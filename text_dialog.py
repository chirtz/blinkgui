# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'text_dialog.ui'
#
# Created: Thu Oct 30 16:33:24 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_TickerDialog(object):
    def setupUi(self, TickerDialog):
        TickerDialog.setObjectName("TickerDialog")
        TickerDialog.resize(400, 256)
        self.gridLayout = QtGui.QGridLayout(TickerDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(TickerDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.textEdit = QtGui.QLineEdit(TickerDialog)
        self.textEdit.setObjectName("textEdit")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.textEdit)
        self.label_5 = QtGui.QLabel(TickerDialog)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_5)
        self.paddingSpin = QtGui.QSpinBox(TickerDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.paddingSpin.sizePolicy().hasHeightForWidth())
        self.paddingSpin.setSizePolicy(sizePolicy)
        self.paddingSpin.setProperty("value", 2)
        self.paddingSpin.setObjectName("paddingSpin")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.paddingSpin)
        self.label_2 = QtGui.QLabel(TickerDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fontEdit = QtGui.QLineEdit(TickerDialog)
        self.fontEdit.setObjectName("fontEdit")
        self.horizontalLayout.addWidget(self.fontEdit)
        self.openFontButton = QtGui.QPushButton(TickerDialog)
        self.openFontButton.setObjectName("openFontButton")
        self.horizontalLayout.addWidget(self.openFontButton)
        self.formLayout.setLayout(3, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.label_4 = QtGui.QLabel(TickerDialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_4)
        self.fontsizeSpin = QtGui.QSpinBox(TickerDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fontsizeSpin.sizePolicy().hasHeightForWidth())
        self.fontsizeSpin.setSizePolicy(sizePolicy)
        self.fontsizeSpin.setProperty("value", 8)
        self.fontsizeSpin.setObjectName("fontsizeSpin")
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.fontsizeSpin)
        self.label_3 = QtGui.QLabel(TickerDialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_3)
        self.durationSpin = QtGui.QSpinBox(TickerDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.durationSpin.sizePolicy().hasHeightForWidth())
        self.durationSpin.setSizePolicy(sizePolicy)
        self.durationSpin.setMinimum(1)
        self.durationSpin.setMaximum(999999)
        self.durationSpin.setProperty("value", 150)
        self.durationSpin.setObjectName("durationSpin")
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.durationSpin)
        self.label_6 = QtGui.QLabel(TickerDialog)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtGui.QLabel(TickerDialog)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_7)
        self.fontColorButton = QtGui.QPushButton(TickerDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fontColorButton.sizePolicy().hasHeightForWidth())
        self.fontColorButton.setSizePolicy(sizePolicy)
        self.fontColorButton.setObjectName("fontColorButton")
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.fontColorButton)
        self.backgroundColorButton = QtGui.QPushButton(TickerDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backgroundColorButton.sizePolicy().hasHeightForWidth())
        self.backgroundColorButton.setSizePolicy(sizePolicy)
        self.backgroundColorButton.setObjectName("backgroundColorButton")
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.backgroundColorButton)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(TickerDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(TickerDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), TickerDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), TickerDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(TickerDialog)
        TickerDialog.setTabOrder(self.textEdit, self.paddingSpin)
        TickerDialog.setTabOrder(self.paddingSpin, self.fontEdit)
        TickerDialog.setTabOrder(self.fontEdit, self.openFontButton)
        TickerDialog.setTabOrder(self.openFontButton, self.fontsizeSpin)
        TickerDialog.setTabOrder(self.fontsizeSpin, self.fontColorButton)
        TickerDialog.setTabOrder(self.fontColorButton, self.backgroundColorButton)
        TickerDialog.setTabOrder(self.backgroundColorButton, self.durationSpin)
        TickerDialog.setTabOrder(self.durationSpin, self.buttonBox)

    def retranslateUi(self, TickerDialog):
        TickerDialog.setWindowTitle(QtGui.QApplication.translate("TickerDialog", "Create ticker font", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("TickerDialog", "Text:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("TickerDialog", "Padding:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("TickerDialog", "Font:", None, QtGui.QApplication.UnicodeUTF8))
        self.openFontButton.setText(QtGui.QApplication.translate("TickerDialog", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("TickerDialog", "Font size:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("TickerDialog", "Frame duration (ms):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("TickerDialog", "Font color:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("TickerDialog", "Background color:", None, QtGui.QApplication.UnicodeUTF8))
        self.fontColorButton.setText(QtGui.QApplication.translate("TickerDialog", "Choose color", None, QtGui.QApplication.UnicodeUTF8))
        self.backgroundColorButton.setText(QtGui.QApplication.translate("TickerDialog", "Choose color", None, QtGui.QApplication.UnicodeUTF8))

