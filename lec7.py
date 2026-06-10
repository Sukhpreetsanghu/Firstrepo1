def add():
    a=30
    b=46
    print(a+b)

add()

def add(a,b):
    return a+b

print(add(20,70))


def multiplication(a,b=5):
       print(a*b)

multiplication(5,6)




#keyword arguments

def sub(a=1,b=3,c=5):
     d= a +b-c 
     return(d)

print(sub(a=10,b=30,c=10))

#args*
def add(*a):
     sum =0
     for i in a:
      sum+=i
     return sum    

print(add(1,3,3,4,))



def sub(**b):
    total =100000
    for i in b.values():
        total -= i
        return total
    
print(sub(a=123,b=456,c=987,d=456))



