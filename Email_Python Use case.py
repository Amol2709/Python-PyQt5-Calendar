# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 12:09:51 2020

@author: priya
"""

import win32com.client as client
import csv

# Email Template setup
def get_content(full_name):

    email_content ="""
Hi """+full_name+""",

Your  Earned Leave application from ---  to --- have been submitted successfully.

 
Regards,

Leave Administrator
    """

    return email_content

# Main function   
def main():
    with open("C:\\Users\\priya\\Documents\\Work\\LTI\\Training\\Assessment\\Python Use Case\\Database.csv") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for name, email in reader:
            print(f"Sending email to {name}")
        
        # send the message via desktop app.
            outlook = client.Dispatch("Outlook.Application")
            m = outlook.CreateItem(0)
            m.Display()
        
        # setup the parameters of the message
            m.To = email
            m.Subject = "Test mail"
            m.Body = get_content(name)
        
        # Sending the mail
            m.Save()
            m.Send()
        
        # Deleting the file content
            with open('C:\\Users\\priya\\Documents\\Work\\LTI\\Training\\Assessment\\Python Use Case\\Database.csv', "w"):
                pass
            print("Email sent")
        
    
if __name__ == '__main__':
    main()

    
    
    
