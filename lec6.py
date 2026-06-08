#dictionary
d1 = {"name":"sachin","age":45,"country":"india"}
print(d1["age"])    
d1.update({"age":46})
print(d1)
d1.pop("country")
print(d1)

print(d1.get("country","Not found "))
print(d1.keys())
print(d1.values())
print(d1.items())

dic2 = {"name":{"first":"sachin","last":"tendulkar"},
        "age":45}
print(dic2["name"]["first"])

#dictionary comprehension

dic3 = {i**2:i for i in range(10)}
print(dic3)

dic4 = {i:("Even " if i%2==0 else "Odd") for i in range(10)}
print(dic4)


l1 = [1,2,3,4,5]
l2 = ["one","two","three","four","five"]
dic5 ={i:j for i,j in zip(l1,l2)}
print(dic5)


#user input in dictionary  comprehension
# value stored in dictionary are of string type
#key can be of any immutable data type


n = int(input("Enter the number of items in the dictionary: "))
user_dict = {input("Enter key: "): input("Enter value: ") for i in range(n)}
print("The user-defined dictionary is:", user_dict)   


