# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\musta\Desktop\SportParkiProjesi\Swimming.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(539, 528)
        Dialog.setStyleSheet("background-color: #83230E;\n"
"color: white;")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 20, 501, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.closeButton = QtWidgets.QPushButton(Dialog)
        self.closeButton.setGeometry(QtCore.QRect(20, 470, 501, 31))
        self.closeButton.setStyleSheet("background-color: white; color: black")
        self.closeButton.setObjectName("closeButton")
        self.closeButton.clicked.connect(Dialog.close)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(20, 310, 501, 151))
        self.textEdit.setStyleSheet("border: 2px solid white")
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.photoLabel = QtWidgets.QLabel(Dialog)
        self.photoLabel.setGeometry(QtCore.QRect(20, 60, 491, 241))
        self.photoLabel.setStyleSheet("border: 2px solid white;border-image: url(resim1.jfif);")
        self.photoLabel.setText("")
        self.photoLabel.setObjectName("photoLabel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Swimming</p></body></html>"))
        self.closeButton.setText(_translate("Dialog", "Close"))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Evidence of recreational swimming in prehistoric times has been found, with the earliest evidence dating to Stone Age paintings from around 10,000 years ago. Written references date from 2000 BC, with some of the earliest references to swimming including the Iliad, the Odyssey, the Bible, Beowulf, the Quran and others. In 1538, Nikolaus Wynmann, a Swiss–German professor of languages, wrote the earliest known complete book about swimming, Colymbetes, sive de arte natandi dialogus et festivus et iucundus lecturer. Swimming emerged as a competitive recreational activity in the 1830s in England. In 1828, the first indoor swimming pool, St George\'s Baths was opened to the public.[6] By 1837, the National Swimming Society was holding regular swimming competitions in six artificial swimming pools, built around London. The recreational activity grew in popularity and by 1880, when the first national governing body, the Amateur Swimming Association was formed, there were already over 300 regional clubs in operation across the country.n 1844 two Native American participants at a swimming competition in London introduced the front crawl to a European audience. Sir John Arthur Trudgen picked up the hand-over stroke from some South American natives and successfully debuted the new stroke in 1873, winning a local competition in England. His stroke is still regarded as the most powerful to use today.[8]</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Captain Matthew Webb was the first man to swim the English Channel (between England and France), in 1875. Using the breaststroke technique, he swam the channel 21.26 miles (34.21 km) in 21 hours and 45 minutes. His feat was not replicated or surpassed for the next 36 years, until T.W. Burgess made the crossing in 1911.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Other European countries also established swimming federations; Germany in 1882, France in 1890 and Hungary in 1896. The first European amateur swimming competitions were in 1889 in Vienna. The world\'s first women\'s swimming championship was held in Scotland in 1892.[9]</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

