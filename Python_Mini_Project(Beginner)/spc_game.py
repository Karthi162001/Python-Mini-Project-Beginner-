import random
print("******Stone,Paper,Scissor Game******")

options = ["Stone","Paper","Scissor"]
your_score = 0
computer_score = 0
while True:
	user_pick = input("Enter your pick (Stone,Paper,Scissor): ").lower()
	random_num = random.randint(0,2)
	computer_pick = options[random_num]

	if user_pick =="stone" and computer_pick.lower()=="scissor":
		your_score+=1
		print("You won!")
		print("If you want to quite press Q")
		continue
	elif user_pick =="scissor" and computer_pick.lower()=="paper":
		your_score+=1
		print("You won!")
	elif user_pick =="paper" and computer_pick.lower()=="stone":
		print("You won!")

	elif user_pick=="q":
		break

	else:
		computer_score+=1
		print("Computer won!..")
		print("If you want to quite press Q")
		continue
print("Thanks for playing the game...")
print(f"Your score is :{your_score} ")
print(f"Computer score is :{computer_score} ")	