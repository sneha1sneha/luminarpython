#intersection of two sorted list
'''list1=[]
list2=[]
a=int(input("enter the list1 numbers"))
list1.append(a)
print(list1)
b=int(input("enter the list2 numbers"))
list2.append(b)
print(list2)'''
list1=[1,2,3,4,5]
list2=[4,5,6,7,9]
list=[]
n1=len(list1)
n2=len(list2)
i=0
j=0
while(i<n1 and j<n2):
    if list1[i]==list2[j]:
        list.append(list1[i])
        i+=1
        j+=1
    elif list1[i]<list2[j]:
        i+=1
    else:
        j+=1
print(list)





