import sys

def largestProduct(digit):
	arr = []
	for x in range(digit):
		arr.append((9*(10**x)))
	return sum(arr)*sum(arr)

def isPalindrome(number):
	number=str(number)
	for x in range(len(number)):
		if number[x] != number[len(number)-x-1]:
			return False
	return True

def func(x,y):
	if x<111 or y<111:
		return 0
	elif isPalindrome(x*y):
		return x*y
	else:
		return func(x-1,y) or func(x,y-1)

print(func(999,999))