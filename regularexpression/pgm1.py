#day 9,10 feb-class 28
from re import *
pattern='ab'
matcher =finditer(pattern,"abaabbababababab") #iterable,avidayenkilum pattern match undho eannan check chayunnath

cnt=0
for match in matcher:
    print(match)
    print(match.start())
    print(match.group())
    cnt+=1
print(cnt)