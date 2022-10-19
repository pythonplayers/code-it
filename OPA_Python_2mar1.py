data=[]
for _ in range(int(input())):
    data.append(input().strip())
fina=[]
vow='aeiou'
for val in data:
    for letter in val:
        if letter in vow:
            fina.append(val)
fina=list(set(fina))
if len(fina)==0:
    print("no values")
else:
    for val in data:
        if val in fina:
            pass
        else:
            print(val)