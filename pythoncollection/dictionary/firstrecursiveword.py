pattern="ABAABBC"
#find first repeating charector

dict{}
for ch in pattern:
    if ch not in dict:
        dict[ch]=1
    else:
        print(ch,recursive)
        break