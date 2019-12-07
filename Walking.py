# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\musta\Desktop\SportParkiProjesi\Walking.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(528, 502)
        Dialog.setStyleSheet("background-color: #83230E;\n"
"color: white;")
        self.photoLabel = QtWidgets.QLabel(Dialog)
        self.photoLabel.setGeometry(QtCore.QRect(13, 47, 501, 241))
        self.photoLabel.setStyleSheet("border: 2px solid white; border-image: url(resim3.jpg);")
        self.photoLabel.setText("")
        self.photoLabel.setObjectName("photoLabel")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(13, 297, 501, 151))
        self.textEdit.setStyleSheet("border: 2px solid white")
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(13, 7, 491, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.closeButton = QtWidgets.QPushButton(Dialog)
        self.closeButton.setGeometry(QtCore.QRect(13, 457, 501, 31))
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
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The word walk is descended from the Old English wealcan &quot;to roll&quot;. In humans and other bipeds, walking is generally distinguished from running in that only one foot at a time leaves contact with the ground and there is a period of double-support. In contrast, running begins when both feet are off the ground with each step. This distinction has the status of a formal requirement in competitive walking events. For quadrupedal species, there are numerous gaits which may be termed walking or running, and distinctions based upon the presence or absence of a suspended phase or the number of feet in contact any time do not yield mechanically correct classification.[1] The most effective method to distinguish walking from running is to measure the height of a person\'s centre of mass using motion capture or a force plate at midstance. During walking, the centre of mass reaches a maximum height at midstance, while during running, it is then at a minimum. This distinction, however, only holds true for locomotion over level or approximately level ground. For walking up grades above 10%, this distinction no longer holds for some individuals. Definitions based on the percentage of the stride during which a foot is in contact with the ground (averaged across all feet) of greater than 50% contact corresponds well with identification of \'inverted pendulum\' mechanics and are indicative of walking for animals with any number of limbs, although this definition is incomplete.[1] Running humans and animals may have contact periods greater than 50% of a gait cycle when rounding corners, running uphill or carrying loads.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Speed is another factor that distinguishes walking from running. Although walking speeds can vary greatly depending on many factors such as height, weight, age, terrain, surface, load, culture, effort, and fitness, the average human walking speed at crosswalks is about 5.0 kilometres per hour (km/h), or about 1.4 meters per second (m/s), or about 3.1 miles per hour (mph). Specific studies have found pedestrian walking speeds at crosswalks ranging from 4.51 kilometres per hour (2.80 mph) to 4.75 kilometres per hour (2.95 mph) for older individuals and from 5.32 kilometres per hour (3.31 mph) to 5.43 kilometres per hour (3.37 mph) for younger individuals;[2][3] a brisk walking speed can be around 6.5 kilometres per hour (4.0 mph).[4] In Japan, the standard measure for walking distance is 80 meters for 1 minute of walking time or 4.8km/h. Champion racewalkers can average more than 14 kilometres per hour (8.7 mph) over a distance of 20 kilometres (12 mi).</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">An average human child achieves independent walking ability at around 11 months old.[5]</p></body></html>"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Walking</p></body></html>"))
        self.closeButton.setText(_translate("Dialog", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

