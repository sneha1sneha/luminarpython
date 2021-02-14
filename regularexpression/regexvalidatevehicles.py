#kl2digits2alphabets4digits

from re import *
regno=input("enter the number")
#rule="kl[0-9][0-9][a-zA-Z][a-zA-Z][0-9][0-9][0-9][0-9]"
rule="kl[0-9]{2}[a-zA-Z]{2}[0-9]{4}"
matcher=fullmatch(rule,regno)
if matcher==None:
    print("invalid number")
else:
    print("valid entry")
