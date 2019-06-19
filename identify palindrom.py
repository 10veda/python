def revr(a):
     s=str(a)
     r=s[::-1]
     return (int(r))
def pali(a):
    s=str(a)
    r=int(s[::-1])
    return r==a

l=input()
n=int(l)
p=False
while(not p):
    if(n<10):
        if(n*2<10):
            n=n*2
            p=True
        else:
            r=revr(n*2)
            p=pali(r+(n*2))
            n=r+(n*2)
    else:
        r=revr(n)
        p=pali(r+n)
        n=r+n
if(p):
    print(n) 
