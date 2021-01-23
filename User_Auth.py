
class Authenticate():
    def __init__(self,ID,pswd):
        self.ID = int(ID)
        self.pswd = pswd
    def authenticate(self):
        #key = Fernet.generate_key() # Generating key
       
        f= open("key.txt","rb")
        key = f.read()
        from cryptography.fernet import Fernet
        cipher_suite = Fernet(key)
        #print(f.read())
        f.close()
        import pandas as pd
        DF =  pd.read_excel('emp_ex.xlsx')
        main_ID2 = list(DF['EmpID'])
        name2 = list(DF['Username'])
        main_ID = []
        
        for i in range(0,len(main_ID2)):
            main_ID.append(int(main_ID2[i]))
        
        main_pswd = list(DF['Password_encrp'])
        
        
        
        while(True):
            try:
                if self.ID in main_ID:
                    print('User Exist')
                
                    temp_index = main_ID.index(self.ID)
                    
                    
                    
                    #-----------------------------------------------------------
                    passwd1_byte = bytes(self.pswd, 'utf-8')
                    
                    if  passwd1_byte ==  cipher_suite.decrypt(bytes(main_pswd[temp_index],'utf-8')):
                        print("Correct Password")
                        return str(self.ID), name2[temp_index]
                        break
                    else:
                        print("Incorrect Password")
                        break
                else:
                    print("User Does Not Exist or Entered ID is Incorrect")
                    break
            except:
                print("Employee ID must be Integer")
                break
            else: 
                return str(self.ID), name2[temp_index]