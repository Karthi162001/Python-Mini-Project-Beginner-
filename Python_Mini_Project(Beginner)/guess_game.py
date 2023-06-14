import random
print("******Guess the Correct Number Game******")

chances = 0
while True:
	chances+=1
	user_input = int(input("Enter the Number: "))
	random_num = random.randint(0,10)

	if user_input ==random_num:
		print("Correct")
		break
	else:
		print("Wrong")
		continue
if chances==1:
	print(f"You got the answer at {chances}st try...")
elif chances==2:
	print(f"You got the answer at {chances}nd try...")
elif chances==3:
	print(f"You got the answer at {chances}rd try...")
else:
	print(f"You got the answer at {chances}th try...")


