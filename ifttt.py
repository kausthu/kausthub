a=['1','2','3','4','5','6','7','8','9']
def printboard():
	print(a[0]+'|'+a[1]+'|'+a[2])
	print("-----")
	print(a[3]+'|'+a[4]+'|'+a[5])
	print("-----")
	print(a[6]+'|'+a[7]+'|'+a[8])
printboard()


playeroneturn=True

for i in range(9):
	printboard()
#Player 1 plays
	if playeroneturn:
		p=input("Player 1,Choose your place:")
		if p in a:
			a[int(p)-1]='X'
			playeroneturn= not playeroneturn
#Player 2 plays
	else:
		p= input("Player 2,Choose your place:")
		if p in a:
			a[int(p)-1]='O'
			playeroneturn= not playeroneturn
if('X'==a[0]==a[1]==a[2]):
	print("Player 1 wins")
elif('O'==a[0]==a[1]==a[2]):
	print("Player 2 wins")
elif('X'==a[0]==a[3]==a[6]):
	print("Player 1 wins")
elif('O'==a[0]==a[3]==a[6]):
	print("Player 2 wins")
#check for winning combinations

#check for a tie condition