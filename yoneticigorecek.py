# Form implementation generated from reading ui file 'yoneticigörecek.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class yoneticigorecek(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(633, 481)
        Form.setStyleSheet("#Form{\n"
"border-image: url(:/a/tamir3.jpg);\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(parent=Form)
        self.widget.setMinimumSize(QtCore.QSize(523, 463))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_2 = QtWidgets.QWidget(parent=self.widget)
        self.widget_2.setMinimumSize(QtCore.QSize(505, 445))
        self.widget_2.setObjectName("widget_2")
        self.yapilanislemler = QtWidgets.QLineEdit(parent=self.widget_2)
        self.yapilanislemler.setGeometry(QtCore.QRect(190, 240, 141, 31))
        self.yapilanislemler.setObjectName("yapilanislemler")
        self.logo = QtWidgets.QLabel(parent=self.widget_2)
        self.logo.setGeometry(QtCore.QRect(160, 90, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(20)
        font.setBold(False)
        self.logo.setFont(font)
        self.logo.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(85, 83, 84, 255), stop:1 rgba(255, 255, 255,110));")
        self.logo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.logo.setWordWrap(True)
        self.logo.setObjectName("logo")
        self.kaydet = QtWidgets.QPushButton(parent=self.widget_2)
        self.kaydet.setGeometry(QtCore.QRect(220, 330, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        self.kaydet.setFont(font)
        self.kaydet.setStyleSheet("QPushButton#kaydet{\n"
"    background-color: rgb(255, 255, 0);\n"
"    background-color: rgb(0, 126, 189);\n"
"\n"
"}\n"
"\n"
"QPushButton#kaydet:pressed{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.kaydet.setObjectName("kaydet")
        self.plakagirin = QtWidgets.QLineEdit(parent=self.widget_2)
        self.plakagirin.setGeometry(QtCore.QRect(190, 160, 141, 31))
        self.plakagirin.setObjectName("plakagirin")
        self.siragir = QtWidgets.QLineEdit(parent=self.widget_2)
        self.siragir.setGeometry(QtCore.QRect(190, 200, 141, 31))
        self.siragir.setObjectName("siragir")
        self.widget_3 = QtWidgets.QWidget(parent=self.widget_2)
        self.widget_3.setGeometry(QtCore.QRect(0, 0, 521, 461))
        self.widget_3.setStyleSheet("")
        self.widget_3.setObjectName("widget_3")
        self.tutar = QtWidgets.QLineEdit(parent=self.widget_2)
        self.tutar.setGeometry(QtCore.QRect(190, 280, 141, 31))
        self.tutar.setObjectName("tutar")
        self.widget_3.raise_()
        self.logo.raise_()
        self.plakagirin.raise_()
        self.siragir.raise_()
        self.yapilanislemler.raise_()
        self.tutar.raise_()
        self.kaydet.raise_()
        self.verticalLayout_2.addWidget(self.widget_2)
        self.verticalLayout.addWidget(self.widget, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.plakagirin, self.siragir)
        Form.setTabOrder(self.siragir, self.yapilanislemler)
        Form.setTabOrder(self.yapilanislemler, self.tutar)
        Form.setTabOrder(self.tutar, self.kaydet)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.yapilanislemler.setPlaceholderText(_translate("Form", "Yapılan İşlem(leri) Girin"))
        self.logo.setText(_translate("Form", "AY- CAR- TAKS"))
        self.kaydet.setText(_translate("Form", "KAYDET"))
        self.plakagirin.setPlaceholderText(_translate("Form", "Plakayı Girin"))
        self.siragir.setPlaceholderText(_translate("Form", "Sırasını Girin"))
        self.tutar.setPlaceholderText(_translate("Form", "Tutar Girin"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = yoneticigorecek()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
