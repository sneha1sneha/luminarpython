#i/p=[1,2,3,4,5,6]
#o/p=[1,2,3,6,5,4]
l1=[1,2,3,4,5,6]
'''b=input("entre the numbers")
l1=[]
l1.append(b)

print(l1)'''
list=[]
l=0
u=len(l1)
m=int((l+u)/2)
for i in range(0,m):
    a=l1[i]
    list.append(a)
#print(list)
i=u
while i>m:
 i=i-1
 a=l1[i]
 list.append(a)
print(list)
