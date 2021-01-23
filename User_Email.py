class Email():
    def __init__(self,emp_id,leave_date,days):
        self.emp_id = emp_id
        self.leave_date = leave_date
        self.days = days
    
    def fetch_mail(self):
        import pandas as pd
        import datetime
        import win32com.client as client
        
        
        def get_content1():

            email_content ="""
        Hi """+name+""",

        Your  Earned Leave application for {}  has been submitted successfully.


        Regards,

        Leave Administrator
            """.format(self.leave_date)

            return email_content
        
        def get_content():

            email_content ="""
        Hi """+name+""",

        Your  Earned Leave application from {}  to {} have been submitted successfully.


        Regards,

        Leave Administrator
            """.format(self.leave_date,to_date)

            return email_content

        
        
        DF = pd.read_excel("emp_ex.xlsx")
        df = DF[DF['EmpID']==int(self.emp_id)]
        email = list(df['EmailID'])[0]
        print(email)
        name = list(df['Username'])[0]
        d1 = datetime.datetime.strptime(self.leave_date, '%d-%m-%Y') + datetime.timedelta(days=int(self.days)-1)
        to_date=d1.strftime('%d-%m-%Y')
        outlook = client.Dispatch("Outlook.Application")
        m = outlook.CreateItem(0)
        m.Display()
        # setup the parameters of the message
        m.To = email
        m.Subject = "Leave Status "
        if int(self.days)==1: 
            m.Body = get_content1()
        else:
            m.Body = get_content()
        # Sending the mail
        m.Save()
        m.Send()
        
        
#obj=Email(10671102,'29-09-2020',4)
#obj.fetch_mail()      
        
        
        