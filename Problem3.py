import sys

def lpf(num,start):
	for x in range(start,num,1):
		if num%x==0:
			print(x)
			return lpf(int(num/x),x)
	return num

print(lpf(int(sys.argv[1]),2))