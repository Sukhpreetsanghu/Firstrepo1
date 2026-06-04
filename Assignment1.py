#Question 1
a = int(input("Enter number between 1 to 12 "))
if a== 1 :
    print("January")
elif a== 2 :
    print("February")
elif a== 3 :
    print("March")
elif a== 4 :
    print("April")
elif a== 5 :
    print("May")
elif a== 6 :
    print("June")
elif a== 7 :
    print("July")
elif a== 8 :
    print("August")
elif a== 9 :
    print("September")
elif a== 10 :
    print("October")
elif a== 11 :
    print("November")
elif a== 12 :
    print("December")
       
# Question 2
a = int(input("Enter number 1 "))
b = int(input("Enter number 2 "))       
ans1 = "Numbers are not equal " if a!=b else "Equal"
print(ans1)
ans2 = "Number 1 is greater  " if a>b else "Number 2 is greater "
print(ans2)
ans3 = " either Number 1 is smaller or equal to second number  " if a<=b else "Number 2 is smaller "
print(ans3)
if a>b :
   
      print (5*"Sukhpreet")
else :
        print(3*"Sanghu")


#Question 3 

input1 = input("Enter input 1 ")
input2 = input("Enter input 2 ")
if input1 == input2 :
    print("Both are equal ")
else :
    print("Not equal") 
print(input1 is input2)       

#Question 4 

str1 = input("Enter first number as string: ")
str2 = input("Enter second number as string: ")

num1 = int(str1)
num2 = int(str2)


if num1 is num2:
    print("Both numbers are equal (same object).")
else:
    print("Numbers are not equal (different objects).")

#Question 5
num = int(input("Enter number "))
sum =0
for i in range(num +1):
   
    sum = sum + i
   
print(sum)

#Question 6
num = int(input("Enter number "))

for i in range(num) :
    if i%2==0 :
     print("Even are ", " ", i)



a = int(input("Enter num"))
a = input("Enter name")