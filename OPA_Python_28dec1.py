class Apartment():
    def __init__(self,flatnum,ownername,billamount):
        self.fn=flatnum
        self.on=ownername
        self.ba=billamount

class ApartmentDemo():
    def __init__(self):
        pass
    def getSecondMinBill(self,apartobj):
        data=[]
        for val in apartobj:
            data.append(val.ba)
        data.sort()
        return data[1]

if __name__=='__main__':
    apartlist=[]
    for _ in range(int(input())):
        apartlist.append(Apartment(int(input()),input(),int(input())))
    print(ApartmentDemo().getSecondMinBill(apartlist))
