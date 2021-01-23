from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_sure(object):
    def setupUi(self, sure):
        sure.setObjectName("sure")
        sure.resize(351, 163)
        self.yeah = QtWidgets.QPushButton(sure)
        self.yeah.setGeometry(QtCore.QRect(60, 110, 93, 28))
        self.yeah.setObjectName("yeah")
        self.nah = QtWidgets.QPushButton(sure)
        self.nah.setGeometry(QtCore.QRect(210, 110, 93, 28))
        self.nah.setObjectName("nah")
        self.label = QtWidgets.QLabel(sure)
        self.label.setGeometry(QtCore.QRect(110, 40, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(sure)
        QtCore.QMetaObject.connectSlotsByName(sure)

    def retranslateUi(self, sure):
        _translate = QtCore.QCoreApplication.translate
        sure.setWindowTitle(_translate("sure", "Dialog"))
        self.yeah.setText(_translate("sure", "Yes"))
        self.nah.setText(_translate("sure", "No"))
        self.label.setText(_translate("sure", "Are You Sure?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    sure = QtWidgets.QDialog()
    ui = Ui_sure()
    ui.setupUi(sure)
    sure.show()
    sys.exit(app.exec_())
