class college:
    def __init__(self,sid,sname,smarks,stid,stname):
     self.sid=sid
     self.sname=sname
     self.smarks=smarks
     self.stid=stid
     self.stname=stname
    def student(self):
       print(self.sid,self.sname,self.smarks)
    def staff(self):
       print(self.stid,self.stname)
obj=college(1,"sruthi",2,22,"reva")
obj.student()
obj.staff()
