
def separate_section(title):
    print("\n" + "="*20 + " " + title + " " + "="*20)

separate_section("Lambda")
separate_section("1st Question")
#

prism = lambda l,h,w:l*h*w
print("Volume of rectangular prism :",prism(5,4,3))

separate_section("2nd Question")

enum = lambda num:"True"  if num%2==0 else "false"
print(enum(5)) 

separate_section("3rd Question")

str = lambda st : st[::-1]
print(str("Manjot is bad"))

separate_section("Map")

separate_section("Ques 1")
l =["15","42","7"]
convert = map(int,l)
print(list(convert))

separate_section("Ques 2")
lstr =["manjot","is ","mad","sanghu"]
convert_upper = map(lambda x:x.upper(),lstr)
print(list(convert_upper))

separate_section("Ques 3")
num = 1,2,3,4,5,6
sqr = map(lambda x:x**2,num)
print(list(sqr))

separate_section("Filter")


#filter(fun_name ,iterable)
separate_section("Ques 1")
l1 =[1,2,-2,0,5,-4]
positive_num = filter(lambda X:X>0,l1)
print(list(positive_num))

separate_section("Ques 2")
l2 =["Tanish","Manjot","Sukh","Dikshu","Ashish","Vivek"]
length_l2 = filter(lambda x:len(x)>5,l2)
print(list(length_l2))

separate_section("Ques 3")

x1 = ["sukh",5,4.3]


spec = filter(lambda x : not isinstance(x,(int,float)),x1)
print(list(spec))

separate_section("Enumerate")
separate_section("Ques 1")

# nset = {"apple", "orange", "banana"}
# for i,j in enumerate(nset,start=1):
#     print(i,j)
fruits = {"Watermelon","orange","Mango"}
for i,j in enumerate(fruits,start=1):
    print(i,j)
separate_section("Ques 2")
string = "Python"
for i,j in enumerate(string,start=1):
    print(i,j)

separate_section("Ques 3")
b_list = [True, False, True]
for i,j in enumerate(b_list,start=1):
    if j==True:
        print(i,j)


