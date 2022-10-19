class Item():
    def __init__(self,iid,iname,iprice,qa):
        self.iid=iid
        self.iname=iname
        self.iprice=iprice
        self.qa=qa

    def calc_price(self,quantity):
        if quantity<self.qa:
            return quantity*self.iprice
        else:
            return 0

class Store():
    def __init__(self,ilist):
        self.ilist=ilist

    def genrate_bill(self,namequantdict):
        price=0
        for iname,quantity in namequantdict.items():
            for storeitem in self.ilist:
                if storeitem.name==iname:
                    price+=storeitem.calc_price(quantity)
        return price

if __name__=='__main__':
    l=[]
    for _ in range(int(input())):
        i=Item(int(input()),input(),int(input()),int(input()))
        l.append(i)
    s=Store(l)
    d={}
    for _ in range(int(input())):
        n=input()
        q=int(input())
        d[n]=q
    print(l[0].calc_price(2))
    print(s.genrate_bill(d))