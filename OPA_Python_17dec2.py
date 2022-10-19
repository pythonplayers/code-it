class Stock():
    def __init__(self,StockName,StockSector,StockValue):
        self.sn=StockName
        self.ss=StockSector
        self.sv=StockValue

class StockDemo:
    def __init__(self):
        self.a=10
    def getStockList(self,StockObjects,StockSector):
        fina=[]
        for val in StockObjects:
            if val.ss==StockSector:
                if int(val.sv)>500:
                    fina.append(val.sn)
        return fina

if __name__=='__main__':
    stocklist=[]
    for val in range(int(input())):
        sn,ss,sv=[input() for _ in range(3)]
        stocklist.append(Stock(sn,ss,sv))
    findsect=input()
    s=StockDemo().getStockList(stocklist,findsect)
    for val in s:
        print(val)
