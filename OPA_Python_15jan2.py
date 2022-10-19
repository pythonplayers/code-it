class Book():
    def __init__(self,bid,bname):
        self.bid=bid
        self.bname=bname
class Library():
    def __init__(self,lid,add,booklist):
        self.lid=lid
        self.add=add
        self.booklist=booklist
    def charin(self,character):
        count=0
        for val in self.booklist:
            if val.bname[0] == character:
                count+=1
        return count
    def removebook(self,booknames):
        for i in self.booklist:
            if i.bname not in names:
                print(i.bname)

if __name__=='__main__':
    bl=[]
    for _ in range(int(input())):
        bid=int(input())
        bname=input()
        bl.append(Book(bid,bname))
    l=Library(123,'Mumbai',bl)
    char=input()
    names=[]
    for i in range(int(input())):
        names.append(input())
    print(l.charin(char))
    l.removebook(names)
    d=l.booklist
    for val in d:
        print('remaining - ',val.bname)