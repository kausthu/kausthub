a=['1','2','3','4','5','6','7','8','9']
def printboard():
	print(a[0]+'|'+a[1]+'|'+a[2])
	print("-----")
	print(a[3]+'|'+a[4]+'|'+a[5])
	print("-----")
	print(a[6]+'|'+a[7]+'|'+a[8])
	printboard()

playeroneturn=True
while True:
	printboard()
	p=input("Choose an spot:")

	if(p in a):
		
#Player 1 plays			
			if playeroneturn:
				print("Player 1,Choose your place:")
				a[int(p)-1]='X'
				playeroneturn= not playeroneturn
#Player 2 plays
			else:
				print("Player 2,Choose your place:")
				a[int(p)-1]='O'
				playeroneturn= not playeroneturn
				if(X==a[0]==a[1]==a[2]):
					print("Player 1 wins..!!")
					exit()
				elif(O==a[0]==a[1]==a[2]):
					print("Player 2 wins..!!")
					exit()
				elif(X==a[3]==a[4]==a[5]):
					print("Player 1 wins..!!")
					exit()
				elif(O==a[3]==a[4]==a[5]):
					print("Player 2 wins..!!")
					exit()
				elif(X==a[6]==a[7]==a[8]):
					print("Player 1 wins..!!")
					exit()
				elif(O==a[6]==a[7]==a[8]):
					print("Player 2 wins..!!")
					exit()
				elif(X==a[0]==a[3]==a[6]):
					print("Player 1 wins..!!")
					exit()
				elif(O==a[0]==a[3]==a[6]):
					print("Player 2 wins..!!")
					exit()
				elif(X==a[1]==a[4]==a[7]):
					print("Player 1 wins..!!")
					exit()
				elif(O==a[1]==a[4]==a[7]):
					print("Player 2 wins..!!")
					exit()
				elif(X==a[2]==a[5]==a[8]):
					print("Player 1 wins..!!")
					exit()
				elif(O==a[2]==a[5]==a[8]):
					print("Player 2 wins..!!")
					exit()
				elif(X==a[0]==a[4]==a[8]):
					print("Player 1 wins..!!")
					exit()
				elif(O==a[0]==a[4]==a[8]):
					print("Player 2 wins..!!")
					exit()
				elif(X==a[2]==a[4]==a[6]):
					print("Player 1 wins..!!")
					exit()
				elif(O==a[2]==a[4]==a[6]):
					print("Player 2 wins..!!")
					exit()
else:
	print("It's a tie..!!")	
