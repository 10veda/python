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




RawBlameHistory
  
#PF-Prac-21
def check_numbers(num1,num2):
    #start writing your code here
    num_list=[]
    for i in range(num1,num2+1):
        for j in range(num1,num2+1):
            if(i%j==0 and i not in num_list and i!=j):
                num_list.append(i)
    count=len(num_list)
    return [num_list,count]

num1=2
num2=20
print(check_numbers(num1, num2))


'''
Write a python function to print the given number of diagonal lines of stars.
Sample input: 5
Expected output: 
* 
.* 
..* 
...* 
....* 
Note: Setting the end parameter of the print function to empty string prevents the issuing of the new line.
Example: print(".",end="") will maintain the cursor in the same line after displaying "."
'''

#PF-Tryout 22
def diagonal_stars(number):
   #start writing your code here
    for i in range(0,number):
        for j in range(i):
            print(".",end="")
        print("*")

number=6    
diagonal_stars(number)


#PF-Prac-23
def divisible_by_sum(number):
    temp=number
    sum=0
    while(number>0):
        rem=number%10
        number=number//10
        sum+=rem
    if(temp%sum==0):
        return True
    else:
        return False


#PF-Prac-24
def find_gcd(num1,num2):
    if(num2==0): 
        return num1
    else:
        return find_gcd(num2,num1%num2)

num1=45
num2=9
print(find_gcd(num1,num2))


#PF-Prac-25
def list_of_count(word_list):
    count_list=[]
    for i in word_list:
        count_list.append(len(i))
    return count_list

word_list=["COme","here"]
print(list_of_count(word_list))


#PF-Prac-26
def check_occurence(string):
    string=string.lower()
    c=string.count("mat")
    cc=string.count("jet")
    if(c==cc):
        return True
    else:
        return False
        
string="Jet on the Mat but mat is too long"
print(check_occurence(string))


#PF-Prac-27
def check_for_ten(num1,num2):
    if(num1==10 or num2==10 or num1+num2==10):
        return True
    else:
        return False
    
print(check_for_ten(10,9))


#PF-Tryout 28
def sing_99_bottles():
   for i in range(99,0,-1):
        print(i,end="")
        print(" bottles of beer on the wall, ",end="")
        print(i,end="") 
        print(" bottles of beer.")
        print("Take one down, pass it around, ",end="")
        print(int(i-1),end="")
        print(" bottles of beer on the wall.")
   
sing_99_bottles()


#PF-Prac-29
def exchange_list(number_list):
    #start writing your code here
    d=len(number_list)
    a=len(number_list)//2
    b=a//2+a
    k=0
    for i in range(a,b):
        c=number_list[i]
        number_list[i]=number_list[d-k-1]
        number_list[d-k-1]=c
        k=k+1
    for i in range(a):
        temp=number_list[i]
        number_list[i]=number_list[i+a]
        number_list[i+a]=temp
    return number_list

    
     
number_list=[1,2,3,4,5,6]
print(exchange_list(number_list))
    
    
#PF-Prac-31
def sum_of_elements(num_list,number):
    a=len(num_list)
    result_sum=0
    for i in range(1,a-1):
        if(num_list[i-1]!=number and num_list[i+1]!=number and num_list[i]!=number):
            result_sum+=num_list[i]
    if(num_list[1]!=number and num_list[0]!=number):
        result_sum+=num_list[0]
    if(num_list[a-2]!=number and num_list[a-1]!=number):
        result_sum+=num_list[a-1]
    return result_sum
      
num_list=[1,2,1,2]
number=2
print(sum_of_elements(num_list, number))


#PF-Prac-37
def sum_of_list(num_list):
    if(len(num_list)>1):
        return num_list[0] + sum_of_list(num_list[1:])
    else:
        return num_list[0]
num_list=[44,23,77,11,89,3]
result=sum_of_list(num_list)
print("Sum of the elements:",result)


#PF-Prac-38
def build_index_grid(rows, columns):
    result_list=[]
    s=""
    for i in range(0,rows):
        for j in range(0,columns):
            if(i==0 and j==0):
                s=s+"["
            if(j==0):
                s=s+"["
            s=s+"'"+str(i)+","+str(j)+"'"
            if(j!=(columns-1)):
                s=s+","
            if(j==(columns-1) and j==(columns-1) and i!=(rows-1)):
                s=s+"],"
            if(j==(columns-1) and i==(rows-1)):
                s=s+"]]"
        result_list.append(s)
        s=""
    return result_list

rows=4
columns=3
result=build_index_grid(rows,columns)
print("Rows:",rows,"Columns:",columns)
print("The matrix is:",result)
for i in result:
    print(i)























    
    
