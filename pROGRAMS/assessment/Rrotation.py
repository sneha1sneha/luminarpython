


#list=[1,2,3,4]
#list=[1,2,3,4,5,6,7,8,9]
#o/p=[3,4,1,2]
a=int(input("enter the  position from "
            "which rotation to be performed"))
i=a-1
n=len(list)
listt=[]
for num in range(i,n):
  listt.append(list[num])
j=0
for num in range(j,i):
    listt.append(list[num])
print(listt)

