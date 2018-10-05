#create a program to play the game rock,paper,scissors
import random
d={1:'r',2:'p',3:'s'}
c=d[random.randint(1,3)]
while(1):
	p=input("enter 'r','p','s':")
	if(c==d):
		print("tie")
	if((c=='r' and d=='s') or (c=='p' and d=='r') or (c=='s' and d=='p')):
		print("computer wins...!!!")
	else:
		print("the player won...!!!")