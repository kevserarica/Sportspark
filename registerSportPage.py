# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\musta\Desktop\SportParkiProjesi\registerSportPage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import salonPicturePage
import sqlite3

dbase = sqlite3.connect('sportParkProject.db')
class Ui_Dialog(object):
    def register(self):
        tc = self.tcLineEdit.text().format(str)
        registeredSport = self.comboBox.currentText().format(str)
        dbase = sqlite3.connect('sportParkProject.db')
        if len(tc) > 0 and len(registeredSport) > 0 :
            dbase.execute('''UPDATE Register SET registeredSport = ? WHERE TC = ?'''
                          ,(registeredSport, tc))
            dbase.commit()
            dbase.close()
            self.giveSuccess()
        else:
            self.giveError()

    def load(self):
        dbase = sqlite3.connect('sportParkProject.db')
        while self.tableWidget.rowCount() > 0:
            self.tableWidget.removeRow(0)
        query = 'SELECT * FROM Sports'
        res = dbase.execute(query)
        for row_index, row_data in enumerate(res):
            self.tableWidget.insertRow(row_index)
            for colm_index, colm_data in enumerate(row_data):
                self.tableWidget.setItem(row_index, colm_index, QTableWidgetItem(str(colm_data)))
        dbase.close()
        return

    def giveSuccess(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle("Successfully Added")
        msgBox.setText("Thank you. Successfully Added.")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def giveError(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle("Check Page")
        msgBox.setText("Please check your information.")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def goToSalonPictures(self):
        self.window = QtWidgets.QWidget()
        self.ui = salonPicturePage.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def getInfosInComboBox(self):
        dbase = sqlite3.connect('sportParkProject.db')
        while self.tableWidget.rowCount() > 0:
            self.tableWidget.removeRow(0)
        query = 'SELECT sportID FROM Sports'
        res = dbase.execute(query)
        for row_index, row_data in enumerate(res):
            self.tableWidget.insertRow(row_index)
            for colm_index, colm_data in enumerate(row_data):
                self.comboBox.addItem(str(colm_data))
        res = dbase.execute(query)
        dbase.close()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(611, 517)
        Dialog.setStyleSheet("background-color: #83230E;\n""color: white;")
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
        self.salonpictureButton.setGeometry(QtCore.QRect(60, 430, 491, 31))
        self.salonpictureButton.setStyleSheet("background-color: white; color: black")
        self.salonpictureButton.setObjectName("salonpictureButton")
        self.salonpictureButton.clicked.connect(self.goToSalonPictures)
        self.closeButton = QtWidgets.QPushButton(Dialog)
        self.closeButton.setGeometry(QtCore.QRect(60, 470, 491, 31))
        self.closeButton.setStyleSheet("background-color: white; color: black")
        self.closeButton.setObjectName("closeButton")
        self.closeButton.clicked.connect(Dialog.close)
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
        self.comboBox.setGeometry(QtCore.QRect(240, 340, 311, 21))
        self.comboBox.setStyleSheet("background-color: #83230E;\n"
"color: white;border:2px solid white")
        self.comboBox.setObjectName("comboBox")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(60, 341, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.registerButton = QtWidgets.QPushButton(Dialog)
        self.registerButton.setGeometry(QtCore.QRect(60, 390, 491, 31))
        self.registerButton.setStyleSheet("background-color: white; color: black")
        self.registerButton.setObjectName("registerButton")
        self.registerButton.clicked.connect(self.register)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(60, 120, 491, 181))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(4)
        self.tableWidget.setStyleSheet("color: black ; font-weight: bold")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(60, 311, 161, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.tcLineEdit = QtWidgets.QLineEdit(Dialog)
        self.tcLineEdit.setGeometry(QtCore.QRect(240, 310, 311, 20))
        self.tcLineEdit.setStyleSheet("background-color: #83230E;\n"
"color: white;border:2px solid white")
        self.tcLineEdit.setObjectName("tcLineEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.getInfosInComboBox()
        self.load()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_6.setText(_translate("Dialog", "Welcome. You can register a new sport to be healtyh."))
        self.salonpictureButton.setText(_translate("Dialog", "Salon Pictures"))
        self.closeButton.setText(_translate("Dialog", "Close"))
        self.label_5.setText(_translate("Dialog", "Register Sport"))
        self.label_7.setText(_translate("Dialog", "Which sport you want to register:"))
        self.label_8.setText(_translate("Dialog", "Sessions by ID:"))
        self.registerButton.setText(_translate("Dialog", "Register"))
        self.label_9.setText(_translate("Dialog", "Identity Card Number:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

