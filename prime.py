num=int(input("enter a number:"))
if(num==1):
	print("not prime")
if(num>1):
	for i in range(2,num):
		if(num%i==0):
			print("it is not a prime no")
			break
		else:
			print("it is a prime no")
			break
