digit in number:

m=list(map(str,str(input().split())))
n=input()
if n in m:
    print("True")
else:
    print("False")
    
    
 \\\
 string compare with position 
    
    
    
    
\\\\
s=int(input(" "))
n=int(input(" "))
m=s
c=0
while m>0:
    r=m%10
    if r==n:
        c=1
    m=m//10
if c==1:
    print("True")
if c==0:
    print("False")
    
    
\\count digits 

s=int(input(" "))
n=int(input(" "))
m=s
c=0
while m>0:
    r=m%10
    if r==n:
        c+=1
    m=m//10
print(c)


\\print first digit of a number
s=int(input(" "))
m=s
while m>0:
    r=m%10
    m=m//10
print(r)


\\\
s=input(" ")
print(s[0])


\\\



