#program to check the value of numbers
#input a from keyboard
a=int(input("enter the value of a: "))
#input b from keyboard
b=int(input("enter the value of b:"))
#print value of a
print("a:",a)
#print value of b
print("b:",b)
if(a>b):
	print(a,"is greater")
elif(b>a):
	print(b,"is greater")
else:
	print("both are equal")