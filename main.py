from calender_form import Ui_Calender
from calender_gui import Ui_Dialog
from calender_form1 import Ui_Calender1
from calender_gui1 import Ui_Dialog1
from sure import Ui_sure
from sure1 import Ui_sure1
from User_Auth import Authenticate
from User_Update import Leave_Mechanism
from Delete_Unamed import DEL
from UserTeamLeave import TeamLeaveInfo
from User_Leave import LeaveRemain
from User_CrossCheck import CrossCheck
from User_Email import Email
from User_ForgetPass import ForgetPass
from User_NewPassword import NewPassword
from User_PasswordComplexity import PasswordComplexity
from User_LeaveColor import LeaveColor
from deleteleave import Delete_leave

from otp import Ui_OTP
from newPass import Ui_newp
from otp1 import Ui_OTP1
from newpass1 import Ui_newp1
from main2 import SplashScreen
from PyQt5.QtWidgets import (QApplication, QWidget, QMessageBox)
from PyQt5.QtGui import QPalette, QTextCharFormat
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QCalendarWidget
from PyQt5 import QtGui
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
import sys

class FinalProduct(qtw.QWidget):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.ui = Ui_Dialog1()
		self.ui.setupUi(self)

		self.ui.lightmode.clicked.connect(self.light)

		self.ui.login_button.clicked.connect(self.authenticate1)
		self.ui.cancel_button.clicked.connect(self.cancelButton)
		self.ui.forgetpass_button.clicked.connect(self.forget1)
		self.close()

	def light(self):

		self.li = qtw.QDialog()
		self.uii = Ui_Dialog()
		self.uii.setupUi(self.li)
		self.li.show()

		self.uii.darkmade.clicked.connect(self.dark)
		self.uii.login_button.clicked.connect(self.authenticate)
		self.uii.cancel_button.clicked.connect(self.cancelButton)
		self.uii.forgetpass_button.clicked.connect(self.forget)
		self.close()

	def dark(self):
		self.li = qtw.QDialog()
		self.ui = Ui_Dialog1()
		self.ui.setupUi(self.li)
		self.li.show()
		self.ui.lightmode.clicked.connect(self.light)

		self.ui.login_button.clicked.connect(self.authenticate1)
		self.ui.cancel_button.clicked.connect(self.cancelButton)
		self.ui.forgetpass_button.clicked.connect(self.forget1)
		self.close()


	#def closeEvent(self, event):
		#reply = QMessageBox.question(self, 'Window Close', 'Are you sure you want to close the window?',
		#		QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

		#if reply == QMessageBox.Yes:
		#	event.accept()
		#	print('Window closed')
		#else:
		#	event.ignore()

		
	def forget1(self):
		self.fpass = qtw.QDialog()
		self.OTP = Ui_OTP1()
		self.OTP.setupUi(self.fpass)
		self.fpass.show()

		self.OTP.sendotp.clicked.connect(self.randomint1)
		self.OTP.cancel.clicked.connect(self.cancelButton)

	def randomint1(self):
		self.usid=self.OTP.userid.text()
		try:
			if not self.usid:
				qtw.QMessageBox.critical(self, "Fail", "Please Enter UserID")
			elif int(self.usid):
				x=ForgetPass(self.usid)
				self.ran=x.fetch_pass()
				self.OTP.ok.clicked.connect(self.confirm1)
				self.OTP.cancel.clicked.connect(self.cancelButton)
		except:
			qtw.QMessageBox.critical(self, "Fail", "Enter Correct Userid")

	def confirm1(self):
		
		pla = self.OTP.otp.text()
		try:
			if not pla:
				qtw.QMessageBox.critical(self, "Fail", "Please Enter OTP")
			elif int(pla) == self.ran:
				self.fpass1 = qtw.QDialog()
				self.OTP1 = Ui_newp1()
				self.OTP1.setupUi(self.fpass1)
				self.fpass1.show()
				self.OTP1.ok.clicked.connect(self.checked1)
				self.OTP1.cancel.clicked.connect(self.cancelButton)
			else:
				qtw.QMessageBox.critical(self, "Fail", "Wrong OTP Entered")
				return
		except:
			qtw.QMessageBox.critical(self, "Fail", "Wrong OTP Entered")


	def checked1(self):
		self.x1=self.OTP1.pass1.text()
		self.x2=self.OTP1.pass2.text()

		yy=PasswordComplexity(self.x1)
		xy=yy.checkcomplexity()
		print(xy)
		if not xy[0]:
			qtw.QMessageBox.critical(self, "Fail",str(xy[1]))	
			return


		if not self.x1 or not self.x2:
			qtw.QMessageBox.critical(self, "Fail","Please Fill both entries ")
			return
		elif self.x1 == self.x2:
			##Enter password updation code
			xx=NewPassword(int(self.usid), str(self.x1))
			xx.change_pswd()
			print("valid password set")
			qtw.QMessageBox.information(self, "Success","Password is set ")
			x=ForgetPass(self.usid)
			x.reset_password()
			self.fpass.close()
			self.fpass1.close()
		else:
			qtw.QMessageBox.critical(self, "Fail","Please Fill Same Password in both entries ")
			return
