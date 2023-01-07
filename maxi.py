# My First Quiz Game in Python

questions = ("How many Elements are there in the priodictable?: ", 
             "Which coding language did I use to write this game?: ", 
             "What the name of the hottes planet?:",
             "How many bones are in a human body?:", 
             "What is the chemical formular of water?:")

options = (("A. 116", "B. 117", "C. 118", "E. 119"), 
           ("A. C++", "B. Java", "C. Python", "E. HTML5"), 
           ("A. Mars", "B. Sarturn", "C. Mecury", "E. Venus"), 
           ("A. 207", "B. 206", "C. 208", "E. 209"),
           ("A. hO", "B. h1O", "C. h2O", "E. h3O"))

answers = ("C", "C", "E", "B", "C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-----------------")
    print(question)
    for option in options[question_num]:
        print(option)
    
    guess = input("Answer: "). upper()
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print ("Incorrect!")
        print(f"{answers[question_num]} is correct answer")
    question_num +=1

print("---------------------------")
print("     RESULTS               ")
print("---------------------------")

score = int(score / len(questions) * 100)

print(f"your score is: {score}%")
