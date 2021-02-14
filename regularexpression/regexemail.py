from re import *
emailid=input("entre the emailid")
rule="[a-zA-Z0-9.]*@gmail.com"
matcher=fullmatch(rule,emailid)
if matcher==None:
    print("invalid emailid")
else:
    print("valid emailid")