list=[2,3,4,5,8]
n=2
l=0
u=len(list)-1  #u=4,value=8
#print(u)
m=int((u+l)/2) #m=2,value=4
#print(m)
while(l<=u):
 if list[m]==n:
    print("element found at ",list[m])
    break
 elif n>list[m]:
    l=m+1 #m=3 value=5
    u=len(list)-1#m=4 value=8
    m=int((u+l)/2)#m=3 value=5
 else:
    u=m-1
    l=0
    m=m-1+l/2


