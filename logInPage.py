# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logInPage.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import aboutUsPage
import registerPage
import managerPage
import sqlite3
import registerSportPage
dbase = sqlite3.connect('sportParkProject.db')

class Ui_Dialog(object):
    def goManagerPage(self):
        self.window = QtWidgets.QWidget()
        self.ui = managerPage.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def goRegisterPage(self):
        self.window = QtWidgets.QWidget()
        self.ui = registerPage.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def checkInfos(self):
        tc = self.lineEdit.text().format(str)
        password = self.lineEdit_2.text().format(str)
        result = dbase.execute(''' SELECT TC, password FROM Register WHERE TC = ? AND Password = ?''', (tc,password))
        if len(result.fetchall())>0 :
            self.window = QtWidgets.QWidget()
            self.ui = registerSportPage.Ui_Dialog()
            self.ui.setupUi(self.window)
            self.window.show()
        else:
            self.giveError()
    def giveError(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle("Check Page")
        msgBox.setText("Please check your information.")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()
    def goAboutUs(self):
        self.window = QtWidgets.QWidget()
        self.ui = aboutUsPage.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(456, 293)
        Dialog.setStyleSheet("background-color: #83230E;\n"
"color: white;")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(80, 70, 301, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 140, 301, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(80, 110, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(80, 50, 47, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.managerButton = QtWidgets.QPushButton(Dialog)
        self.managerButton.setGeometry(QtCore.QRect(80, 225, 91, 31))
        self.managerButton.setStyleSheet("background-color: white; color: black")
        self.managerButton.setObjectName("managerButton")
        self.managerButton.clicked.connect(self.goManagerPage)
        self.registerButton = QtWidgets.QPushButton(Dialog)
        self.registerButton.setGeometry(QtCore.QRect(190, 225, 91, 31))
        self.registerButton.setStyleSheet("background-color: white; color: black")
        self.registerButton.setObjectName("registerButton")
        self.registerButton.clicked.connect(self.goRegisterPage)
        self.aboutUsbutton = QtWidgets.QPushButton(Dialog)
        self.aboutUsbutton.setGeometry(QtCore.QRect(290, 225, 91, 31))
        self.aboutUsbutton.setStyleSheet("background-color: white; color: black")
        self.aboutUsbutton.setObjectName("aboutUsbutton")
        self.aboutUsbutton.clicked.connect(self.goAboutUs)
        self.loginButton = QtWidgets.QPushButton(Dialog)
        self.loginButton.setGeometry(QtCore.QRect(80, 180, 301, 31))
        self.loginButton.setStyleSheet("background-color: white; color: black")
        self.loginButton.setObjectName("loginButton")
        self.loginButton.clicked.connect(self.checkInfos)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(155, 10, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "Password"))
        self.label_4.setText(_translate("Dialog", "TC"))
        self.managerButton.setText(_translate("Dialog", "Manager"))
        self.registerButton.setText(_translate("Dialog", "Register"))
        self.aboutUsbutton.setText(_translate("Dialog", "About Us"))
        self.loginButton.setText(_translate("Dialog", "Login"))
        self.label_5.setText(_translate("Dialog", "Senlik Sport Center"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
