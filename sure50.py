

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_sure50(object):
    def setupUi(self, sure50):
        sure50.setObjectName("sure50")
        sure50.resize(400, 203)
        self.label = QtWidgets.QLabel(sure50)
        self.label.setGeometry(QtCore.QRect(30, 30, 341, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(sure50)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 361, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.yeah1 = QtWidgets.QPushButton(sure50)
        self.yeah1.setGeometry(QtCore.QRect(60, 140, 93, 28))
        self.yeah1.setObjectName("yeah1")
        self.nah2 = QtWidgets.QPushButton(sure50)
        self.nah2.setGeometry(QtCore.QRect(230, 140, 93, 28))
        self.nah2.setObjectName("nah2")

        self.retranslateUi(sure50)
        QtCore.QMetaObject.connectSlotsByName(sure50)

    def retranslateUi(self, sure50):
        _translate = QtCore.QCoreApplication.translate
        sure50.setWindowTitle(_translate("sure50", "Dialog"))
        self.label.setText(_translate("sure50", "More Than 50 % Of Team on Leave "))
        self.label_2.setText(_translate("sure50", "Are You sure You Want to take Leave?"))
        self.yeah1.setText(_translate("sure50", "Yes"))
        self.nah2.setText(_translate("sure50", "No"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    sure50 = QtWidgets.QDialog()
    ui = Ui_sure50()
    ui.setupUi(sure50)
    sure50.show()
    sys.exit(app.exec_())
