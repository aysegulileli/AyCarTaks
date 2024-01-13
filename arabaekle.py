# Form implementation generated from reading ui file 'arabaekle.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class arabaekle(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(620, 469)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(602, 451))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        self.widget.setFont(font)
        self.widget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(85, 83, 84, 255), stop:1 rgba(255, 255, 255,110));")
        self.widget.setObjectName("widget")
        self.plaka = QtWidgets.QLineEdit(parent=self.widget)
        self.plaka.setGeometry(QtCore.QRect(210, 120, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        self.plaka.setFont(font)
        self.plaka.setText("")
        self.plaka.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.plaka.setObjectName("plaka")
        self.sira = QtWidgets.QLineEdit(parent=self.widget)
        self.sira.setGeometry(QtCore.QRect(212, 180, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        self.sira.setFont(font)
        self.sira.setText("")
        self.sira.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.sira.setObjectName("sira")
        self.kaydet = QtWidgets.QPushButton(parent=self.widget)
        self.kaydet.setGeometry(QtCore.QRect(260, 240, 121, 41))
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
        self.verticalLayout.addWidget(self.widget, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.plaka.setPlaceholderText(_translate("Form", "Plaka"))
        self.sira.setPlaceholderText(_translate("Form", "Sırası"))
        self.kaydet.setText(_translate("Form", "Kaydet"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())