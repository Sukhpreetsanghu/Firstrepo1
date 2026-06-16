print("="*20+""+"File handling"+""+"="*20)

print("="*20+""+"Question 1"+""+"="*20)
fruit = ["Mango \n","Apple\n ","Banana\n "]
with open("fruits.txt","w")as file :
    file.writelines(fruit)
    print("file written")

print("="*20+""+"Question 2"+""+"="*20)
try:
    with open("vegetables.txt","r")as file:
        file.read()

except FileNotFoundError :
    print("Not found")

print("="*20+""+"Question 3"+""+"="*20)
list2 =["Orange\n ","Strawberry\n"]
with open("fruits.txt","a")as file:
    file.writelines(list2)
    print("fruits added")

print("="*20+""+"Question 4"+""+"="*20)
with open("fruits.txt","r")as file:
    for lines in file:
        print("fruits {}".format(lines.strip()))

print("="*20+""+"Question 5"+""+"="*20)
try :
    num1 =10
    num2 = int(input("Enter number "))
    res = num1/num2
except ZeroDivisionError:
    print("Division error")
except ValueError :
    print("Invalid input")
else :
    print(f"the result is {res}")

finally:
    print("Finally exiited ")

print("="*20+""+"Question 6"+""+"="*20)

print("="*20+""+"part a"+""+"="*20)
my_colors = ["red", "blue", "green"]
student_info = {"name": "John", "grade": "A"}

try:
    print(my_colors[5])

except IndexError:
    print("Out of index")

print("="*20+""+"part b"+""+"="*20)
try:
    print(student_info["age"])

except KeyError :
    print("key not found")