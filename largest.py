a=int(input("enter first no:"))
b=int(input("enter second no:"))
c=int(input("enter third no:"))
print("\n a=",a,"b=",b,"c=",c)
if(a>b and a>c):
	print("largest is:",a)
elif(b>a and b>c):
	print("largest is:",b)
else:
	print("largest is:",c)
