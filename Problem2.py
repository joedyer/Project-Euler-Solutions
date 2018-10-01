import sys
#script will stop when it gets to 'stop' term

stop = sys.argv[1]

a = 1
b = 1

sum = 0

while b < int(stop):
	temp = a+b
	#print(a,b,temp)
	if temp%2==0:
		sum+=temp
	a=b
	b=temp


print(sum)