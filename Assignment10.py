print("+"*20+""+"Question 1"+""+"+"*20)

class dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age


bark = dog("oskar",7)
print(f"Woof!My name is {bark.name}and age is {bark.age}")

print("+"*20+""+"Question 2"+""+"+"*20)

class school:
    school_name = "Python Academy "
    def __init__(self,student_name):
        self.student_name =student_name


s1 = school("Sukhpreet")
s2 = school("Manjot")
print(f"School name is {school.school_name} and students names are {s1.student_name} and {s2.student_name}")





print("+"*20+""+"Question 3"+""+"+"*20)

class BankAccount:
    def __init__(self,owner,balance=0):
       self.owner = owner 
       self.balance = balance
    def deposit(self,amount):
        self.balance +=amount

    def withdraw(self,amount):
        self.balance -=amount

account = BankAccount("Sukhpreet")

account.deposit(100)
account.withdraw(70)
print(account.owner ,":",account.balance)

print("+"*20+""+"Question 4"+""+"+"*20)

class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
         self.items =[]

    def add_item(self,product):
        self.items.append(product)

p1 = Product("Shirt",200)
p2= Product("T-shirt",150)
cart = ShoppingCart()
cart.add_item(p1)
cart.add_item(p2)

for i in cart.items  :
    print(f"{i.name}:{i.price}")     


print("+"*20+""+"Question 5"+""+"+"*20)

class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width*self.height
    def calculate_parameter(self):
        return (2*(self.width+self.height))
    
r = Rectangle(5,10)
print("Area of rectangle is",r.calculate_area() ,"and perimeter of rectangle is ",r.calculate_parameter())
        

