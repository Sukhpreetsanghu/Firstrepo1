l1 =[ { "name": "Forrest Gump", "year": 1994, "duration": 142, "genres": ["Drama", "Romance"] },
{ "name": "Avengers: Endgame", "year": 2019, "duration": 181, "genres": ["Action",
"Adventure", "Drama"] }, { "name": "Back to the Future", "year": 1985, "duration": 114,
"genres": ["Adventure", "Comedy", "Sci-Fi"] } ]
   
def input_int(prompt):
    while True:
            value = int(input(prompt))   
            if value >= 1:
                return value
            else:
        
             print("Invalid input. Please enter an integer.")

def input_something(prompt):
    while True:
        value = input(prompt).strip()
        if value:   
            return value
        else:
            print("Please enter something valid (not empty).")



print("="*20+""+"Welcome"+""+"="*20)
print("Choose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.")
while True:
  choice = input("Enter your choice :")
  if choice=='a':
   mname = input("Enter movie name :") 
   genre = input("Enter genre :")
   year = int(input("Enter year :"))
   duration = int(input("Enter duration :"))

   movies = {"name":mname,"year":year,"Duration":duration,"genres":genre}
   l1.append(movies)
   print("Added succesfully")
  

  elif choice =='l':
     
     for i,l1 in enumerate(l1,start=1):
      print(f"{i}.{l1['name']},{l1['year']}")

  elif choice =='s':
      srch = input("Enter movie to search :").strip().lower()
      for i,l1  in enumerate(l1,start=1):
       if srch in l1['name'].lower() :

        print(f"{i}.{l1['name']},{l1['year']}")
   

  
  elif choice =='v':
     view = int(input("Enter index number to view :"))
     for i,l1  in enumerate(l1,start=1):
           if view == i :

             print(f"{i}.{l1['name']},{l1['year']}")
  
  elif choice == 'd':
      delete = int(input("Enter index number to delete :"))
      if delete <=0:
       print("invalid")
      else : 
       d = l1.pop((delete -1))
       print(d,"Deleted ")
  
  
  elif choice == 'q':
       print("="*20+""+"thank you"+""+"="*20)
       break
     

     