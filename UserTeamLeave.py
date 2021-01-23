class TeamLeaveInfo():
    def __init__(self,emp_id,leave_date,nod):
        self.emp_id = emp_id
        self.leave_date = leave_date
        self.nod = nod
    
    def display(self):
        import pandas as pd
        import datetime
        DF_emp = pd.read_excel('emp_ex.xlsx')
        DF = pd.read_excel('leave.xlsx')
        team_no = list(DF[DF['EmpID']==int(self.emp_id)]['TeamNo'])[0]
        DF_team = DF[DF['TeamNo']==int(team_no)]
        
        start = datetime.datetime.strptime(str(self.leave_date), "%d-%m-%Y")
        end = datetime.datetime.strptime(str(self.leave_date), '%d-%m-%Y') + datetime.timedelta(days=int(self.nod))
        date_array =(start + datetime.timedelta(days=x) for x in range(0, (end-start).days))
        a=[]
        for date_object in date_array:
            a.append(date_object.strftime("%d-%m-%Y"))
        
        common2 = list(set(a + list(DF_team['Leave_Date'])))
        common=list(set(a) & set(list(DF_team['Leave_Date'])))
        
        
        if True:
            RET=[]
            BEST={}
            DAYS=[]
            D=[]
            E=[]
            BEST
            for i in common:
                temp_df = DF_team[DF_team['Leave_Date']==i]
                for j in range(0,len(list(temp_df['Leave_Date']))):
                    
                    if i == list(temp_df['Leave_Date'])[j]:
                        EMP_ID=list(temp_df['EmpID'])[j]
                        DATE = list(temp_df['Leave_Date'])[j]
                        days=list(temp_df['remaindays'])[j]
                        name=list(DF_emp[DF_emp['EmpID']==int(EMP_ID)]['Username'])[0]
                        #BEST.append((name,EMP_ID,DATE))
                        DAYS=[]
                        D=[]
                        E=[]
                        EMP=[]
                        
                       
                        D.append(DATE)
                        DAYS.append(days)
                        EMP.append(EMP_ID)
                        BEST[str(name)]= (D,DAYS,EMP)
                        RET.append("{}-{} is on Leave on {} for {} days".format(name,EMP_ID,DATE,days))
            print(BEST)
            if len(RET)!=0:
                F=[]
                Final=[]
                
                for keys in BEST.keys():
                    start = datetime.datetime.strptime(BEST[keys][0][0], "%d-%m-%Y") +datetime.timedelta(days=BEST[keys][1][0])-datetime.timedelta(days=1)
                    if BEST[keys][0][0] == start.strftime("%d-%m-%Y"):
                        Final.append("{}-{} is on leave on {}".format(keys,BEST[keys][2][0],BEST[keys][0][0]))
                    else:
                        Final.append("{}-{} is on leave from {} to {}".format(keys,BEST[keys][2][0],BEST[keys][0][0],start.strftime("%d-%m-%Y")))
                        
                return Final
            else:
                print("No one is on Leave")
                Final=['No one is on Leave']
                return Final
        
        
    