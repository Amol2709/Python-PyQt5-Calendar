class NewPassword():
    from cryptography.fernet import Fernet
    import pandas as pd
    
    def __init__(self,emp_id,pswd):
        self.emp_id =emp_id
        self.pswd =pswd
        
    def change_pswd(self):
        from cryptography.fernet import Fernet
        import pandas as pd
        f= open("key.txt","rb")
        key = f.read()
        f.close()
        cipher_suite = Fernet(key)
        DF = pd.read_excel('emp_ex.xlsx')
        
        index=list(DF['EmpID']).index(int(self.emp_id))
        
        pswd_bytes=bytes(self.pswd,'utf-8')
        #print(pswd_bytes)
        x= cipher_suite.encrypt(pswd_bytes)
        #print(x)
        #print(x.decode("utf-8"))
        DF.loc[index, 'Password_encrp'] = x.decode("utf-8")
        DF.to_excel('emp_ex.xlsx')
        