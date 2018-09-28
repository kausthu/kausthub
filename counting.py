count=0
import random
(random.randint(1,6))
while(count<=100):
	n=input("enter 'r' to roll the dice:")
	if(n=='r'):
		a=random.randint(1,6)
		count=count+a
		print("my position:",count)
		print("your random value was:",a)
	if(count==8):
		count=37
		print("congrats,u got a ladder")
	elif(count==11):
		count=2
		print("sorry,the snake bit u")
	elif(count==13):
		count=34
		print("congrats,u got a ladder")
	elif(count==25):
		count=4
		print("sorry,the snake bit u")
	elif(count==38):
		count=9
		print("sorry,the snake bit u")
	elif(count==40):
		count=68
		print("congrats,u got a ladder")
	elif(count==52):
		count=81
		print("congrats,u got a ladder")
	elif(count==65):
		count=46
		print("sorry,the snake bit u")
	elif(count==76):
		count=97
		print("congrats,u got a ladder")
	elif(count==89):
		count=70
		print("sorry,the snake bit u")
	elif(count==93):
		count=64
		print("sorry,the snake bit u")
	elif(count>100):
		count=count-a
		print("u can't go more than 100")
	elif(count==100):
		print("u won the game...!!!")