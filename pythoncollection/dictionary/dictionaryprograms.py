#values stored with key
#not possible to store duplicates key must be unique
expenses={"jan":30000,"feb":40000,"march":50000,"april":25000}
print(expenses["march"])
#check for june2
#adding new key value pair
print("june20" in expenses)
#adding new key value pair
expenses["sep"]=70000
print(expenses)
#value updating
expenses["jan"]+=2000
print(expenses["jan"])
