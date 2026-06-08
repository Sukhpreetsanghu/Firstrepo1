#1 set question
#
s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print("The set is:", s1)
#
s1.update([11,14,10])
print("The updated set is:", s1)
#
s1.remove(2)
print("The set after removing 2 is:", s1)
s1.discard(3)
print("The set after discarding 3 is:", s1)

#union and intersection
s2 = {1, 2, 3, 4, 5}
s3 = {4, 5, 6, 7, 8}
print("The union of the two sets is:", s2 | s3)
print("The intersection  :",s2 & s3)

#
print("The difference of s2 and s3 is:", s2 - s3)

if 5 in s2:
    print("5 is present in s2")
else:    print("5 is not present in s2")

#
list1 = [1, 2, 3, 4, 5,5]
print("The list is:", list1)
#convert list to set
set1 = set(list1)
print("The set is:", set1)


#Question 2
#
t = ("English", "Maths", "Science", "Social Studies", "Computer Science")
print("The tuple is:", t)

#
for i in t:
    print(i)
print("The length of the tuple is:", len(t)) 
#
t1 = ("History", "Geography")
t2 = t + t1
print("The concatenated tuple is:", t2)


#Question 3
#
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s=[]
s = [i**2 for i in numbers]
print("The squares of the numbers are:", s)
#
p =[]
p = [i for i in range(1, 20) if i%2==0]
print("The list of even numbers is:", p)
#
s1 = ["string1", "string2", "string3"]
su=[]
su = [i.upper() for i in s1]
print("The uppercase strings are:", su)
#
words = ["apple", "banana", "cherry", "date", "elderberry"]
l = []
l= [len(i) for i in words]
print("The lengths of the words are:", l)
#
div =[]
div =[i for i in range(1,100)if i%2==0 and i%5==0]
print("The numbers divisible by 2 and 5 are:", div)

#
s = "Hello World"
no_vowels = ([i for i in s if i not in ('a','e','i','o','u','A','E','I','O','U')])
print("The string without vowels is:", no_vowels)
#
table =[]
table = [i*5 for i in range(1,11)]
print("The multiplication table of 5 is:", table)
#
ns = [(i,2**i) for i in range(0,10)]
print(ns)
