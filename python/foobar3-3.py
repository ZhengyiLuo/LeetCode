#!/usr/bin/python

def answer(n):
	# your code here
	st = n
	n = n + 1
	T = [[0] * n for i in range(n)]
	for i in range(1, n):
			T[i][i] = 1
				
	for i in range(1, n):
		for j in range(1, n):
			s = 0
			for m in range(1, min(j, i - j + 1)):
				s += T[i-j][m]					
			T[i][j]	+= s
	res = 0
	for i in range(1, st):
		res +=  T[st][i]
	return res


	
if __name__ == "__main__":
	print("google")
	print(answer(200))
	

	