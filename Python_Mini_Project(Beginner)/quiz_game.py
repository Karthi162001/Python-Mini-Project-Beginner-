print("Welcome to this Quiz Game...")
print("This is gonna really fun for you..")
print("")
print("OK let's get start")
print("Note: If you answer the questions correctly then you will got 10 points for each questions")
print("Good luck...")
print("")

score = 0
question = input("What does RAM stands for? ")
answer = "random access memory"
if question.lower() == "yes":
	print("Correct")
	score+=1
else:
	print("Incorrect")

question1 = input("What does CPU stands for? ")
answer1 = "central processing unit"
if question1.lower() == answer1:
	print("Correct")
	score+=1
else:
	print("Incorrect")

question2 = input("What does IDLE stands for? ")
answer2 ="integrated development environment"
if question.lower() == answer2:
	print("Correct")
	score+=1
else:
	print("Incorrect")

question3 = input("What does SDLC stands for? ")
answer3 ="software development life cycle"
if question3.lower() == answer3:
	print("Correct")
	score+=1
else:
	print("Incorrect")

question4 = input("What does HTML stands for? ")
answer4 ="hypertext markup language"
if question4.lower() == answer4:
	print("Correct")
	score+=1
else:
	print("Incorrect")

question5 = input("What does CSS stands for? ")
answer5 ="cascading life cycle"
if question5.lower() == answer5:
	print("Correct")
	score+=1
else:
	print("Incorrect")


print(f"Your Final Score is :{score}")
print(f"Your total percentage is :{(score/4)*100}")
if score >3:
	print("Good played...")
elif score==5:
	print("Well played...")
else:
	print("Good try...")
print("Thanks for participating this Game...")