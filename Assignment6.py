#Ques 1
sentence = input("Enter a sentence: ")
words = sentence.split()
print(words)
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
sorted_freq = dict((freq.items()))
print(sorted_freq)

#Ques 2
n = int(input("Enter number of students "))
student ={input("Enter Student name :"):int(input("Enter marks :"))for i in range (n)}
print(student)
av = sum(student.values())/n
print("Average marks obtained :",av)
for name, score in student.items():
    if score > av:
        print(name, "has marks greater than average marks")

#Ques 3
dic1 = {'a': 50, 'b': 30, 'c': 70}
dic2 = {'b': 60, 'c': 65, 'd': 40}
merge = dic1.copy()
for i,j in dic2.items():
    merge[i] = max(merge.get(i,j),j)
print(merge)

#ques 4
dic = {'name': 'Alice', 'city': 'Bangalore', 'course': 'Data Science'}
max_value =0
max_key =None
for i,j in dic.items():
    if len(j) > max_value:
        max_value = len(j)
        max_key = i
print(i)

#ques 5

dic1 = {"num1":20,"num2":40,"num3":2,"num4":200,"num5":27,"num6":65,"num7":49,"num8":44}

ndic ={}
ndic = {i:j for i,j in dic1.items() if j>10 and j<50}
print(ndic)

#ques 6

voters = int(input("Enter number of voters "))
votes ={}
for i in range(voters):
 count = input(f"Choose candidate {i+1}:")
 votes[count]= votes.get(count,0)+1

print("Vote counting")
for i,j in votes.items():
  print(i,":",j)

Highscore =0
Winner =None
for i,j in votes.items():
    if j > Highscore:
        Highscore = j
        Winner = i
print("Winner is ",Winner)

#ques 7

data = {'a': 10, 'b': 20, 'c': 30}
update = {'b': 200, 'c': 300}

for i,j in update.items():
   data[i] =max(data.get(i,j),j)
print(data)






 


   
     
      

