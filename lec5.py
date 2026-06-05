#Tuples
#immutable datatye
#ordered pairs
#it allows duplicates
from operator import index


example_tuple = (1, 2, 3, 4, 5)
print(example_tuple)
a=(10)
b =1,2,3,4,5
c=(1,)
print(type(a))
print(type(b))
print(type(c))


t= (1,2,3,4,3,3,3,3,5)
print(t.count(3))
print("Length is", len(t))
print(t.index(3))

t1 = (1,2,3,4,5)
t2 = (6,7,8,9,10)
t3  = t1 + t2
print(t3)