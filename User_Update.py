class Leave_Mechanism():
    def __init__(self,event,date,descrp,num_of_days,emp_id):
        self.event = event
        self.date = date
        self.descrp = descrp
        self.num_of_days = num_of_days
        self.emp_id = emp_id
        
    def update(self):
        import pandas as pd
        import datetime
        
        
        def temp_update():
            if leave>=int(self.num_of_days):
                print(" Available Leave Balance: {}".format(leave))
                #DF_leave=pd.read_excel('leave.xlsx')
                flag = 0
                for i in range(0,int(self.num_of_days)):
                    
                    DF_leave=pd.read_excel('leave.xlsx')
                    df =DF_leave[DF_leave['Leave_Date']==str(self.date)]
                    temp_id2_new = list(df['EmpID'])
                    
                    temp_id_new=[]
                    for j in range(0,len(temp_id2_new)):
                        temp_id_new.append(str(temp_id2_new[j]))
                    
                    
                    if str(self.emp_id) in temp_id_new:
                        
                        print("You Have already Applied Leave on {} Please Choose Other Date".format(self.date))
                        x="You Have already Applied Leave on {} Please Choose Other Date".format(self.date)
                        flag = flag+1
                        d = datetime.datetime.strptime(self.date, '%d-%m-%Y') + datetime.timedelta(days=1)
                        self.date=d.strftime('%d-%m-%Y')
                        return x
                    
                    elif flag==0:
                        Data=[{'EmpID': self.emp_id,'TeamNo':Team_mem[team_no],'Leave_Date':self.date,'Leave_Type':self.event,' Description':self.descrp,
                               'numberDays':self.num_of_days,'remaindays':int(self.num_of_days)-i}]
                        #print(int(self.num_of_days)-i)
                        #print("============")
                        A=DF_leave.append(Data,ignore_index=True,sort=False)
                        d = datetime.datetime.strptime(self.date, '%d-%m-%Y') + datetime.timedelta(days=1)
                        self.date=d.strftime('%d-%m-%Y')
                        A.to_excel("leave.xlsx")
                    
                if flag!=0:
                    print("Choose Other Date")
                    return 0
                DF.loc[team_no, 'Leave_Balance'] = str(leave - int(self.num_of_days))
                DF.to_excel("emp_ex.xlsx")
                #print("************************************")
                return self.num_of_days

            else:
                print("You Don't have Enough Leave Available You can apply Leave For maximum {} days".format(leave))
                x="You Don't have Enough Leave Available You can apply Leave For maximum {} days".format(leave)
                return x

        
        
        
        
        DF = pd.read_excel('emp_ex.xlsx')
        ID2 = list(DF['EmpID'])
        ID =[]
        
        for i in range(0,len(ID2)):
            ID.append(str(ID2[i]))
        
        Team_mem = list(DF['TeamNo'])
        team_no = ID.index(self.emp_id)
        
        leave = int(DF.loc[team_no].Leave_Balance)
        #----------------------------------------------------------------------------------------
        temp_df = pd.read_excel('leave.xlsx')
        temp_id2 = list(temp_df['EmpID'])
        temp_id2_leave_date = list(temp_df['Leave_Date'])
        temp_id2_number_of_date = list(temp_df['numberDays'])
        
        temp_id=[]
        for i in range(0,len(temp_id2)):
            temp_id.append(str(temp_id2[i]))
        x = temp_update()#...................................Change.........
        return x
        '''
        #.............Irrelevant Code...........................................
        if (self.emp_id in temp_id):
            ind=temp_id.index(self.emp_id)
            s =  temp_id2_leave_date[ind]
            d = datetime.datetime.strptime(s, '%d-%m-%Y') + datetime.timedelta(days=30)
            d=d.strftime('%d-%m-%Y')
            from datetime import timedelta, date
            start = datetime.datetime.strptime(s, "%d-%m-%Y")
            end = datetime.datetime.strptime(d, "%d-%m-%Y")
            date_array = (start + datetime.timedelta(days=x) for x in range(0, (end-start).days))
            a=[]
            for date_object in date_array:
                a.append(date_object.strftime("%d-%m-%Y"))
            temp_update()
           # if self.date in a:
            #    print("You can't take leave...You can take Leave after {}".format(a[-1]))
            #else:
               # temp_update()
        else:
            temp_update()
        '''
                
        

           
        
        #----------------------------------------------------------------------------------------
        