class PasswordComplexity():
    def __init__(self,password):
        self.password = password
    def checkcomplexity(self):
        import re
        if (len(self.password)<8): 
            x= "password is short"
            flag = 0
           
        elif not re.search("[a-z]", self.password): 
            x= "password has no small letters"

            flag = 0
   
        elif not re.search("[A-Z]", self.password): 
            x= "password has no capital lettters"
            flag = 0
       
        elif not re.search("[0-9]", self.password): 
            x= "password no numbers"
            flag = 0
         
        elif not re.search("[_@$#%&*^!~`]", self.password): 
            x= "password has no special characters"
            flag = 0
         
        elif re.search("\s", self.password): 
            x= "whitespace not allowed in password"
            flag = 0
           
        else: 
            flag = 1
            x= " the Password is strong"
        return flag,x

            


