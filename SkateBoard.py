# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\musta\Desktop\SportParkiProjesi\SkateBoard.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(534, 513)
        Dialog.setStyleSheet("background-color: #83230E;\n"
"color: white;")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 10, 491, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(20, 300, 501, 151))
        self.textEdit.setStyleSheet("border: 2px solid white")
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.closeButton = QtWidgets.QPushButton(Dialog)
        self.closeButton.setGeometry(QtCore.QRect(20, 460, 501, 31))
        self.closeButton.setStyleSheet("background-color: white; color: black")
        self.closeButton.setObjectName("closeButton")
        self.closeButton.clicked.connect(Dialog.close)
        self.photoLabel = QtWidgets.QLabel(Dialog)
        self.photoLabel.setGeometry(QtCore.QRect(20, 50, 491, 241))
        self.photoLabel.setStyleSheet("border: 2px solid white;border-image: url(resim4.jpg);")
        self.photoLabel.setText("")
        self.photoLabel.setObjectName("photoLabel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Skateboard</p></body></html>"))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A skateboard is a type of sports equipment used for skateboarding. They are usually made of a specially designed 7-ply maple plywood deck with a polyurethane coating for smoothness and durability and wheels attached to the underside.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The skateboarder moves by pushing with one foot with other foot balanced on the board, or by pumping one\'s legs in structures such as a bowl or half pipe. A skateboard can also be used by simply standing on the deck while on a downward slope and allowing gravity to propel the board and rider. If the rider\'s leading foot is their right foot, they are said to ride &quot;goofy;&quot; if the rider\'s leading foot is their left foot, they are said to ride &quot;regular.&quot; If the rider is normally regular but chooses to ride goofy, they are said to be riding in &quot;switch,&quot; and vice versa. A skater is typically more comfortable pushing with their back foot; choosing to push with the front foot is commonly referred to as riding &quot;mongo&quot;, and has negative connotations of style and effectiveness in the skateboarding community.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In the early 2000s, electric skateboards have also appeared. These no longer require the propelling of the skateboard by means of the feet; rather an electric motor propels the board, fed by an electric battery.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">There is no governing body that declares any regulations on what constitutes a skateboard or the parts from which it is assembled. Historically, the skateboard has conformed both to contemporary trends and to the ever-evolving array of stunts performed by riders/users, who require a certain functionality from the board. The board shape depends largely upon its desired function. Longboards are a type of skateboard with a longer wheelbase and larger, softer wheels.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The two main types of skateboards are the longboard and the shortboard. The shape of the board is also important: the skateboard must be concaved to perform tricks.[1] Longboards are usually faster and are mostly used for cruising and racing, while shortboards are mostly used for doing tricks and riding in skateparks.</p></body></html>"))
        self.closeButton.setText(_translate("Dialog", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

