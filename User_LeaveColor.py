class LeaveColor():
    def __init__(self,emp_id):
        self.emp_id = emp_id
    def color_leave(self):
        import pandas as pd
        import holidays
        import datetime
        
        DF = pd.read_excel('leave.xlsx')
        DF2 = DF[DF['EmpID']==int(self.emp_id)]
        L1 = list(DF2['Leave_Date'])
        L2=[]
        var = datetime.datetime.now()
        var1= var.strftime('%Y')
        for ptr in holidays.India(years = int(var1)).items():
            L2.append(ptr[0].strftime('%d-%m-%Y'))
        return L1,L2 #first list in tuple will be Employee Holidays(green) and second one is National Holidays(RED)