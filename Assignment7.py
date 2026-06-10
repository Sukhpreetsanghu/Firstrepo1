#ques 1
def sep(title):
    print("\n"+"="*20+""+title+""+"="*20)

sep("1st Question")
import random 
import string

def generate_password():
    teri = string.ascii_letters+string.digits 
    password = "".join(random.choice(teri) for i in range(8) )
    return password
print(generate_password())

#ques 2
sep("2nd Question")
def calculate_bmi(weight_kg, height_m):
    return weight_kg/(height_m**2)

print("Body Mass Index is ",calculate_bmi(75,1.79))

#ques 3
sep("3rd Question")
def book_flight(destination , class_type = 'Economy'):
      return (destination,"confirming booking for ",class_type)


destination = input("Enter destination ")
class_type = input("Enter class")

if class_type == '':
 print(book_flight(destination ))
else :
    print(book_flight(destination,class_type))

#ques 4
sep("4th Question")
def create_profile(username, age, country='Unknown'):
    return{f"username:{username},age:{age}country :{country}"}


age = int(input("Enter age "))
country = input("Enter country")
username = input("Enter username ")

if country=='':
 print(create_profile(username,age))
else :
   print(create_profile(username, age, country))


#Ques 5
sep("5th Question")
def concatinate_words(*words):
      return "-".join(words)

print(concatinate_words("Manjot ","Sandhu","is","Mad"))

#Ques 6
sep("6th Question")
def build_configuration(**settings):
      for i,j in settings.items():
       print(f"{i}:{j}")
      
build_configuration(theme='dark', debug=True, max_users=100)