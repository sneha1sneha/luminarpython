#i/p=[2,3,4]
#o/p=[7,6,5]
list=[]
list1=[]
total=0
a=int(input("enter the number of elements"))
for i in range(0,a):
 list.append(int(input("entre the elements")))
print("input list",list)
for i in list:
     total+=i
for i in list:
    v=total-i
    list1.append(v)
print("output list",list1)




