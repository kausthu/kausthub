def greet(name):
	if name:
		print("hey",name)
	else:
		print("hey ya")
		return

n=input("who are you?")
greet(n)