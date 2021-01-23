class LeaveRemain():
    def __init__(self,emp_id):
        self.emp_id = emp_id
    def leave_remain(self):
        import pandas as pd
        DF = pd.read_excel('emp_ex.xlsx')
        df =DF[DF['EmpID']== int(self.emp_id)]
        print(list(df['Leave_Balance'])[0])
      
        return str(list(df['Leave_Balance'])[0])
      
        