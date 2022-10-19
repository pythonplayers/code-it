def func1(data):
    dicta={}
    data2=data.split()
    for val in data2:
        if val in dicta:
            dicta[val]+=1
        else:
            dicta[val]=1
    return dicta

def func2(data):
    dictb=func1(data)
    print(dictb)
    max=0
    maxkey=''
    for val in dictb.keys():
        if dictb[val] > max:
            max=dictb[val]
            maxkey=val
    return maxkey

if __name__=='__main__':
    data=input()
    print(func2(data))