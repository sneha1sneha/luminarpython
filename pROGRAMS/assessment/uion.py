#union of two list
list1=[1,2,3,4,5,6,7]
list2=[7,8,9]
#list1=[7,8,9]
#list2=[1,2,3,4,5,6,7]
list=[]
a=len(list1)
b=len(list2)
i=0
j=0
while(i<a or j<b):
 if i<a and j<b:
    if list1[i]==list2[j]:
       i+=1
       j+=1
    elif list1[i]>list2[j]:
         list.append(list2[j])
         j+=1
    else:
         list.append(list1[i])
         i+=1
 elif j<b and a==i:
       list.append(list2[j])
       j+=1
       #break
 else :
       list.append(list1[i])
       i+=1
       #break
print(list)
