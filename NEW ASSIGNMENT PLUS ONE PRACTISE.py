PERFECT NUMBER:

def check_perfect_number(number):
    sum1 = 0
    for i in range(1, number):
        if(number % i == 0):
            sum1 = sum1 + i
    if (sum1 == number):
        return True
    else:
        return False
def check_perfectno_from_list(no_list):
    l=[]
    for i in range(0,len(no_list)):
        if no_list[i]!=0 and check_perfect_number(no_list[i])==True:
            l.append(no_list[i])
        else:
            continue
    return l
   
perfectno_list=check_perfectno_from_list([18,6,4,2,1,28])
print(perfectno_list)



REMOVE DUPLICATE:


from collections import OrderedDict 
def remove_duplicates(value):
    return "".join(OrderedDict.fromkeys(value)) 
print(remove_duplicates("11223445566666ababzzz@@@123#*#*"))



practise 1:

def add_string(str1):
    if(len(str1)>=3):
        r='ing'
        if(str1[-3::]==r):
            str1+="ly"
        else:
            str1+="ing"
    return str1
str1="amazing"
print(add_string(str1))
