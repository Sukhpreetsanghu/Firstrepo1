# Question 1
num = int(input("Enter number"))
sum =0
for i in range(num):
    sum +=i
print("Sum of number is ",sum)

for j in range(num):
    print(num ,"*",j,"=",num*j)

#Prime number 
for i in range (2,num):
    if num%i==0 :
        print("Not  a prime ")
        break
    
else :
        print("Number is prime")    
#FizzBuzz
for i in range(1,100):
  print(i)    
 
  if ( i%3==0 and i%5==0):
    print("FizzBuzz")   
  elif i%5 ==0:
    print("Buzz") 
  elif i%3 == 0:
    print("Fizz")
  
#Railway ticket Booking System
print("Welcome to CodeRail Railway Booking System 🚆")
name = input("Enter your name :")
age = int(input("Enter your age :"))
print("Choose travel class :\n1.First Class\n2.Second Class\n3.Sleeper Class")
choose = int(input("Enter choice(1/2/3):"))
meal = input("Do you want to add a meal? (yes/no):")
final_price =0
price1 = 1500
price2= 1000
price3 = 500
mealprice =200
print("\n----- Ticket Summary ----")
print("Pasanger Name :",name)
print("Age : ",age)
if age <= 5:
     if choose ==1:
      print("Class : First Class")
     elif choose ==2:
         print("Class: Second Class")
     elif choose == 3:
         print("Class : Sleeper class")
     print("final price :",final_price)
elif age >60:     
 if choose == 1:
     if meal =="yes":
          dmprice1 = price1*(20/100) +mealprice
          print("Meal Added : yes")
          print("Final price : " ,dmprice1)  
     else :
         print("Meal Added : no")
         print("Final price :",price1*(20/100))
 if choose == 2:
     if meal =="yes":
          dmprice2 = price2*(20/100) +mealprice
          print("Meal Added : yes")
          print("Final price : " ,dmprice2)  
     else :
         print("Meal Added : no")
         print("Final price :",price2*(20/100))
 if choose == 3:
     if meal =="yes":
          dmprice3 = price1*(20/100) +mealprice
          print("Meal Added : yes")
          print("Final price : " ,dmprice3)  
     else :
         print("Meal Added : no")
         print("Final price :",price3*(20/100))
else :
    if choose ==1:
        if meal == "yes":
            print("Meal Added : yes")
            print("Final price :",price1+mealprice)
        else:
            print("Meal Added : no")
            print("Final price :",price1)
    if choose ==2:
        if meal == "yes":
            print("Meal Added : yes")
            print("Final price :",price2+mealprice)
        else:
            print("Meal Added : no")
            print("Final price :",price2)
    if choose ==2:
        if meal == "yes":
            print("Meal Added : yes")
            print("Final price :",price2+mealprice)
        else:
            print("Meal Added : no")
            print("Final price :",price2)  
print("Enjoy your journey! 🎉")    
                     
#Burger king 
print("\n\nWelcome to Burger King 🍔!\n\nMenu:\n\n1. Whopper Burger - ₹150\n2. Crispy Veg - ₹100\n3. Chicken Wings - ₹120 ")

choice = int(input("Enter the item number (1/2/3):"))
quantity = int(input("\nEnter Quantity :"))
coupon = input("Do you have a coupon code? (yes/no): ")


print("Applying coupon...")
if choice ==1:
    print("Original Price:",150*quantity)
    if coupon =="yes":
     couponnum = input("Enter your coupon code:")

     if couponnum == "KING50":
        print("Discount applied :50%")
        fprice1 =(150*quantity)-(150*quantity*50/100)
        print("Final Price:₹",fprice1)
     elif couponnum =="BK20":
        print("Discount applied :20%")
        fprice2 = (150*quantity)-(150*quantity*20/100)
        print("Final Price:₹",fprice2)
     else :
        print("Coupon invalid") 
        print("Final Price:₹",150*quantity)
    elif coupon =="no":
       print("No coupon :No discount")
   
elif choice==2:
    print("Original Price:",100*quantity)
    if coupon =="yes":
     couponnum = input("Enter your coupon code:")

     if couponnum == "KING50":
        print("Discount applied :50%")
        fprice1 = (100*quantity)-(100*quantity*50/100)
        print("Final Price:₹",fprice1)
     elif couponnum =="BK20":
        print("Discount applied :20%")
        fprice2 = (100*quantity)-(100*quantity*20/100)
        print("Final Price:₹",fprice2)
     else :
        print("Coupon invalid") 
        print("Final Price:₹",100*quantity)
    elif coupon =="no":
       print("No coupon :No discount")
elif choice==3:
    print("Original Price:",120*quantity)
    if coupon =="yes":
     couponnum = input("Enter your coupon code:")

     if couponnum == "KING50":
        print("Discount applied :50%")
        fprice1 = ((120*quantity)-(120*quantity*50/100))
        print("Final Price:₹",fprice1)
     elif couponnum =="BK20":
        print("Discount applied :20%")
        fprice2 = ((120*quantity)-(120*quantity*20/100))
        print("Final Price:₹",fprice2)
     else :
        print("Coupon invalid") 
        print("Final Price:₹",120*quantity)
    elif coupon =="no":
       print("No coupon :No discount")

print("Thanks for ordering at Burger King! 🍟")

palindrome
a = input("Enter number")
if a== a[::-1]:
 print("Palindrome")  
else:
  print("Not a palindrome")



