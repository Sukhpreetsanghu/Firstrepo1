#Question 1
l = ["Sukh","Tanish","Dikshuuuu","Ashish","Vivek"]
name = input("Enter the name to add : ")
l.append(name)
print(l)
favorite_name = input("Enter the name of your favorite person : ")
if favorite_name in l:
    l.remove(favorite_name)
    l.insert(0, favorite_name)
    print(l)
l.extend(["Raju"])
print(l)
print(l.index("Index of favorite person: " + favorite_name))

#Question 2
l= []
for i in range(1, 11):
    l.append(i)
print(l)

#question 3
l = [1,10,100,3,6,8]
l.insert(3,59)
l.append(5)
print(l)
print(len(l))

#question 4
l= ["Ram","Tanish","Dikshuuuu","Ashish","Vivek"]
print(l)
for i in l:
  
    if len(i)  <4:
        print(i)

# #question 5
l=[]
for i in range(1,20):
    if i%2==0:
        i="Even"
        l.append(i)
      

       
    else:
        i="Odd"
        l.append(i)
print(l)

#question 6
l=[]
for i in range(1,1000):
    if i%7==0:
        l.append(i)
print(l)

#question 7
s = "Hello World Welcome to Python"
print("Number of spaces:",s.count(" "))

#question 8
a = [1,2,3,4]
b=[2,3,4,5 ]
l = []
for i in a:
    if i in b:
        print(i)
        l.append(i)
print(l)        
