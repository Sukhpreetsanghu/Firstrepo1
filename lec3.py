
# write a program print the table using for loop
# num = int(input("Enter number "))
# for i in range(11) :
#     print(f"{num} x {i} = {num*i}")
    #Star pattern
# n = int(input("Enter number of rows "))
# for i in range(0,n):
#     for j in range(i+1):
#         print("*", end="")
#     print(" "* (2*(n-i)), end="")  
#     print("*"*(i+1))

# for i in range(n-2,-1,-1):
#     for j in range(i+1):
#         print("*", end="")
#     print(" "* (2*(n-i)), end="")      
#     print("*"*(i+1))

     
# bottom pattern        
# for i in range(n-1,0,-1):
#     for j in range(i):
#         print("*", end="")
#     print()  

# for i in range (n):
#     for j in range (n-i):
#         print(" ", end="")
#     for k in range (i+1):
#         print("*", end="")
#     print()
num = 5
n = 1
for i in range (num):
  for j in range(i+1):
     n+=1
     print(n,end="")
  print()       


  
s ="      Hello i am here"
print(s)
#split
print(s.split(' '))
print(s.strip())
print(s.lstrip())
print(s.rstrip())