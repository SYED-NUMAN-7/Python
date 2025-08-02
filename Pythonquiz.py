questions = ("Who is the Father of the Nation ? : ",
             "Who is the Rocket Man of India ? : ",
             "Who is First Prime Minister of the India ? : ",
             "What is the Capital of China ? : ",
             "How many Elements are their in periodic table ? : ")

options = (("A.Nelson Mandela","B.Mahatma Gandhi","C.Rahul Gandhi","D.Indira Gandhi"),
           ("A.Albert Enstein","B.Nikola Tesla","C.A.P.J Abdul Kalam","D.Charles Babbage"),
           ("A.Jawaharlal Nehru","B.Syed Numan","C.Sardar Vallabhai Patel","D.Rocky Bhai"),
           ("A.New Delhi","B.Beijing","C.Moscow","D.Baghdad"),
           ("A.116","B.117","C.119","D.118"))

answers = ("B","C","A","B","D")
guesses = []
score = 0 
question_num = 0 

for question in questions :
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A,B,C,D) :")
    guesses.append(guess)
    if guess == answers[question_num]:
        print("CORRECT!")
        score += 1 
    else :
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1
print("------------------------------------")
print("             RESULTS")
print("------------------------------------")
print("Answers : ",end="")
for answer in answers :
    print(answer,end=" ")
print()
print("Guesses : ",end="")
for guess in guesses :
    print(guess,end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is {score}%")