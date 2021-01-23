# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newpass.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_newp(object):
    def setupUi(self, newp):
        newp.setObjectName("newp")
        newp.resize(400, 250)
        self.pass1 = QtWidgets.QLineEdit(newp)
        self.pass1.setGeometry(QtCore.QRect(60, 40, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pass1.setFont(font)
        self.pass1.setText("")
        self.pass1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass1.setObjectName("pass1")
        self.pass2 = QtWidgets.QLineEdit(newp)
        self.pass2.setGeometry(QtCore.QRect(60, 80, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pass2.setFont(font)
        self.pass2.setText("")
        self.pass2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass2.setObjectName("pass2")
        self.ok = QtWidgets.QPushButton(newp)
        self.ok.setGeometry(QtCore.QRect(40, 180, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ok.setFont(font)
        self.ok.setStyleSheet("background: rgb(141, 209, 104);\n"
"color: rgb(255,255,255)")
        self.ok.setObjectName("ok")
        self.cancel = QtWidgets.QPushButton(newp)
        self.cancel.setGeometry(QtCore.QRect(250, 180, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cancel.setFont(font)
        self.cancel.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"background:rgb(126, 143, 255);")
        self.cancel.setObjectName("cancel")

        self.retranslateUi(newp)
        QtCore.QMetaObject.connectSlotsByName(newp)

    def retranslateUi(self, newp):
        _translate = QtCore.QCoreApplication.translate
        newp.setWindowTitle(_translate("newp", "Set New Password"))
        self.pass1.setPlaceholderText(_translate("newp", "Enter new password"))
        self.pass2.setPlaceholderText(_translate("newp", "Renter new password"))
        self.ok.setText(_translate("newp", "OK"))
        self.cancel.setText(_translate("newp", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    newp = QtWidgets.QDialog()
    ui = Ui_newp()
    ui.setupUi(newp)
    newp.show()
    sys.exit(app.exec_())