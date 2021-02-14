class employee:#for query refer 4 feb 2021
    def __init__(self,id,name,designation,salary):
        self.id=id
        self.name=name
        self.designation=designation
        self.salary=salary
    def __str__(self):
        return self.name
f=open("employees.txt","r")
emplist=[]
sallist=[]
for lines in f:#100,"akhil","developer",25000
    id,name,designation,salary=lines.rstrip("\n").split(",")
    emplist.append(employee(id,name,designation,salary))
for employ in emplist:
     sallist.append(employee.salary)
print(max(sallist))




