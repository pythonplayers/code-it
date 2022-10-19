#code copied from kumarweb not written by me
class Passenger:
    def __init__(self,pid,pname,pgender,pmiles):
        self.pid=pid
        self.pname=pname
        self.pgender=pgender
        self.pmiles=pmiles
    def calculate_discount(self,pid,discount_rate):
        for i in pass_list:
            if i.pid==pid:
                discount=(i.pmiles*discount_rate)/100
                return discount
class Organisation(Passenger):
    def __init__(self,oname,pass_list):
        self.oname=oname
        self.pass_list=pass_list
if __name__ == '__main__':
    n=int(input())
    pass_list=[]
    for i in range(n):
        pid=input()
        pname=input()
        pgender=input()
        pmiles=int(input())
        pass_list.append(Passenger(pid,pname,pgender,pmiles))
    pid=input()
    discount_rate=int(input())
    o=Organisation('TCS',pass_list)
    discount=o.calculate_discount(pid,discount_rate)
    if discount<0:
        print("Passenger not eligible for discount")
    else:
        print("The discount of passenger "+pid+" is " +str(discount))
