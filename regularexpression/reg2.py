from re import *
pattern='aa'
matches=finditer(pattern,"aaaayaayaayyaay")
print(matches)
for m in matches:
 print(m.start(),"->",m.group())