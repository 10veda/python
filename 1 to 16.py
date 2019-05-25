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



PRACTISE 2

def bracket_pattern(input_str): 
    open_tup = tuple('({[') 
    close_tup = tuple(')}]') 
    map = dict(zip(open_tup, close_tup)) 
    queue = [] 
    for i in input_str: 
        if i in open_tup: 
            queue.append(map[i]) 
        elif i in close_tup: 
            if not queue or i != queue.pop(): 
                return "False"
    return "True"
input_str = ")()((()())"
print(bracket_pattern(input_str)) 

PRACTISE 4:
    
    def find_nine(nums):
    for i in range(0,len(nums)):
        if(i<4):
            if(nums[i]==9):
                return True
    return False           
nums=[1,8,4,5,6]
print(find_nine(nums))


PRACTISE 5

def count_digits_letters(sentence):
    count1=0
    count2=0
    result_list=[]
    for i in sentence:
        if(i.isdigit()):
            count1=count1+1
        if(i.isalpha()):
            count2=count2+1
    result_list.append(count2)
    result_list.append(count1)
    return result_list
sentence="Infosys Mysore 570027"
print(count_digits_letters(sentence))




PRACTISE 6:
    
    def list123(nums):
    for i in range(0,len(nums)-1):
        if (nums[i]==1 and nums[i+1]==2 and nums[i+2]==3):
            return True
        else:
            return False
nums=[1,2,3,4,5]
print(list123(nums))


#PF-Prac-7
def seed_no(number,ref_no):
    t=number
    while(number!=0):
        rem=number%10
        t*=rem
        number//=10
    if(t==ref_no):
        return True
    else:
        return False
    
number=123
ref_no=738
print(seed_no(number,ref_no))


#PF-Prac-8
def calculate_net_amount(trans_list):
    net_amount=0
    for i in trans_list:
        a=[]
        a=i.split(":")
        if(a[0]=='D'):
            net_amount+=int(a[1])
        else:
            net_amount-=int(a[1])
    
    return net_amount

trans_list=["D:300","D:200","W:200","D:100"]
print(calculate_net_amount(trans_list))


#PF-Prac-9
def generate_dict(number):
	#start writing your code here
	new_dict={}
	for i in range(1,number+1):
	    new_dict[i]=i**2

	
	return new_dict

number=10
print(generate_dict(number))


#PF-Prac-10
def string_both_ends(input_string):
	if(len(input_string)<2):
	    return -1
	else:
	    s=""
	    s=input_string[0:2]+input_string[len(input_string)-2:len(input_string)]
	    return s

input_string="w3"
print(string_both_ends(input_string))



#PF-Prac-11
def find_upper_and_lower(sentence):
    #start writing your code here
    up=0
    lo=0
    for i in sentence:
        if(i>="a" and i<="z"):
            lo+=1
        if(i>="A" and i<="Z"):
            up+=1
    result_list=[]
    result_list.append(up)
    result_list.append(lo)

    return result_list

sentence="Come Here"
print(find_upper_and_lower(sentence))


#PF-Prac-12
def generate_sentences(subjects,verbs,objects):
    sentence_list=[]
    for i in subjects:
        for j in verbs:
	        for k in objects:
	            sentence_list.append(i+" "+j+" "+k)
    return sentence_list

subjects=["I","You"]
verbs=["love", "play"]
objects=["Hockey","Football"]
print(generate_sentences(subjects,verbs,objects))


#PF-Prac-13
import math

def close_number(num1,num2,num3):
    if math.fabs(num1-num2)==1 and math.fabs(num3-num2)>=2 and math.fabs(num3-num1)>=2:
        return True
    elif math.fabs(num3-num2)==1 and math.fabs(num1-num2)>=2 and math.fabs(num3-num1)>=2:
        return True
    elif math.fabs(num1-num3)==1 and math.fabs(num3-num2)>=2 and math.fabs(num2-num1)>=2:
        return True
    else:
        return False
    
print(close_number(5,4,2))


#PF-Tryout 14
def find_five_digit():
    num2=0
    num3=0
    num4=0
    num5=0
    for i in range(9,-1,-1):
        num2=int(i-2)
        num3=int(num2-2)
        num4=int(num3-2)
        num5=int(num3)
        if(num3+num4+num5==i and num2+num3+num4+num5+i==19):
            break
    s=str(i)+str(num2)+str(num3)+str(num4)+str(num5)
    print(s)

find_five_digit()


#PF-Prac-15
def check_22(num_list):
    for i in range(0,len(num_list)-1):
        if(num_list[i]==2 and num_list[i+1]==2):
            return True
    return False
        
print(check_22([3,2,5,1,2,1,2,2]))


#PF-Prac-16
def rotate_list(input_list,n):
    output_list=[]
    for i in range(len(input_list)-n,len(input_list)):
        output_list.append(input_list[i])
    for i in range(0,len(input_list)-n):
        output_list.append(input_list[i])
    return output_list

input_list= [1,2,3,4,5,6]
output_list=rotate_list(input_list,4)
print(output_list)



