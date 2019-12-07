# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\musta\Desktop\SportParkiProjesi\checkYourSport.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

import sqlite3

class Ui_Dialog(object):

    def checkInfo(self):
        tc = self.tcLineEdit.text().format(str)
        if len(tc) > 0:
            dbase = sqlite3.connect('sportParkProject.db')

            while self.tableWidget.rowCount() > 0:
                self.tableWidget.removeRow(0)
            query = 'SELECT * FROM Register'
            res = dbase.execute(query)
            jumpCounter = 0
            for row_index, row_data in enumerate(res):
                self.tableWidget.insertRow(row_index)
                if jumpCounter % 10 ==0:
                    for colm_index, colm_data in enumerate(row_data):
                        if colm_data == tc:
                            jumpCounter = 10
                        if jumpCounter > 0:
                            self.tableWidget.setItem(0, colm_index-1, QTableWidgetItem(str(colm_data)))
                            print("C: ", jumpCounter, " Colum_index: ", colm_index, " Column_data: ", colm_data,
                                  " Row_index: ", row_index)
                            jumpCounter = jumpCounter - 1

            dbase.close()
            return
        else:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setIcon(QtWidgets.QMessageBox.Warning)
            msgBox.setWindowTitle("Check Page")
            msgBox.setText("Please check your information.")
            msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msgBox.exec_()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(535, 328)
        Dialog.setStyleSheet("background-color: #83230E;\n"
                             "color: white;")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 20, 491, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.closeButton = QtWidgets.QPushButton(Dialog)
        self.closeButton.setGeometry(QtCore.QRect(20, 270, 491, 31))
        self.closeButton.setStyleSheet("background-color: white; color: black")
        self.closeButton.setObjectName("closeButton")
        self.closeButton.clicked.connect(Dialog.close)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(20, 120, 491, 91))
        self.tableWidget.setStyleSheet("background-color: #83230E;\n"
                                       "border:2px solid white;color: black ; font-weight: bold")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setRowCount(10)
        self.checkButton = QtWidgets.QPushButton(Dialog)
        self.checkButton.setGeometry(QtCore.QRect(20, 230, 491, 31))
        self.checkButton.setStyleSheet("background-color: white; color: black")
        self.checkButton.setObjectName("checkButton")
        self.checkButton.clicked.connect(self.checkInfo)
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(30, 81, 161, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.tcLineEdit = QtWidgets.QLineEdit(Dialog)
        self.tcLineEdit.setGeometry(QtCore.QRect(210, 80, 301, 20))
        self.tcLineEdit.setStyleSheet("background-color: #83230E;\n"
                                      "color: white;border:2px solid white")
        self.tcLineEdit.setObjectName("tcLineEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_5.setText(_translate("Dialog",
                                        "<html><head/><body><p align=\"center\">You can see your registered sport</p></body></html>"))
        self.closeButton.setText(_translate("Dialog", "Close"))
        self.checkButton.setText(_translate("Dialog", "Check"))
        self.label_9.setText(_translate("Dialog", "Identity Card Number:"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
