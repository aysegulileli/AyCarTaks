# Form implementation generated from reading ui file 'musteri.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class musteri(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(550, 450)
        Form.setMinimumSize(QtCore.QSize(550, 450))
        Form.setMaximumSize(QtCore.QSize(16777215, 16777215))
        Form.setStyleSheet("#Form{\n"
"border-image: url(:/a/tamir3.jpg);}\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, -1, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(parent=Form)
        self.widget.setMinimumSize(QtCore.QSize(541, 450))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        self.widget.setFont(font)
        self.widget.setObjectName("widget")
        self.logo = QtWidgets.QLabel(parent=self.widget)
        self.logo.setGeometry(QtCore.QRect(10, 80, 201, 291))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(46)
        font.setBold(False)
        self.logo.setFont(font)
        self.logo.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(85, 83, 84, 255), stop:1 rgba(255, 255, 255,110));")
        self.logo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.logo.setWordWrap(True)
        self.logo.setObjectName("logo")
        self.plaka2 = QtWidgets.QLineEdit(parent=self.widget)
        self.plaka2.setGeometry(QtCore.QRect(230, 180, 151, 41))
        self.plaka2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.plaka2.setText("")
        self.plaka2.setObjectName("plaka2")
        self.dogrulamakodu = QtWidgets.QLineEdit(parent=self.widget)
        self.dogrulamakodu.setGeometry(QtCore.QRect(230, 230, 91, 31))
        self.dogrulamakodu.setStyleSheet("background-color: rgb(236, 236, 176);")
        self.dogrulamakodu.setObjectName("dogrulamakodu")
        self.kodugir = QtWidgets.QLineEdit(parent=self.widget)
        self.kodugir.setGeometry(QtCore.QRect(330, 230, 171, 31))
        self.kodugir.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.kodugir.setObjectName("kodugir")
        self.sorgula = QtWidgets.QPushButton(parent=self.widget)
        self.sorgula.setGeometry(QtCore.QRect(390, 180, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        self.sorgula.setFont(font)
        self.sorgula.setStyleSheet("QPushButton#sorgula{\n"
"    background-color: rgb(0, 77, 116);\n"
"    background-color: rgb(0, 126, 189);\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton#sorgula:pressed{\n"
"    background-color: rgb(236, 236, 176);\n"
"}")
        self.sorgula.setObjectName("sorgula")
        self.yoneticiGirisButon = QtWidgets.QPushButton(parent=self.widget)
        self.yoneticiGirisButon.setGeometry(QtCore.QRect(450, 20, 91, 41))
        self.yoneticiGirisButon.setStyleSheet("QPushButton#yoneticiGirisButon{\n"
"    background-color: rgb(0, 77, 116);\n"
"    background-color: rgb(0, 126, 189);\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton#yoneticiGirisButon:pressed{\n"
"    background-color: rgb(236, 236, 176);\n"
"}")
        self.yoneticiGirisButon.setObjectName("yoneticiGirisButon")
        self.logo.raise_()
        self.dogrulamakodu.raise_()
        self.kodugir.raise_()
        self.sorgula.raise_()
        self.plaka2.raise_()
        self.yoneticiGirisButon.raise_()
        self.gormewidget = QtWidgets.QWidget(parent=Form)
        self.gormewidget.setMinimumSize(QtCore.QSize(581, 417))
        self.gormewidget.setObjectName("gormewidget")
        self.plakagörme = QtWidgets.QLabel(parent=self.gormewidget)
        self.plakagörme.setGeometry(QtCore.QRect(200, 160, 141, 31))
        self.plakagörme.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.plakagörme.setObjectName("plakagörme")
        self.logo2 = QtWidgets.QLabel(parent=self.gormewidget)
        self.logo2.setGeometry(QtCore.QRect(170, 90, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(20)
        font.setBold(False)
        self.logo2.setFont(font)
        self.logo2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(85, 83, 84, 255), stop:1 rgba(255, 255, 255,110));")
        self.logo2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.logo2.setWordWrap(True)
        self.logo2.setObjectName("logo2")
        self.sirasi = QtWidgets.QLabel(parent=self.gormewidget)
        self.sirasi.setGeometry(QtCore.QRect(200, 200, 141, 31))
        self.sirasi.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.sirasi.setObjectName("sirasi")
        self.yapilanislemler = QtWidgets.QLabel(parent=self.gormewidget)
        self.yapilanislemler.setGeometry(QtCore.QRect(200, 240, 141, 31))
        self.yapilanislemler.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.yapilanislemler.setObjectName("yapilanislemler")
        self.tutar = QtWidgets.QLabel(parent=self.gormewidget)
        self.tutar.setGeometry(QtCore.QRect(200, 280, 141, 31))
        self.tutar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tutar.setObjectName("tutar")
        self.gormewidget.setHidden(True)
        self.verticalLayout.addWidget(self.widget, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.logo.setText(_translate("Form", "AY- CAR- TAKS"))
        self.plaka2.setPlaceholderText(_translate("Form", "Plakanizi Giriniz"))
        self.dogrulamakodu.setPlaceholderText(_translate("Form", "Doğrulama Kodu "))
        self.kodugir.setPlaceholderText(_translate("Form", "Doğrulama Kodununu Giriniz"))
        self.sorgula.setText(_translate("Form", "SORGULA"))
        self.yoneticiGirisButon.setText(_translate("Form", "Yönetici Girişi"))
        self.plakagörme.setText(_translate("Form", "plakagörme"))
        self.logo2.setText(_translate("Form", "AY- CAR- TAKS"))
        self.sirasi.setText(_translate("Form", "Sırası"))
        self.yapilanislemler.setText(_translate("Form", "Yapılan İşlemler"))
        self.tutar.setText(_translate("Form", "Tutar"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = musteri()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
