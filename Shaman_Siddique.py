#printing the start of quiz.
print("              !--Welcome to the Quiz--!")
print("Here are some questions.Answer all of them correctly to win.")
#SHAMAN SIDDIQUE - 3 - QUIZ

#Questions 
q1= "(i) cos0 = ?"
q2= "(ii) tan45 = ?" 
q3= "(iii) 360/6 = ?"
q4= "(iv) 5*5 = ?"
q5= "(v) 210+7 = ?"

#dictionary giving the answers of question given above.
questions = {q1:"1", q2:"1", q3:"60", q4:"25", q5:"217" }

score=0
#conditions to check if the answer inputed by the user is same as given in dictionary.
for i in questions:
    print(i)
    answer = input("Answer: ") 
    if answer==questions[i]:
        #after checking if answer is correct it adds 1 to the score
        score+=1
        print("Correct")
    else:
        print("Wrong")
        
#conditons to check if sum of score adds upto 5.     
if score==5:
    print("YOU WIN")
else:
    print("YOU LOSE")
        

 

