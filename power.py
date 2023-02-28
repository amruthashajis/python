def pow(n,p):
	if(p==0):
		return 1
	elif(p==1):
		return n
	else:
		return n*pow(n,(p-1))
n=int(input("enter a no:"))
p=int(input("enter power:"))
a=pow(n,p)
print(n,"^",p,"=",a)
