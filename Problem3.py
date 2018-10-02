import sys

def lpf(num):
	for x in range(int((num+1)/2),1,-1):
		if num%x==0:
			return lpf(x)
	return num

print(lpf(int(sys.argv[1])))