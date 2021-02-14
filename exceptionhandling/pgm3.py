list=[1,2,3,4]
g=int(input("entre the postion of element to be print"))
k=int(input("entre the number"))
m=int(input("entre the number"))
try:
    res=k/m
    print(int(res))
    print(list[g])
except Exception as z:
    print(z.args)
finally:
    print("Thanku for using this services")

