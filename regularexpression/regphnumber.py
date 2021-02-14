from re import *
#num=input("enter the number")
#rule="(91)?[0-9]{10}" #\d{10}
f=open("phonenumber","r")
for num in f:
 rule="(91)?[0-9]{10}"
 matcher=fullmatch(rule,num)
 if matcher==None:
    print("invalid entry")
 else:
    print("valid entry")