def palindrome_list(data):
    fina=[]
    for val in data:
        j=val.lower()
        if j[::-1]==j:
            fina.append(val)
    return fina

if __name__=='__main__':
    data=[]
    for _ in range(int(input())):
        data.append(input().strip())
    filterdata=palindrome_list(data)
    for val in filterdata:
        print(val)