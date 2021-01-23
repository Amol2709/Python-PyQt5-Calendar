class CrossCheck():
    def __init__(self,emp_id,leave_date,number_of_days):
        self.emp_id  = emp_id
        self.leave_date = leave_date
        self.number_of_days = number_of_days
    def checkPrev(self):
        import pandas as pd
        import datetime

        import holidays
        
        #var = datetime.datetime.now()
        #var1= var.strftime('%Y')
        var1 = datetime.datetime.strptime(str(self.leave_date), '%d-%m-%Y')
        var1 = str(var1.strftime("%Y"))
        L=[]
        for ptr in holidays.IND(years = int(var1)).items():
            L.append(ptr[0].strftime('%d-%m-%Y'))
        #d3 = var.strftime("%A") #if...and holidays
        
        print(var1)

        s=datetime.datetime.now()
        s1=s.strftime('%d-%m-%Y')
        d1 = datetime.datetime.strptime(s1, '%d-%m-%Y')
        d2 = datetime.datetime.strptime(str(self.leave_date), '%d-%m-%Y')
        d22 = d2.strftime('%d-%m-%Y')
        d3 = str(d2.strftime('%A'))
        print(d3)
        print(type(d2))
        print(str(d2))
        if d1<d2 and d3 != "Sunday" and str(d22) not in L:
            return True
        elif d3 == "Sunday":
            return "Cant Apply Leave on Sunday"
        elif str(d22) in L:
            return "Cant Apply Leave on public holidays"
        #else:
            #return "Insufficient Leave Balance. Pleae check your leave balance"


    def check_team(self):
        import pandas as pd
        import datetime
        DF1 = pd.read_excel("emp_ex.xlsx")
        DF2 = pd.read_excel("leave.xlsx")
        DF3 = pd.read_excel("team_count.xlsx")
        
        
        df =DF1[DF1['EmpID']== int(self.emp_id)]
        team_no=list(df['TeamNo'])[0]
        
        
        df_3 = DF3[DF3['Team_no']== int(team_no)]
        count = list(df_3['count'])[0]
        
        df =DF2[DF2['TeamNo']== team_no]
        
        df = df[df['Leave_Date']== self.leave_date]
        
        #df_leave = pd.read_excel('leave.xlsx')
        df_leave_2 = DF2[DF2['TeamNo']==int(team_no)]
        if len(df_leave_2)!=0:
            print("inside loop")
            
            #count=0
            teammem_entry=[]
            RET_L = []
            for i in range(0,int(self.number_of_days)):
                for j in df_leave_2['Leave_Date']:
                    if self.leave_date == j:
                        
                        teammem_entry=df_leave_2[df_leave_2['Leave_Date']==self.leave_date]
                        #print(teammem_entry)
                        
                        var = len(list(teammem_entry['EmpID']))
                        RET_L.append((var/int(count),self.leave_date))
                        #if var/int(count) >0.5:
                            #print("Proportion is More than 50 ......{}".format(var/int(count)))
                        #else:
                         #   pass
                            
                        print("{} on {}".format(len(list(teammem_entry['EmpID'])),self.leave_date))
                        #print(len(list(teammem_entry['EmpID']))," on ",self.leave_date)
                        # print(str(list(teammem_entry['EmpID'])))
                        break
                    
                d= datetime.datetime.strptime(self.leave_date, '%d-%m-%Y') + datetime.timedelta(days=1)
                self.leave_date=d.strftime('%d-%m-%Y')
           # temp=list(teammem_entry['EmpID'])   
            #print(temp[0])
            #print("#============== >>",count)
            print(RET_L)
            count=0
            if len(RET_L)>0:
                res="More than 50 percent of your team are on leave on : "
                for x,y in RET_L:
                    if int(100*x) >= 50:
                        count=1
                        res += y
                        res += ", "
                if count==1: return res[:-2]
                else: return -1
            else: return -1
                
        else:
            print("no member frm ur team is on leave")
            return -1
            
        