#### forget password
	def forget(self):
		self.fpass = qtw.QDialog()
		self.OTP = Ui_OTP()
		self.OTP.setupUi(self.fpass)
		self.fpass.show()

		self.OTP.sendotp.clicked.connect(self.randomint)
		self.OTP.cancel.clicked.connect(self.cancelButton)

	def randomint(self):
		self.usid=self.OTP.userid.text()
		try:
			if not self.usid:
				qtw.QMessageBox.critical(self, "Fail", "Please Enter UserID")
			elif int(self.usid):
				x=ForgetPass(self.usid)
				self.ran=x.fetch_pass()
				self.OTP.ok.clicked.connect(self.confirm)
				self.OTP.cancel.clicked.connect(self.cancelButton)
		except:
			qtw.QMessageBox.critical(self, "Fail", "Enter Correct Userid")

	def confirm(self):
		
		pla = self.OTP.otp.text()
		try:
			if not pla:
				qtw.QMessageBox.critical(self, "Fail", "Please Enter OTP")
			elif int(pla) == self.ran:
				self.fpass1 = qtw.QDialog()
				self.OTP1 = Ui_newp()
				self.OTP1.setupUi(self.fpass1)
				self.fpass1.show()
				self.OTP1.ok.clicked.connect(self.checked)
				self.OTP1.cancel.clicked.connect(self.cancelButton)
			else:
				qtw.QMessageBox.critical(self, "Fail", "Wrong OTP Entered")
				return
		except:
			qtw.QMessageBox.critical(self, "Fail", "Wrong OTP Entered")


	def checked(self):
		self.x1=self.OTP1.pass1.text()
		self.x2=self.OTP1.pass2.text()

		yy=PasswordComplexity(self.x1)
		xy=yy.checkcomplexity()
		print(xy)
		if not xy[0]:
			qtw.QMessageBox.critical(self, "Fail",str(xy[1]))	
			return


		if not self.x1 or not self.x2:
			qtw.QMessageBox.critical(self, "Fail","Please Fill both entries ")
			return
		elif self.x1 == self.x2:
			##Enter password updation code
			xx=NewPassword(int(self.usid), str(self.x1))
			xx.change_pswd()
			print("valid password set")
			qtw.QMessageBox.information(self, "Success","Password is set ")
			x=ForgetPass(self.usid)
			x.reset_password()
			self.fpass.close()
			self.fpass1.close()
		else:
			qtw.QMessageBox.critical(self, "Fail","Please Fill Same Password in both entries ")
			return

			
