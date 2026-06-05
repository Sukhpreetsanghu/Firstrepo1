#question 1
name = input("Student name ")
sclass = int(input("Student class "))
sec = input("Student sec ")

maths = int(input("Enter marks of mathematics "))

Punjabi = int(input("Enter marks of  Punjabi "))

English  = int(input("Enter marks of English "))

Hindi= int(input("Enter marks of Hindi "))

Science = int(input("Enter marks of Science "))
total_marks = maths + Punjabi +English + Hindi+Science

percentage = (total_marks/500)*100
#print("Name " ,name ,"Class  " , sclass ,"Section ", sec)
print(f"Name : name Class : {sclass}    Section : {sec} ")
print(f"Marks : \nMathematics {maths}\nPunjabi {Punjabi}\nEnglish {English}\nHindi {Hindi}\nScience {Science}\nTotal Marks {total_marks}\nPercentage {percentage} ")

#question 2 
num1 = int(input("Enter num 1"))
num2 = int(input("Enter num 2"))
num3 = int(input("Enter num 3"))
total_sum = num1+num2+num3 
print(f"Total sum of three {total_sum}")

#question 3 
num = int(input("Enter num "))
sq = num*num
print(f"Square of {num} is {sq}")
cel = int(input("Enter value in celcius "))
cels =float(cel)
farh = (cels*9/5)+32
print(f"Temperature in celcius {cels} and temperature in fahrenheit {farh}")


# #question 4
a = int(input("Enter num 1"))
b = int(input("Enter num 2"))
rem = a%b
if b!=0:
   quo = a/b
   print(f"Reminder is {rem} and Quotient is {quo}")

#Question 5
P = int(input("Enter principal "))
R = int(input("Enter Rate "))
T = int(input("Enter time "))
SI = (P*R*T)/100
print(SI)

