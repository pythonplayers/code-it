class Payslip():
    def __init__(self,bs,h,t):
        self.bs=bs
        self.h=h
        self.t=t
class Pd():
    def __init__(self):
        self.a=10
    def getpf(self,l):
        k=[]
        for i in l:
            a=i.bs*0.12
            k.append(a)
        k1=max(k)
        return k1
if __name__=='__main__':
    p=[]
    c=int(input())
    for i in range(c):
        bs=int(input())
        h=int(input())
        t=int(input())
        p.append(Payslip(bs,h,t))
    pa=Pd()
    pf=pa.getpf(p)
    print(int(pf))
