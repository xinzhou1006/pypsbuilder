# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adduni.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddUni(object):
    def setupUi(self, AddUni):
        AddUni.setObjectName("AddUni")
        AddUni.resize(300, 100)
        self.verticalLayout = QtWidgets.QVBoxLayout(AddUni)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(AddUni)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.labelEdit = QtWidgets.QLineEdit(AddUni)
        self.labelEdit.setObjectName("labelEdit")
        self.horizontalLayout_2.addWidget(self.labelEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(AddUni)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.comboBegin = QtWidgets.QComboBox(AddUni)
        self.comboBegin.setObjectName("comboBegin")
        self.horizontalLayout.addWidget(self.comboBegin)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(AddUni)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.comboEnd = QtWidgets.QComboBox(AddUni)
        self.comboEnd.setObjectName("comboEnd")
        self.horizontalLayout.addWidget(self.comboEnd)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(AddUni)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(AddUni)
        self.buttonBox.accepted.connect(AddUni.accept)
        self.buttonBox.rejected.connect(AddUni.reject)
        QtCore.QMetaObject.connectSlotsByName(AddUni)

    def retranslateUi(self, AddUni):
        _translate = QtCore.QCoreApplication.translate
        AddUni.setWindowTitle(_translate("AddUni", "Add univariant line"))
        self.label.setText(_translate("AddUni", "Label"))
        self.label_2.setText(_translate("AddUni", "Begin:"))
        self.label_3.setText(_translate("AddUni", "End:"))

