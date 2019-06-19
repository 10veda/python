'''Armstrong'''
p=input(" ")
d=len(p)
n=int(p)
t=n
s=0
while n!=0:
    r=n%10
    s=r**d+s
    n=n//10n=input()
p=int(n)
h=p
o=0
while(p!=0):
    r=p%10
    o=o*10+r 
    p=p//10
if o==h:
    print("Palin")
else:
    print("Not palin")
    
    

if t==s:
    print("Armstrong")
else:
    print("Not Armstrong")
''' between interval armstrong'''

l=100
u=2000
for i in range(l,u+1):
    d=len(str(i))
    s=0
    t=i
    while t>0:
        r=t%10
        s=r**d+s
        t=t//10
    if i==s:
        print(i)
''' palind'''
def re(s):
    return s[::-1]
def isp(s):
   r= re(s)
   if(s==r):
    return 1 
   else:
       return 0

s="MadaM"
print(isp(s))

'''Another pali'''
s="mdam"
pr=1
for i in range(0,len(s)//2):
    if s[i]!=s[len(s)-i-1]:
        pr=0
    else:
        pr=1
print(pr)

'''reverse a num'''
p=input(" ")
n=int(p)
r=0
while n!=0:
    re=n%10
    r=r*10+re
    n=n//10
print(r)
    
'''reverse a num'''
p=input(" ")
print(p[::-1])
    
'''sum of digits'''
p=input(" ")
n=int(p)
r=0
while n!=0:
    re=n%10
    r=r+re
    n=n//10
print(r)


'''number of digits'''
p=input(" ")
n=int(p)
r=0
while n!=0:
    n=n//10
    r=r+1;
print(r)
    

'''factors & count'''
p=input(" ")
n=int(p)
c=0
for i in range(1,n+1):
    if n%i==0:
        print(i)
        c=c+1
print(c)


'''sum of natural '''
p=input(" ")
n=int(p)
c=0
for i in range(0,n+1):
    c=c+i 
print(c)

'''formula sum '''
p=input(" ")
n=int(p)
c=0
c=(n*(n+1))//2
print(c)


'''tables'''
n=input(" ")
m=input(" ")
v=int(n)
j=int(m)
for i in range(1,j+1):
    print(v,"*",i,"=",v*i)
    
    
    
    \\\\digit pslin
    n=input()
p=int(n)
h=p
o=0
while(p!=0):
    r=p%10
    o=o*10+r 
    p=p//10
if o==h:
    print("Palin")
else:
    print("Not palin")
