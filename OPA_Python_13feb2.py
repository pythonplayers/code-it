class Employee():
    def __init__(self,id,name,leaves):
        self.id=id
        self.name=name
        self.leaves=leaves

class Company():
    def __init__(self,name,emps):
        self.name=name
        self.emps=emps

    def display_leave(self,emp,ltype):
        for empi in self.emps:
            if empi.id==emp:
                return empi.leaves[ltype]

    def number_of_leaves(self,emp,ltype,nol):
        for empi in self.emps:
            if empi.id==emp:
                if empi.leave[ltype]>=nol:
                    return "Granted"
                else:
                    return "Rejected"
n=int(input())
emps=[]
c=Company("Com",emps)
leaves={}
for i in range(n):
    eid=int(input())
    ename=input()
    leaves["CL"]=int(input())
    leaves["EL"]=int(input())
    leaves["SL"]=int(input())
    c.emps.append(Employee(eid,ename,leaves))
emp=int(input())
ltype=input()
nol=int(input())
print(c.display_leave(emp,ltype))
print(c.number_of_leaves(emp,ltype,nol))
