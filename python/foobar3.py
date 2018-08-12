#!/usr/bin/python

def answer(l, t):
	# your code here
	s = 0
	low = 0
	for i in range(len(l)):
		s = s + l[i]
		if s == t:
			return [low, i]
		if s > t:
			while s > t:
				s = s - l[low]
				low += 1
			if s == t:
				return [low, i]
	return [-1, -1]	
			
				
if __name__ == "__main__":
	print("google")
	print(answer( [1,2,3,4], 7))