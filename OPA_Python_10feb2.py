class Employee():
    def __init__(self,eid,ename,erole,esalary):
        self.eid=eid
        self.ename=ename
        self.erole=erole
        self.esalary=esalary

    def increment_salary(self,percent):
        self.esalary=self.esalary+(self.esalary*(percent/100))

class Organization():
    def __init__(self,orgname,emplist):
        self.orgname=orgname
        self.emplist=emplist

    def calculate_salary(self,erole,salarypercent):
        result=[]
        for emp in self.emplist:
            if(emp.erole==erole):
                emp.increment_salary(salarypercent)
                result.append(emp)
        return result

if __name__=='__main__':
    emps=[]
    for _ in range(int(input())):
        emp=Employee(int(input()),input(),input(),int(input()))
        emps.append(emp)
    org1=Organization('org1',emps)
    role=input()
    percent=int(input())
    fina=org1.calculate_salary(role,percent)
    for emp in fina:
        print(emp.ename)
        print(emp.esalary)