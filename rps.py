#create a program to play the game rock,paper,scissors
import random
d={1:'R',2:'P',3:'S'}
c=d[random.randint(1,3)]
p=input("enter 'R','P','S':")
if(c==d):
	print("tie")
if((c=='R' and p=='S') or (c=='P' and p=='R') or (c=='S' and p=='P')):
	print("computer wins...!!!")
else:
	print("the player won...!!!")
