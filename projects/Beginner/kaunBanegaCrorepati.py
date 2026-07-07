#create a program capable of displaying questions to the user like KBS
#use list data type to store the questions and their correct answers
#display the final amount the person is taking home after playing the game 
questions=[["which language was used to create fb?","python","french","java","php",4],
           ["Who developed Python programming language?","Dennis Ritchie", "James Gosling", "Guido van Rossum", "Bjarne Stroustrup", 3],
           ["Which data type is immutable in Python?", "List", "Dictionary", "Set", "Tuple", 4]]
levels=[1000,2000,3000]
money=0
for i in range (0,len(questions)):
    question=questions[i]
    print(f"Questions for Rs.{levels[i]}")
    print(question[0])
    print(f"a.{question[1]}        b.{question[2]}")
    print(f"c.{question[3]}        d.{question[4]}")
    reply=int(input("Enter your answer(1-4)"))
    if(reply==question[5]):
        print(f"Correct answer ,you have won rs.{levels[i]}")
        money=levels[i]
    else:
        print("wrong answer!")
        break
print(f"\nGame Over. You won Rs.{money}")