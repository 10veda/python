String:
1.find occurance:
def o(a,c):
    f=0
    for i in range(0,len(a)):
        if c in a[i]:
            f+=1
    return f
a=input(" ")
c=input(" ")

print(o(a,c))
f=0


2,3.low-upper:
s=input(" ")
print(s.lower())
print(s.islower())
print(s.isupper())
print(s.upper())

\\\\count low and upper
def lu(s):
    u=0
    l=0
    for i in range(0,len(s)):
        if ord(s[i])>=97 and ord(s[i])<=122:
            l+=1 
        elif ord(s[i])>=65 and ord(s[i])<=90:
            u+=1
    return u,l
s=input(" ")
print(lu(s))

4.vowels:
a=input(" ")
r=0
for i in range(0,len(a)):
    if a[i]=="a" or a[i]=="A" or a[i]=="e" or a[i]=="E" or a[i]=="i" or a[i]=="I" or a[i]=="O" or a[i]=="O" or a[i]=="U" or a[i]=="u":
        r=r+1    
print(r)
    
5.locate substring:
h=input(" ")
f=input(" ")
r=h.find(f)
print(r)
if r==-1:
    print("not")
else:
    print("yes")
    
    
    \\\\new
    def g(a,b):
    for i in range(len(a)-len(b)+1):
        for j in range(len(b)):
            if a[i+j]!=b[j]:
                break
        if j+1==len(b):
            return i 
    return -1
a=input(" ")
b=input(" ")
print(g(a,b))
   
 6,1.count occurance of substring,character in a string:
 h=input(" ")
f=input(" ")
r=h.count(f)
print(r)


\\\
def g(a,b):
    c=0
    for i in range(len(a)-len(b)+1):
        for j in range(len(b)):
            if a[i+j]!=b[j]:
                break
        if j+1==len(b):
            c+=1  
            j=0
    return c
a=input(" ")
b=input(" ")
print(g(a,b))

7.reverse string:
n=input(" ")
p=" "
for  i in n:
    p=i+p
print(p)
    
    \\\
    n=input(" ")
print(n[::-1])
    
8.palindrome
n=input(" ")
s=n[::-1]
if n==s:
    print("Palindrome")
else:
    print("Not")
9.remove spaces
s=input(" ")
print(s.replace(" ",""))
print(s.strip())
print(s.lstrip())
print(s.rstrip())

9.remove vowels


def g(a):
    l=('a','e','i','o','u',"A","E","I","O","U")
    for i in a:
        if i in l:
            a=a.replace(i,"")
    return a
a=input(" ")
print(g(a))
