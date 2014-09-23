# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lg_dialog.ui'
#
# Created: Tue Sep 23 20:15:23 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_LinearGradientDialog(object):
    def setupUi(self, LinearGradientDialog):
        LinearGradientDialog.setObjectName("LinearGradientDialog")
        LinearGradientDialog.resize(275, 200)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LinearGradientDialog.sizePolicy().hasHeightForWidth())
        LinearGradientDialog.setSizePolicy(sizePolicy)
        LinearGradientDialog.setMinimumSize(QtCore.QSize(275, 200))
        LinearGradientDialog.setMaximumSize(QtCore.QSize(275, 200))
        self.verticalLayout = QtGui.QVBoxLayout(LinearGradientDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(LinearGradientDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.stepsSpin = QtGui.QSpinBox(LinearGradientDialog)
        self.stepsSpin.setMaximum(100000)
        self.stepsSpin.setProperty("value", 1000)
        self.stepsSpin.setObjectName("stepsSpin")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.stepsSpin)
        self.label_2 = QtGui.QLabel(LinearGradientDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtGui.QLabel(LinearGradientDialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtGui.QLabel(LinearGradientDialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_4)
        self.phaseRedSpin = QtGui.QDoubleSpinBox(LinearGradientDialog)
        self.phaseRedSpin.setProperty("value", 2.0)
        self.phaseRedSpin.setObjectName("phaseRedSpin")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.phaseRedSpin)
        self.phaseGreenSpin = QtGui.QDoubleSpinBox(LinearGradientDialog)
        self.phaseGreenSpin.setObjectName("phaseGreenSpin")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.phaseGreenSpin)
        self.phaseBlueSpin = QtGui.QDoubleSpinBox(LinearGradientDialog)
        self.phaseBlueSpin.setProperty("value", 4.0)
        self.phaseBlueSpin.setObjectName("phaseBlueSpin")
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.phaseBlueSpin)
        self.label_5 = QtGui.QLabel(LinearGradientDialog)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtGui.QLabel(LinearGradientDialog)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_6)
        self.centralValueSpin = QtGui.QSpinBox(LinearGradientDialog)
        self.centralValueSpin.setMaximum(255)
        self.centralValueSpin.setProperty("value", 128)
        self.centralValueSpin.setObjectName("centralValueSpin")
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.centralValueSpin)
        self.valueRangeSpin = QtGui.QSpinBox(LinearGradientDialog)
        self.valueRangeSpin.setMaximum(255)
        self.valueRangeSpin.setProperty("value", 127)
        self.valueRangeSpin.setObjectName("valueRangeSpin")
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.valueRangeSpin)
        self.durationSpin = QtGui.QSpinBox(LinearGradientDialog)
        self.durationSpin.setMaximum(100000)
        self.durationSpin.setProperty("value", 10)
        self.durationSpin.setObjectName("durationSpin")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.durationSpin)
        self.label_7 = QtGui.QLabel(LinearGradientDialog)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_7)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtGui.QDialogButtonBox(LinearGradientDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(LinearGradientDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), LinearGradientDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), LinearGradientDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(LinearGradientDialog)
        LinearGradientDialog.setTabOrder(self.durationSpin, self.stepsSpin)
        LinearGradientDialog.setTabOrder(self.stepsSpin, self.phaseRedSpin)
        LinearGradientDialog.setTabOrder(self.phaseRedSpin, self.phaseGreenSpin)
        LinearGradientDialog.setTabOrder(self.phaseGreenSpin, self.phaseBlueSpin)
        LinearGradientDialog.setTabOrder(self.phaseBlueSpin, self.centralValueSpin)
        LinearGradientDialog.setTabOrder(self.centralValueSpin, self.valueRangeSpin)
        LinearGradientDialog.setTabOrder(self.valueRangeSpin, self.buttonBox)

    def retranslateUi(self, LinearGradientDialog):
        LinearGradientDialog.setWindowTitle(QtGui.QApplication.translate("LinearGradientDialog", "Linear color gradient", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("LinearGradientDialog", "Number of steps:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("LinearGradientDialog", "Phase Red:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("LinearGradientDialog", "Phase Green:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("LinearGradientDialog", "Phase Blue:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("LinearGradientDialog", "Central value:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("LinearGradientDialog", "Value range:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("LinearGradientDialog", "Frame Duration (ms):", None, QtGui.QApplication.UnicodeUTF8))

