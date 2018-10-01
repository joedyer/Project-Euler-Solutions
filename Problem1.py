import sys

sum = 0

for x in range(int(sys.argv[1])):
	if x%3==0:
		sum+=x
	elif x%5==0:
		sum+=x

print(sum)
