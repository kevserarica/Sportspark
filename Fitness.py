# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\musta\Desktop\SportParkiProjesi\Fitness.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(533, 509)
        Dialog.setStyleSheet("background-color: #83230E;\n"
"color: white;")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(20, 300, 501, 151))
        self.textEdit.setStyleSheet("border: 2px solid white")
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.photoLabel = QtWidgets.QLabel(Dialog)
        self.photoLabel.setGeometry(QtCore.QRect(20, 50, 491, 241))
        self.photoLabel.setStyleSheet("border: 2px solid white; border-image: url(resim5.jpg);")
        self.photoLabel.setText("")
        self.photoLabel.setObjectName("photoLabel")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 10, 491, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.closeButton = QtWidgets.QPushButton(Dialog)
        self.closeButton.setGeometry(QtCore.QRect(20, 460, 501, 31))
        self.closeButton.setStyleSheet("background-color: white; color: black")
        self.closeButton.setObjectName("closeButton")
        self.closeButton.clicked.connect(Dialog.close)


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">According to the Centers for Disease Control and Prevention (CDC), physical fitness is defined as \'the ability to carry out daily tasks with vigor and alertness, without undue fatigue, and with ample energy to enjoy leisure-time pursuits and respond to emergencies.\' Based on this definition, fitness involves everything from getting out of bed to hiking to performing CPR.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In order to complete all of these tasks, one must consistently address their fitness levels. This requires proper conditioning through both structured exercise and leisurely activities.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Components of Fitness</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Depending on the source, the components of fitness vary considerably. Below are common components:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Cardiorespiratory endurance - typically measured by how long or fast a person can perform an activity and how this impacts measurements such as heart rate and oxygen consumption.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Muscular endurance - typically measured by how many repetitions of an exercise a person can perform. Common tests involve push-ups and sit ups.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Muscular strength - typically measured by how much weight can be moved in relation to repetitions. Exercises involving multiple joints and muscle groups such as squats or bench press are often used.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Muscular power - typically measured by how much force can be generated during a given activity. Advanced equipment used by biomechanists are often needed to measure muscular power.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Flexibility - typically measured by how far a muscle group can be stretched or joint can be moved. The most common tests involve the hamstrings and shoulders.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Balance - typically measured by how long a particular position can be held with or without some type of activity being performed. Simple tests such as standing on one leg can be used to assess balance. More advanced tests may involve standing on an unsteady object while trying to catch a ball.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Speed - typically measured by how quickly an individual can move from one point to another. The 40-yard dash is often used to assess speed.</p></body></html>"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Fitness</p></body></html>"))
        self.closeButton.setText(_translate("Dialog", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

