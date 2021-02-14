lst=[1,2,3,4,5]
#sqlist=list(map(lambda num:num**2,lst))
#print(sqlist)

newlist=list(map(lambda num:num+1 if num>5 else num-1,lst))
print(newlist)
