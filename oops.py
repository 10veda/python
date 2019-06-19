https://docs.python.org/3/library/functions.html#id



Exercise:1

def purchase_mobile(price,brand):
    if brand == "Apple":
        discount = 10
    else:
        discount = 5
    total_price = price - price * discount / 100

    print("Total price of Mobile is "+str(total_price))

def purchase_shoe(price,material):
    if material == "leather":
        tax = 5
    else:
        tax = 2
    total_price = price + price * tax / 100

    print("Total price of Shoe is "+str(total_price))

purchase_mobile(20000,"Apple")
purchase_shoe(200,"leather")


#OOPR-Exer-3
#Start writing your code here
class Employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Salary:",self.salary)
c1=Employee("Jack",24,30000)
c2=Employee("Jill",27,40000)
c1.display()
c2.display()
        


#OOPR-Exer-4
class Athlete:
    def __init__(self,name,gender):
        self.__name=name
        self.__gender=gender

    def running(self):
        if(self.__gender=="girl"):
            print("150mtr running")
        else:
            print("200mtr running")
a=Athlete("Maria","girl")
a.running()


#OOPR-Assgn-8 error
#Start writing your code here

class student:
    def __init__(self,student_id,marks,age):
        self.__student_id=student_id
        self.__marks=marks
        self.__age=age
    def validate_marks(self):
            if self.__marks>=0 and self.__marks<=100:
                return True 
        else:
            return False 
    def validate_age(self):
        if self.__age>20:
            return True
        else:
            return False
    def check_qualification():
        if validate_age()==True and validate_marks==True:
            if self.__marks>=65:
                return True
            else:
                return False
        else:
            return False
c=student()
        
