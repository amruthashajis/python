num=int(input("enter a no:"))
sum=0
k=num
while(k>0):
	r=k%10
	sum=sum+(r*r*r)
	k=int(k/10)
if(sum==num):
	print("amstrong")
else:
	print("not amstrong")
