class Bill():
    def __init__(self,mn,pb):
        self.mn=mn
        self.pb=pb
class Mobile():
    def __init__(self,sp,mn,du,pm):
        self.sp=sp
        self.mn=mn
        self.du=du
        self.pm=pm
class CalcBillDemo():
    def __init__(self):
        pass
    def calculatebill(self,mobilelist):
        fina=[]
        for val in mobilelist:
            mn=val.mn
            pb=0
            if val.sp == 'airtel':
                pb=pb+(val.du*11)
                if val.pm == 'paytm':
                    pb=pb-(pb*0.1)
                    # print(pb)
            else:
                pb=pb+(val.du*10)
            tempobj=Bill(mn,int(pb))
            fina.append(tempobj)
        return fina

if __name__=='__main__':
    for _ in range(int(input())):
        data=[]
        sp=input().strip()
        mn=int(input().strip())
        du=int(input().strip())
        pm=input().strip()
        data.append(Mobile(sp,mn,du,pm))
        calcbill=CalcBillDemo()
        data2=calcbill.calculatebill(data)
        for val in data2:
            print(val.mn,val.pb)
