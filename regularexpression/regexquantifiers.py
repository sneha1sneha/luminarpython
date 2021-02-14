'''pattern='[ab]'#check for either a or b
pattern="[a-z]"#check for lower case a to z
pattern="\s"#check for space
pattern="\d"#check for digits
pattern="\D"#[^0-9]
pattern="a+"#one or more
pattern="a*"#zero or more
pattern="(a)?"#zero or one
#{2},two times
#{2,4},min two max 4'''

#question:first character must be a alphabet b/w a-k
        # second must be a number divisible by 3
        # followed by any number of character
from re import *
value=input("enter the value")
rule="[a-k][369][a-zA-Z0-9]*"
matcher=fullmatch(rule,value)#fullmatch finds the exact match with rule in each position
if matcher==None:
    print("invalid entry")
else:
    print("valid entry")