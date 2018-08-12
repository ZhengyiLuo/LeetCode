#!/usr/bin/python
# lucky triples
def answer(l):
	# your code here
	T = [0] * len(l)
	K = [0] * len(l)
	for i in range(len(l)):
		v = l[i]
		for j in range(i):
			if v % l[j] == 0:
				T[i] += 1
	
	for i in range(len(l)):
		v = l[i]
		for j in range(i):
			if v % l[j] == 0:
				K[i] += T[j]
	
	res = sum(K)	
	return res
	
	
if __name__ == "__main__":
	print("google")
	print(answer([1, 2,3,4,5,6,7,8]))
	
