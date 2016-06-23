"""This code checks the complexity of the password

Create function for checking"""

def pas(data):
    num=False
    up=False
    low=False
    char=False
    forChar=["!","@","#","$","%","^","&","*","(",")","-","_","=","+",";",":"]
    for i in data:
        if i.isdigit():
            num=True
        elif i.isupper():
            up=True
        elif i.islower():
            low=True
        elif i in forChar:
            char=True
    if len(data)>5:
        if (num==True) and (up==True) and (low==True) and (char==True):
            return "Very good password"
        elif ((num==True) and (char==True) and ((up==True) or (low==True))) or\
                (((num==True) or (char==True)) and (up==True) and (low==True)):
            return "Good password"
        elif ((num==True) or (char==True)) and ((up==True) or (low==True)):
            return "Normal password"
        elif (low==True) and (up==True):
            return "Simple password"
        elif (up==True) or (low==True) or (num==True):
            return "Very simple password"
    else:
        return "Short password"

#Ask user to enter password
a=input("Enter password: ")
print(pas(a))