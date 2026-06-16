def Add():
  
    ques = input("Enter question ")

    choices = []   

    for i in range(4):  
     choice = input(f"Enter choice {i}: ")
     choices.append(choice)

    print("Choices entered:", choices)

    correct = input("Enter correct choice :")
    l1 = {"ques": ques, "choices": choices, "correct": correct}
    return list_Quiz.append(l1)
  

def Print_list():
     for i,j in enumerate(list_Quiz,start=1):
         print(f"{i}.{j}")
        
def update_Quiz():
            index_update = int(input("Enter index to update :"))
            Uchoices = []
            if 0<= index_update <= len(list_Quiz) :
             
                 
              Uques = input("Enter  updated question ")
              for i in range(4):
                    Uchoice = input(f"Enter choice {i}: ")
                    Uchoices.append(Uchoice)  
              Ucorrect = input(f"Correct answer :")
              
              l3 = f"{Uques}\n{Uchoices}\ncorrect answer is {Ucorrect}"               
              list_Quiz[index_update]=l3
              print("Updated")
        
        
def play_Quiz():
        print("="*20+""+"Quiz started"+""+"="*20)
        for i,j in enumerate(list_Quiz,start=1):
             print(f"{i}.{j['ques']}\n{j['choices']}")
             user_choice = input("Enter your choice : ")   
             if user_choice ==j["correct"]:
               print("Correct")
               score+=1
             else :
               print("Wrong answer")
        
        print(f"\nYour final score: {score}/{len(list_Quiz)}")

def Delete_List():
     delete_index = int(input("Enter index to delete "))
     if 0<= delete_index<= len(list_Quiz):
          list_Quiz.pop(delete_index)
   
def Quit():
       print("="*20+""+"thank you"+""+"="*20)


list_Quiz = []
score =0
def main():
    while True :
        print("="*20+""+"Quiz Management"+""+"="*20)
        print("1. Add Quiz")
        print("2. List Quiz")
        print("3. Update Quiz")
        print("4. Play Quiz")
        print("6. Exit")
        
        

        choice = input("Enter your choice")

        if choice == "1":
           Add()
           print(list_Quiz)

        elif choice == "2":
            Print_list()
        
        elif choice == "3":
            update_Quiz()
           
        elif choice =="4":
            play_Quiz()
             
        elif choice =="5":
             Delete_List()

        elif choice=="6":
            Quit()
            break
main()

