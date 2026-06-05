#list
# insert
l1 = [12,45,34,78,23]
# l1.insert(1,44)
# print(l1)
# l1.insert(1,[44])
# print(l1)

#append
# l1.append(23)
# print(l1)
# l1.append([24,25])
# l1.extend([25,34])
# print(l1)

# #remove and pop
# l1.pop()
# l1.pop(2)
# print(l1)




# # for i in l1:
# #     print(i+4)
# #     print(l1)

# a =[2,3,4,5]
# b =[1,2,3,4,7]
# for i,j in zip(a,b):
#     print(i,"=",j)

# #string list

# l=["Hello","How","Are","you"]
# print(" ".join(l))
# new =[]
# for i in a:
#     if i in b:
#         new.append(i)
# print(new)

 #list comprehension
number =[1,2,3,4,5]
s=[]
s=[number**2 for number in number]
print(s)
name = ["Ram","Shyam","Sita","Gita"]
s=[names.upper() for names in name]
print(s)

number = [1,2,3,4,5,6,7,8,9,10]
s=[("Even" if numbers%2==0 else "Odd") for numbers in number]
print(s)

l=[21,56,12,-12,15,-25,-30,58,-9,28,-18]
positive =[(i if i>0 else 0) for i in l]
print(positive)

num = [4,5,6,7,8]
s11 = [i  for i in num if i**2>50]
print(s11)

words=["apple","elephant","banana","dog","computer","cat"]
s12 = [i for i in words if len(i)>5]
print(s12)