##### login button
	def authenticate(self):

		emai = self.uii.email_text.text()
		passwd = self.uii.pass_text.text()
		if not emai and not passwd:
			qtw.QMessageBox.critical(self, "Fail", "Enter your User id and Password")
			return
		try:
			if not emai:
				qtw.QMessageBox.critical(self, "Fail", "Enter User ID")
				return
			elif not passwd:
				qtw.QMessageBox.critical(self, "Fail", "Please enter your password")
				return
			elif int(emai):
		## Please add authentication part here
				aut = Authenticate(emai,passwd)
				self.x,name2 = aut.authenticate()
				print(self.x)
				if self.x:
				#if emai == 'karan' and passwd == 'karan':
					self.Calender = qtw.QDialog()
					self.calen = Ui_Calender()
					self.calen.setupUi(self.Calender)
					self.Calender.show()
					x=LeaveRemain(emai)
					leaveBal = x.leave_remain()
					self.calen.welcome.setText("Welcome "+ name2)
					self.calen.leaveBalance.setText(leaveBal)
					self.calen.submit_2.clicked.connect(self.submitButton)
					self.calen.dele.clicked.connect(self.deleButton)
					self.calen.cancel_3.clicked.connect(self.cancelButton)
					self.calen.check_button_2.clicked.connect(self.checkButton)
				else:
					qtw.QMessageBox.critical(self, "Fail", "Incorrect Password. Click Forget password")
					return
			else:
				qtw.QMessageBox.critical(self, "Fail", "Incorrect Login information. Click Forget password")
				return
		except Exception:
			print(Exception)
			qtw.QMessageBox.critical(self, "Fail", "Entered Wrong User ID")
			return
		self.li.close()
	def authenticate1(self):

		emai = self.ui.email_text.text()
		passwd = self.ui.pass_text.text()
		if not emai and not passwd:
			qtw.QMessageBox.critical(self, "Fail", "Enter your User id and Password")
			return
		try:
			if not emai:
				qtw.QMessageBox.critical(self, "Fail", "Enter User ID")
				return
			elif not passwd:
				qtw.QMessageBox.critical(self, "Fail", "Please enter your password")
				return
			elif int(emai):
		## Please add authentication part here
				aut = Authenticate(emai,passwd)
				self.x,name2 = aut.authenticate()
				if self.x:
				#if emai == 'karan' and passwd == 'karan':
					self.Calender = qtw.QDialog()
					self.calen = Ui_Calender1()
					self.calen.setupUi(self.Calender)
					self.Calender.show()
					x=LeaveRemain(emai)
					leaveBal = x.leave_remain()
					self.calen.welcome.setText("Welcome "+ name2)
					self.calen.leaveBalance.setText(leaveBal)
					self.calen.submit_2.clicked.connect(self.submitButton1)
					self.calen.dele.clicked.connect(self.deleButton)
					self.calen.cancel_3.clicked.connect(self.cancelButton)
					self.calen.check_button_2.clicked.connect(self.checkButton)
				else:
					qtw.QMessageBox.critical(self, "Fail", "Incorrect Password. Click Forget password")
					return
			else:
				qtw.QMessageBox.critical(self, "Fail", "Incorrect Login information. Click Forget password")
				return
		except:
			qtw.QMessageBox.critical(self, "Fail", "Entered Wrong User ID")
			return
		self.close()

	def deleButton(self):

		date = str(self.calen.calendar_3.selectedDate())
		date = date[18:][1:-1]
		date = date.split(",")[::-1]
		d1=date[0].replace(" ","")
		d2=date[1].replace(" ","")
		if len(d1)==1: d1='0'+d1
		
		if len(d2)==1: d2='0'+d2
		self.date = d1+"-"+d2+"-"+date[2]
		xc=Delete_leave(self.x,self.date)
		d=xc.delete()
		if d==1:
			qtw.QMessageBox.information(self, "Success","Leave is deleted")
			f=ForgetPass(self.x)
			f.delete_lev()
		elif d==2:
			qtw.QMessageBox.critical(self,"Fail","You have no leave on this day")
		elif d==3:
			qtw.QMessageBox.critical(self,"Fail","You Cannot delete past leaves")

		x=LeaveRemain(self.x)
		leaveBal = x.leave_remain()
		self.calen.leaveBalance.setText(leaveBal)

