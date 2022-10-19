def is_prime(num):
    if num<=1:
        return -1
    else:
        for i in range(2,int(a/2)+1):
            if a%i==0:
                return 0
        return 1

def printlist(l):
    both=[]
    prime=[]
    composite=[]
    for val in l:
        if val == 1:
            prime.append(val)
        elif val == 0:
            composite.append(val)
    both.append(p)
    both.append(c)
    return both

if __name__ == '__main__':
    l=[]
    for _ in range(int(input())):
        l.append(int(input()))
    print(is_prime(l[1]))
    print(printlist(l))