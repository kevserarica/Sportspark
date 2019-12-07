# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\musta\Desktop\SportParkiProjesi\registerSportPage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(611, 517)
        Dialog.setStyleSheet("background-color: #83230E;\n"
"color: white;")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(60, 60, 411, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.salonpictureButton = QtWidgets.QPushButton(Dialog)
        self.salonpictureButton.setGeometry(QtCore.QRect(60, 400, 491, 31))
        self.salonpictureButton.setStyleSheet("background-color: white; color: black")
        self.salonpictureButton.setObjectName("salonpictureButton")
        self.closeButton = QtWidgets.QPushButton(Dialog)
        self.closeButton.setGeometry(QtCore.QRect(60, 440, 491, 31))
        self.closeButton.setStyleSheet("background-color: white; color: black")
        self.closeButton.setObjectName("closeButton")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(254, 10, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(60, 90, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(320, 96, 231, 21))
        self.comboBox.setStyleSheet("background-color: #83230E;\n"
"color: white;border:2px solid white")
        self.comboBox.setObjectName("comboBox")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(60, 141, 251, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.registerButton = QtWidgets.QPushButton(Dialog)
        self.registerButton.setGeometry(QtCore.QRect(60, 360, 491, 31))
        self.registerButton.setStyleSheet("background-color: white; color: black")
        self.registerButton.setObjectName("registerButton")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(60, 160, 491, 181))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_6.setText(_translate("Dialog", "Welcome. You can register a new sport to be healtyh."))
        self.salonpictureButton.setText(_translate("Dialog", "Salon Piictures"))
        self.closeButton.setText(_translate("Dialog", "Close"))
        self.label_5.setText(_translate("Dialog", "Register Sport"))
        self.label_7.setText(_translate("Dialog", "Which sport you want to register:"))
        self.label_8.setText(_translate("Dialog", "Sessions:"))
        self.registerButton.setText(_translate("Dialog", "Register"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