## cancel button
	def cancelButton(self):
		sys.exit()
	def submitButton1(self):
		#self.calen.calendar_1.selectionChanged.connect(self.onSelectionChanged)
		date = str(self.calen.calendar_3.selectedDate())
		date = date[18:][1:-1]
		date = date.split(",")[::-1]
		d1=date[0].replace(" ","")
		d2=date[1].replace(" ","")
		if len(d1)==1: d1='0'+d1
		
		if len(d2)==1: d2='0'+d2
		self.date = d1+"-"+d2+"-"+date[2]

		self.event_title = self.calen.event_name_2.text()
		self.event_discription = self.calen.event_detail_2.text()
		self.combo_op = self.calen.event_combo_2.currentText()
		self.combo_days = self.calen.days_combo_3.currentText()
		
		print(int(self.combo_days[:2]))
		print(self.combo_days,",",self.event_title, ",",self.event_discription,",", self.combo_op,",",self.date)
		## cross check
		if not self.event_title:
			qtw.QMessageBox.warning(self, "Warning","Please Enter The Reason for Leave")
		elif self.combo_op == "other" and not self.event_discription:
			qtw.QMessageBox.warning(self, "Warning","Please Enter The Discription for Leave")
		else:
			cc = CrossCheck(self.x, self.date, int(self.combo_days[:2]))
			xxx=cc.checkPrev()
			if xxx==True:  ## for correct date
				msg=cc.check_team()
				if msg != -1:
					qtw.QMessageBox.critical(self, "Warning", msg)


				self.S = qtw.QDialog()
				self.c = Ui_sure1()
				self.c.setupUi(self.S)
				self.S.show()

				self.c.yeah.clicked.connect(self.areUSure)
				self.c.nah.clicked.connect(self.notSure)

			else:
				qtw.QMessageBox.warning(self, "Warning", "Cant Apply Leave on Previous dates or on Public holidays")

	def submitButton(self):
		#self.calen.calendar_1.selectionChanged.connect(self.onSelectionChanged)
		date = str(self.calen.calendar_3.selectedDate())
		date = date[18:][1:-1]
		date = date.split(",")[::-1]
		d1=date[0].replace(" ","")
		d2=date[1].replace(" ","")
		if len(d1)==1: d1='0'+d1
		
		if len(d2)==1: d2='0'+d2
		self.date = d1+"-"+d2+"-"+date[2]

		self.event_title = self.calen.event_name_2.text()
		self.event_discription = self.calen.event_detail_2.text()
		self.combo_op = self.calen.event_combo_2.currentText()
		self.combo_days = self.calen.days_combo_3.currentText()
		
		print(int(self.combo_days[:2]))
		print(self.combo_days,",",self.event_title, ",",self.event_discription,",", self.combo_op,",",self.date)
		## cross check
		if not self.event_title:
			qtw.QMessageBox.warning(self, "Warning","Please Enter The Reason for Leave")
		elif self.combo_op == "other" and not self.event_discription:
			qtw.QMessageBox.warning(self, "Warning","Please Enter The Discription for Leave")
		else:
			cc = CrossCheck(self.x, self.date, int(self.combo_days[:2]))
			xxx=cc.checkPrev()
			if xxx==True:  ## for correct date
				msg=cc.check_team()
				if msg != -1:
					qtw.QMessageBox.critical(self, "Warning", msg)


				self.S = qtw.QDialog()
				self.c = Ui_sure()
				self.c.setupUi(self.S)
				self.S.show()

				self.c.yeah.clicked.connect(self.areUSure)
				self.c.nah.clicked.connect(self.notSure)

			else:
				qtw.QMessageBox.warning(self, "Warning", "Cant Apply Leave on Previous dates")
			
	def areUSure(self):
		upd = Leave_Mechanism(self.combo_op, self.date , self.event_discription, int(self.combo_days[:2]), self.x )
		self.NOD=upd.update()
		print(self.NOD)
		if not type(self.NOD) == int: 
			qtw.QMessageBox.critical(self, "Warning", self.NOD)
		else:
			em = Email(self.x, self.date, int(self.combo_days[:2]))
			em.fetch_mail()
		d = DEL()
		d.del_unamed()
		d.del_unamed2()
		x=LeaveRemain(self.x)
		leaveBal = x.leave_remain()
		self.calen.leaveBalance.setText(leaveBal)
		self.S.close()
	def notSure(self):
		self.S.close()

	def checkButton(self):

		date = str(self.calen.calendar_3.selectedDate())
		date = date[18:][1:-1]
		date = date.split(",")[::-1]
		d1=date[0].replace(" ","")
		d2=date[1].replace(" ","")
		if len(d1)==1: d1='0'+d1
		
		if len(d2)==1: d2='0'+d2
		date = d1+"-"+d2+"-"+date[2]
		print(date,"---------")
		nod = self.calen.days_combo_4.currentText()
		if nod == "Select number of days": nod = 1
		else: nod=int(str(nod[:2]))
		leave = TeamLeaveInfo(self.x, date, nod)
		op= leave.display()
		if len(op) == 0 :
			self.calen.event_list_3.setText("No one is on leave")
		if len(op) >= 1:
			self.calen.event_list_3.setText(op[0])
		for i in op[1:]:
			self.calen.event_list_3.append(i)
		#self.calen.event_list_1.setText(combo_days+","+event_title+ ","+event_discription+","+ combo_op+","+date)
		#self.calen.event_list_1.append(combo_days+","+event_title+ ","+event_discription+","+ combo_op+","+date)

 
if __name__ == "__main__":
    
    app = qtw.QApplication(sys.argv)
    #Dialog = qtw.QDialog()

    widget = FinalProduct()
    widget.show()
    SplashScreen()
    sys.exit(app.exec_())
