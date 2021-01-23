from main import FinalProduct
from PyQt5 import QtWidgets as qtw
import sys

class HelperMaining:
	def helper(self):
		app = qtw.QApplication(sys.argv)
		widget = FinalProduct()
		widget.show()
		sys.exit(app.exec_())


if __name__ == "__main__":
    
	x=HelperMain()
	x.helper()