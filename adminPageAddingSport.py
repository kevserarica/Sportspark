# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\musta\Desktop\SportParkiProjesi\adminPageAddingSport.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import sqlite3

dbase = sqlite3.connect('sportParkProject.db')


class Ui_Dialog(object):
    def addSport(self):
        sportName = self.lineEdit.text().format(str)
        sportTime = self.lineEdit_2.text().format(str)
        gender = self.lineEdit_3.text().format(str)
        if len(sportName) > 0 and len(sportTime) > 0 and len(gender) > 0:
            self.addInfos(sportName,sportTime,gender)
            self.giveSuccess()
            self.load()
        else:
            self.giveError()

    def addInfos(self,name,session,gender):
        dbase = sqlite3.connect('sportParkProject.db')
        dbase.execute('''INSERT INTO Sports(sportName,session,forGender) VALUES(?,?,?)''',
                         (name, session,gender))
        dbase.commit()  # To Applying the Changes
        dbase.close()
    def load(self):
        dbase = sqlite3.connect('sportParkProject.db')
        while self.tableWidget.rowCount() > 0:
            self.tableWidget.removeRow(0)
        query = 'SELECT sportName,session,forGender FROM Sports'
        res = dbase.execute(query)
        for row_index, row_data in enumerate(res):
            self.tableWidget.insertRow(row_index)
            for colm_index, colm_data in enumerate(row_data):
                self.tableWidget.setItem(row_index, colm_index, QTableWidgetItem(str(colm_data)))
        dbase.close()
        return
    def delete(self):
        dbase = sqlite3.connect('sportParkProject.db')
        cursor = dbase.cursor()
        query = 'SELECT * FROM Sports'
        alldata = dbase.execute(query)
        for row in enumerate(alldata):
            if row[0] == self.tableWidget.currentRow():
                data = row[1]
                sportID = data[0]
                SportName = data[1]
                session = data[2]
                forGender = data[3]
                cursor.execute(
                    ''' DELETE FROM Sports WHERE sportID = ? AND SportName = ? AND session = ? AND forGender = ?''',
                    (sportID, SportName, session, forGender))
                dbase.commit()
                self.deletedMessage()
                self.load()
    def deletedMessage(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle("Deleted Info")
        msgBox.setText("Successfully Deleted.")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

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

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(599, 481)
        Dialog.setStyleSheet("background-color: #83230E;\n"
                             "color: white;")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(60, 10, 491, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.addButton = QtWidgets.QPushButton(Dialog)
        self.addButton.setGeometry(QtCore.QRect(60, 390, 251, 31))
        self.addButton.setStyleSheet("background-color: white; color: black")
        self.addButton.setObjectName("addButton")
        self.addButton.clicked.connect(self.load)
        self.closeButton = QtWidgets.QPushButton(Dialog)
        self.closeButton.setGeometry(QtCore.QRect(60, 430, 491, 31))
        self.closeButton.setStyleSheet("background-color: white; color: black")
        self.closeButton.setObjectName("closeButton")
        self.closeButton.clicked.connect(Dialog.close)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(60, 60, 461, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 100, 135, 46))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(250, 100, 133, 18))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 124, 133, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setPlaceholderText("15.30 - 16.30")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(420, 124, 133, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setPlaceholderText("Female")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(420, 100, 133, 18))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(60, 150, 491, 181))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(3)
        self.deleteButton = QtWidgets.QPushButton(Dialog)
        self.deleteButton.setGeometry(QtCore.QRect(320, 390, 231, 31))
        self.deleteButton.setStyleSheet("background-color: white; color: black")
        self.deleteButton.setObjectName("deleteButton")
        self.deleteButton.clicked.connect(self.delete)
        self.refreshButton = QtWidgets.QPushButton(Dialog)
        self.refreshButton.setGeometry(QtCore.QRect(60, 350, 491, 31))
        self.refreshButton.setStyleSheet("background-color: white; color: black")
        self.refreshButton.setObjectName("refreshButton")
        self.refreshButton.clicked.connect(self.addSport)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.load()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_5.setText(
            _translate("Dialog", "<html><head/><body><p align=\"center\">Admin Page</p></body></html>"))
        self.addButton.setText(_translate("Dialog", "Refresh"))
        self.closeButton.setText(_translate("Dialog", "Close"))
        self.label_6.setText(_translate("Dialog", "Welcome Sir. You can add or delete sports in this page"))
        self.label_4.setText(_translate("Dialog", "Sport Name"))
        self.label_7.setText(_translate("Dialog", "Sport Time"))
        self.label_8.setText(_translate("Dialog", "Which Gender"))
        self.deleteButton.setText(_translate("Dialog", "Delete Sport"))
        self.refreshButton.setText(_translate("Dialog", "Add"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
