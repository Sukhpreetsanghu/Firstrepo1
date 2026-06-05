#sets
# mutable
# unordered and unindexed
# no duplicate values
# defined with {}curly brackets
#store hetrogeneous data

# a ={}#by default it is a dictionary
# c = set()#empty set
# b ={12}
# print(type(a))
# print(type(b))
# print(type(c))
# s1 = {25,"jatin",53,25,"jatin"}
# print(s1)
# for i in s1:
#     print(i,end=" ")
# s1.add("Ashish")
# print(s1)
# s1.update([23,45,67])
# print(s1)

# s2 = {23,45,67}
# #removing the element from th set 
# s2.pop()#removes the random element from the set
# print(s2)
# s2.remove(45)#removes the specified element from the set if not present give error
# print(s2)
# s2.discard(45)#removes the specified element from the set if it is present otherwise do nothing
# print(s2)

#common set operations
s3 = {1,2,3,4,5}
s4 = {4,5,6,7,8}
print(s3|s4)#prints the union of two sets
print(s3&s4)#prints the intersection of two sets
print(s3-s4)#prints the difference of two sets
print(s3^s4)
# print(s3.union(s4))#prints the union of two sets
# print(s3.intersection(s4))#prints the intersection of two sets
# print(s3.difference(s4))#prints the difference of two sets
# print(s4.difference(s3))#prints the difference of two sets
#frozenset

f = frozenset([1,2,3,4,5])#immutable set
print(f)
