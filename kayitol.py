# Form implementation generated from reading ui file 'kayıtol.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class kayitol(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(543, 487)
        Form.setStyleSheet("#Form{\n"
"border-image: url(:/a/tamir3.jpg);\n"
"}")
        self.widget = QtWidgets.QWidget(parent=Form)
        self.widget.setGeometry(QtCore.QRect(10, 10, 521, 471))
        self.widget.setObjectName("widget")
        self.logo = QtWidgets.QLabel(parent=self.widget)
        self.logo.setGeometry(QtCore.QRect(20, 80, 201, 291))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(46)
        font.setBold(False)
        font.setWeight(50)
        self.logo.setFont(font)
        self.logo.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(85, 83, 84, 255), stop:1 rgba(255, 255, 255,110));")
        self.logo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.logo.setWordWrap(True)
        self.logo.setObjectName("logo")
        self.kaydol = QtWidgets.QLabel(parent=self.widget)
        self.kaydol.setGeometry(QtCore.QRect(240, 60, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setBold(True)
        font.setWeight(75)
        self.kaydol.setFont(font)
        self.kaydol.setStyleSheet("background-color: rgba(240, 240, 240, 140);")
        self.kaydol.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.kaydol.setObjectName("kaydol")
        self.ad = QtWidgets.QLineEdit(parent=self.widget)
        self.ad.setGeometry(QtCore.QRect(240, 110, 121, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(False)
        font.setWeight(50)
        self.ad.setFont(font)
        self.ad.setObjectName("ad")
        self.soyad = QtWidgets.QLineEdit(parent=self.widget)
        self.soyad.setGeometry(QtCore.QRect(380, 110, 121, 22))
        self.soyad.setText("")
        self.soyad.setObjectName("soyad")
        self.eposta = QtWidgets.QLineEdit(parent=self.widget)
        self.eposta.setGeometry(QtCore.QRect(240, 140, 261, 22))
        self.eposta.setObjectName("eposta")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_4.setGeometry(QtCore.QRect(-180, 330, 113, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.yenisifre = QtWidgets.QLineEdit(parent=self.widget)
        self.yenisifre.setGeometry(QtCore.QRect(240, 170, 261, 22))
        self.yenisifre.setObjectName("yenisifre")
        self.yenisifretekrar = QtWidgets.QLineEdit(parent=self.widget)
        self.yenisifretekrar.setGeometry(QtCore.QRect(240, 200, 261, 22))
        self.yenisifretekrar.setObjectName("yenisifretekrar")
        self.cinsiyet = QtWidgets.QLabel(parent=self.widget)
        self.cinsiyet.setGeometry(QtCore.QRect(240, 240, 266, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setBold(True)
        font.setWeight(75)
        self.cinsiyet.setFont(font)
        self.cinsiyet.setStyleSheet("background-color: rgba(240, 240, 240, 140);")
        self.cinsiyet.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.cinsiyet.setObjectName("cinsiyet")
        self.kadin = QtWidgets.QRadioButton(parent=self.widget)
        self.kadin.setGeometry(QtCore.QRect(240, 270, 75, 24))
        self.kadin.setStyleSheet("QRadioButton#kadin{\n"
"    \n"
"    background-color: rgb(170, 170, 255);\n"
"\n"
"}\n"
"\n"
"QRadioButton#kadin:pressed{\n"
"    background-color: rgb(255, 170, 255);\n"
"    background-color: rgb(202, 202, 151);\n"
"}")
        self.kadin.setObjectName("kadin")
        self.erkek = QtWidgets.QRadioButton(parent=self.widget)
        self.erkek.setGeometry(QtCore.QRect(330, 270, 81, 24))
        self.erkek.setStyleSheet("QRadioButton#erkek{\n"
"    background-color: rgb(255, 255, 0);\n"
"    background-color: rgb(170, 170, 255)\n"
"\n"
"}\n"
"\n"
"QRadioButton#erkek:pressed{\n"
"    background-color: rgb(255, 170, 255);\n"
"    background-color: rgb(202, 202, 151);\n"
"}")
        self.erkek.setObjectName("erkek")
        self.ozel = QtWidgets.QRadioButton(parent=self.widget)
        self.ozel.setGeometry(QtCore.QRect(424, 270, 81, 24))
        self.ozel.setStyleSheet("QRadioButton#ozel{\n"
"    background-color: rgb(170, 170, 255);\n"
"    background-color: rgb(170, 170, 255)\n"
"\n"
"}\n"
"\n"
"QRadioButton#ozel:pressed{\n"
"    background-color: rgb(255, 170, 255);\n"
"    background-color: rgb(202, 202, 151);\n"
"}")
        self.ozel.setObjectName("ozel")
        self.kaydol_2 = QtWidgets.QPushButton(parent=self.widget)
        self.kaydol_2.setGeometry(QtCore.QRect(304, 313, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.kaydol_2.setFont(font)
        self.kaydol_2.setStyleSheet("QPushButton#kaydol_2{\n"
"    background-color: rgb(255, 255, 0);\n"
"    background-color: rgb(0, 126, 189);\n"
"\n"
"}\n"
"\n"
"QPushButton#kaydol_2:pressed{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.kaydol_2.setObjectName("kaydol_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.logo.setText(_translate("Form", "AY- CAR- TAKS"))
        self.kaydol.setText(_translate("Form", "KAYDOL"))
        self.ad.setPlaceholderText(_translate("Form", "Adın"))
        self.soyad.setPlaceholderText(_translate("Form", "Soyadın"))
        self.eposta.setPlaceholderText(_translate("Form", "E-posta "))
        self.yenisifre.setPlaceholderText(_translate("Form", "Yeni Şifre"))
        self.yenisifretekrar.setPlaceholderText(_translate("Form", "Yeni Şifreyi Girin"))
        self.cinsiyet.setText(_translate("Form", "Cinsiyet"))
        self.kadin.setText(_translate("Form", "Kadın"))
        self.erkek.setText(_translate("Form", "Erkek"))
        self.ozel.setText(_translate("Form", "Özel"))
        self.kaydol_2.setText(_translate("Form", "KAYDOL"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = kayitol()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
