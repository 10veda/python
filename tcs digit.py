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


EXTRACT DIGIT

n=input(" ")
s=" "
for i in range(0,len(n)):
    if n[i]=="-" or n[i]=="0" or n[i]=="1" or n[i]=="2" or n[i]=="3" or n[i]=="4" or n[i]=="5" or n[i]=="6" or n[i]=="7" or n[i]=="8" or n[i]=="9":
        s+=n[i]
print(s)

