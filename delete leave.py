

class Delete_leave():
    def __init__(self,empid,leave_date):
        self.empid=int(empid)
        self.leave_date=str(leave_date)
        

    def delete(self):
        import pandas as pd
        import datetime
        DF_leave=pd.read_excel('leave.xlsx')
        
        #leave_ind=DF_leave.index
        DF_emp=DF_leave[DF_leave['EmpID']==self.empid]
        
        DF_emp_leave=list(DF_emp['Leave_Date'])
       
        now=datetime.datetime.now()
        now=now.strftime('%d-%m-%Y')
        now=datetime.datetime.strptime(now,'%d-%m-%Y')
        
        leaveD=datetime.datetime.strptime(self.leave_date,'%d-%m-%Y')
     
        #========
      
        
        if leaveD > now:
            
            if(self.leave_date in DF_emp_leave):
                leave_ind=DF_leave[DF_leave['EmpID']==self.empid]
                leave_ind1=leave_ind[leave_ind['Leave_Date']==self.leave_date].index
                
                DF_leave.drop(leave_ind1, inplace = True)
                DF_leave.to_excel('leave.xlsx')
                #=======================
                
                DF = pd.read_excel('emp_ex.xlsx')
                ID = list(DF['EmpID'])
                #
                
                emp_ind = ID.index(self.empid)
                
                leave = int(DF.loc[emp_ind].Leave_Balance)
                DF.loc[emp_ind, 'Leave_Balance'] = str(leave + 1)
                DF.to_excel("emp_ex.xlsx")
                
                #==========================
                print("leave deleted succesfully")
                return 1
            else:
                print("enter proper leave date//u r not on leave on this day")
                return 2
                
                
        else:
            print("you cannot choose past days")
            return 3
obj=Delete_leave('10671105','29-01-2021')
obj.delete()