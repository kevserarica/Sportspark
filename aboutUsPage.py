# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutUsPage.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setStyleSheet("background-color: #83230E;\n"
"color: white;")
        self.closebutton = QtWidgets.QPushButton(Dialog)
        self.closebutton.setGeometry(QtCore.QRect(20, 250, 371, 31))
        self.closebutton.setStyleSheet("background-color: white; color: black")
        self.closebutton.setObjectName("closebutton")
        self.closebutton.clicked.connect(Dialog.close)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(160, 20, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 60, 381, 171))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.textEdit, self.closebutton)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.closebutton.setText(_translate("Dialog", "Close"))
        self.label_5.setText(_translate("Dialog", "About Us"))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#000000; background-color:#ffffff;\">Kuruluşu ve Mahalleleri</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Tahoma,Geneva,sans-serif\'; color:#ffffff; background-color:transparent;\">2008 yılında Küçükçekmece, Esenler ve Büyükçekmece ilçelerinden ayrılarak ilçe yapılmıştır.Başakşehir, kuzeyde Arnavutköy, kuzeydoğuda Sultangazi, doğuda Esenler, güneyde Bağcılar, Küçükçekmece ve Avcılar ile batıda Esenyurt ilçeleriyle çevrilidir. Başakşehir 1. ve 2. etapları, Altınşehir merkezi, Güvercintepe, Şahintepe mahalleleri ve Kayabaşı köyü Küçükçekmece Belediyesi\'ne, 4. etap ve 5. etap\'ı EsenlerBelediyesi\'ne, Bahçeşehir ise Büyükçekmece ilçesine bağlı bir belde belediyesi durumundaydı. Fakat son yapılan düzenlemelerle bu semtler birleştirilerek Başakşehir ilçesi kuruldu.    </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ffffff; background-color:#ffffff;\">Tarihçe</span><span style=\" font-family:\'Tahoma,Geneva,sans-serif\'; color:#ffffff; background-color:transparent;\"><br /></span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Tahoma,Geneva,sans-serif\'; color:#ffffff; background-color:transparent;\">İstanbul\'un yeni ilçelerinden Başakşehir; Altınşehir, Şahintepe, Kayabaşı, Güvercintepe, Başakşehir, Başak, Ziya Gökalp,  Bahçeşehir 1. Kısım, Bahçeşehir 2. Kısım Mahalleleri ve Şamlar Köyü\'nden oluşmaktadır.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Tahoma,Geneva,sans-serif\'; color:#ffffff; background-color:transparent;\"><br /></span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Tahoma,Geneva,sans-serif\'; color:#ffffff; background-color:transparent;\">Başakşehir ilçesinin, Şahintepe, Kayabaşı, Şamlar, Güvercintepe, Altınşehir\'i içine alan bölgesinin bilinen en eski adı Azatlık\'dır. Bu isim, Şamlar Baruthanesi\'nde çalışan Ermenilerin Osmanlı yönetimince 1. Sınıf vatandaş sayılması ile azat edilenlerin yeri manasında, bölgenin Azatlık olarak adlandırılmasından gelmektedir. Meşrutiyetin ilanından sonra Arnavut Kökenli Resneli Niyazi Bey bölgedeki Ermenileri göndererek arazinin sahibi olmuştur. Bu dönemde ismi geçen bölgelerin tamamı için Resneli Çiftliği ismi kullanılmıştır. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Tahoma,Geneva,sans-serif\'; color:#ffffff; background-color:transparent;\"><br /></span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Tahoma,Geneva,sans-serif\'; color:#ffffff; background-color:transparent;\">İlçede bulunan ve en sağlıklı biçimde günümüze ulaşan eser Resneli Çiftliği\'dir. Baruthane binaları ve etrafındaki arazi Meşrutiyet yıllarında Hazine-i Hassa\'dan Resneli Niyazi Bey ailesine geçmiş ve 1950 yıllarına kadar Resneliler Çiftliği adıyla bu aile mülkiyetinde kalmıştır. Son sahibinin 1952\'ye doğru ölümü üzerine mirasçılar arasında paylaşılarak ayrı ayrı parsellenip satılmış, yerlerine modern siteler yapılmaya başlanmıştır.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Tahoma,Geneva,sans-serif\'; color:#ffffff; background-color:transparent;\"><br /></span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Tahoma,Geneva,sans-serif\'; color:#ffffff; background-color:transparent;\">İstanbul\'daki bilinen ilk yerleşim yeri olan Yarımburgaz, halk arasında bilinen popüler adıyla Altınşehir Mağarası, İstanbul\'dan 22 Km. kadar uzaklıktadır. Halkalı yakınlarındaki Altınşehir mevkiinde, kayalık bir tepenin bayırında Kayabaşı yolu üzerinde yer alan mağarada alt paleotik çağa ait kalıntılar ve Bizans dönemine ait bir kilise kalıntısı bulunmakla birlikte bu kalıntılar zamanla tahribata uğramıştır. Mağaranın güneyindeki, taş ocakları yarığı birçok yerli sinema filmine mekân olmuştur. Şamlar Bendi ve Baruthanesi, Osmanlı döneminde yapılmış ve günümüze gelmeyi başarmıştır.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Tahoma,Geneva,sans-serif\'; color:#ffffff; background-color:transparent;\"><br /></span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Tahoma,Geneva,sans-serif\'; color:#ffffff; background-color:transparent;\">Azatlı Baruthanesi ve Şamlar Bendi, Altınşehir / Yarımburgaz Mağaraları, Resneli Çiftliği bölgedeki tarihi mekânlardır. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Tahoma,Geneva,sans-serif\'; color:#ffffff; background-color:transparent;\"><br /></span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Tahoma,Geneva,sans-serif\'; color:#ffffff; background-color:transparent;\">İlçede zamanında bir Bulgar\'ın çiftliği olan Hoşdere (o zamanki adı Bojdar), Türk-Rus Savaşı\'nda (93 Harbi) Bulgaristan\'dan kaçan üç haneli bir Türk aileye ev sahipliği yapar. Bir müddet sonra o üç aile şimdiki Boğazköy tarafından toprak satın almaya başlar. 1923-1927 yılları arasında mübadele olur. Bulgaristan ve Yunanistan\'dan yaklaşık 30 aile ile Romanya\'dan bir iki aile muhacir gelir. Köyün yüzde 90-95\' i muhacirlere dağıtılır. Bojdar, bu dönemden 2. Dünya Savaşı\' nın hüküm sürdüğü yıllara kadar Boşdere daha sonra da Hoşdere olarak anılır.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Tahoma,Geneva,sans-serif\'; color:#ffffff; background-color:transparent;\"><br /></span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Tahoma,Geneva,sans-serif\'; color:#ffffff; background-color:transparent;\">&quot;Ispartakule Mekii&quot; diye bilinen bölge ise; İstanbul\'u Avrupa\'ya bağlayan tren yolunun Halkalı\'dan sonraki istasyona verilen &quot;Ispartakule İstasyonu&quot;, &quot;Ispartakule Viyadüğü&quot; ve &quot;Ispartakule Çiftliği&quot; olarak karşımıza çıkmaktadır. Fakat yapılan araştırmalarda, &quot;Belgrad-İstanbul Yolu&quot; olarak bilinen yolun üzerinde de bu isimlere rastlandığı görülmektedir.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Tahoma,Geneva,sans-serif\'; color:#ffffff; background-color:transparent;\"><br /></span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Tahoma,Geneva,sans-serif\'; color:#ffffff; background-color:transparent;\">Bölgede çeşitli zamanlarda yapılmış olan araştırmalar, Bahçeşehir çevresinde prehistorik dönemlerden başlayıp günümüze kadar gelen önemli buluntuların varlığınıda ortaya koymaktadır. İstanbul Arkeoloji Müzeleri Müdürlüğü\'nce yapılmış olan bir kazıda, şu anki Yamaç Villaları\'nın olduğu bölgede; Roma dönemine ait, kayaya oyulmuş Kaya Mezarları\'nın varlığı tespit edilmiştir. Ancak eldeki bulgulara dayanılarak; mezara çevrilmeden önceki dönemlerde bu kaya oyuğunun prehistorik dönemlerde kullanıldığı sanılmaktadır.</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
