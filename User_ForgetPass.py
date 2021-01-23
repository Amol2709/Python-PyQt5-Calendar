class ForgetPass:
    def __init__(self,emp_id):
        self.emp_id = emp_id
        #self.leave_date = leave_date
        #self.days = days
    def reset_password(self):
        import win32com.client as client
        import pandas as pd

        def get_content2():

            password_content ="""
        Hi """+name+""",

        Your  Password has been reset Successfully!!.


        Regards,

        Administrator

        This is System Generated Mail.Please Do not Reply.
            """

            return password_content

        DF = pd.read_excel("emp_ex.xlsx")
        print(self.emp_id)
        print(type(self.emp_id))
        df = DF[DF['EmpID']==int(self.emp_id)]
        email = list(df['EmailID'])[0]
        print(email)



        name = list(df['Username'])[0]
        #d1 = datetime.datetime.strptime(self.leave_date, '%d-%m-%Y') + datetime.timedelta(days=int(self.days)-1)
        #to_date=d1.strftime('%d-%m-%Y')
        outlook = client.Dispatch("Outlook.Application")
        m = outlook.CreateItem(0)
        m.Display()
        # setup the parameters of the message
        m.To = email
        m.Subject = "Successfully Reset Password"
        m.Body = get_content2()
        # Sending the mail
        m.Save()
        m.Send()


    def delete_lev(self):
        import win32com.client as client
        import pandas as pd

        def get_content2():

            password_content ="""
        Hi """+name+""",

        Your  Leave has been deleted Successfully!!.


        Regards,

        Administrator

        This is System Generated Mail.Please Do not Reply.
            """

            return password_content

        DF = pd.read_excel("emp_ex.xlsx")
        print(self.emp_id)
        print(type(self.emp_id))
        df = DF[DF['EmpID']==int(self.emp_id)]
        email = list(df['EmailID'])[0]
        print(email)



        name = list(df['Username'])[0]
        #d1 = datetime.datetime.strptime(self.leave_date, '%d-%m-%Y') + datetime.timedelta(days=int(self.days)-1)
        #to_date=d1.strftime('%d-%m-%Y')
        outlook = client.Dispatch("Outlook.Application")
        m = outlook.CreateItem(0)
        m.Display()
        # setup the parameters of the message
        m.To = email
        m.Subject = "Successfully deleted leave"
        m.Body = get_content2()
        # Sending the mail
        m.Save()
        m.Send()





    def fetch_pass(self):
        import pandas as pd
        import win32com.client as client
        
        import random
        r=random.randint(300000, 1000000)
        
        def get_content():

            password_content ="""
        Hi """+name+""",

        Your  OTP To Reset Password is  {}.


        Regards,

        Leave Administrator
            """.format(r)

            return password_content

        
        
        DF = pd.read_excel("emp_ex.xlsx")
        print(self.emp_id)
        print(type(self.emp_id))
        df = DF[DF['EmpID']==int(self.emp_id)]
        email = list(df['EmailID'])[0]
        print(email)
        name = list(df['Username'])[0]
        #d1 = datetime.datetime.strptime(self.leave_date, '%d-%m-%Y') + datetime.timedelta(days=int(self.days)-1)
        #to_date=d1.strftime('%d-%m-%Y')
        outlook = client.Dispatch("Outlook.Application")
        m = outlook.CreateItem(0)
        m.Display()
        # setup the parameters of the message
        m.To = email
        m.Subject = "OTP Generated"
        m.Body = get_content()
        # Sending the mail
        m.Save()
        m.Send()
        return r
        
        
#obj=Email(10671102,'29-09-2020',4)
#obj.fetch_mail()      
        
        
        