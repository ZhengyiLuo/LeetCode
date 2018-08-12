#!/usr/bin/python

from fractions import gcd
from fractions import Fraction

def transposeMatrix(m):
	t = []
	for r in range(len(m)):
		tRow = []
		for c in range(len(m[r])):
			if c == r:
				tRow.append(m[r][c])
			else:
				tRow.append(m[c][r])
		t.append(tRow)
	return t

def getMatrixMinor(m,i,j):
	return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
	#base case for 2x2 matrix
	if len(m) == 2:
		return m[0][0]*m[1][1]-m[0][1]*m[1][0]

	determinant = 0
	for c in range(len(m)):
		determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
	return determinant

def getMatrixInverse(m):
	determinant = getMatrixDeternminant(m)
	#special case for 2x2 matrix:
	if len(m) == 2:
		return [[m[1][1]/determinant, -1*m[0][1]/determinant],
				[-1*m[1][0]/determinant, m[0][0]/determinant]]

	#find matrix of cofactors
	cofactors = []
	for r in range(len(m)):
		cofactorRow = []
		for c in range(len(m)):
			minor = getMatrixMinor(m,r,c)
			cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
		cofactors.append(cofactorRow)
	cofactors = transposeMatrix(cofactors)
	for r in range(len(cofactors)):
		for c in range(len(cofactors)):
			cofactors[r][c] = cofactors[r][c]/determinant
	return cofactors
	
def matmult(m1,m2):
	r=[]
	m=[]
	for i in range(len(m1)):
		for j in range(len(m2[0])):
			sums=0
			for k in range(len(m2)):
				sums=sums+(m1[i][k]*m2[k][j])
			r.append(sums)
		m.append(r)
		r=[]
	return m

def inv(A):
	""" Return the matrix inverse
	Uses Gauss-Jordan Elimination, seems the simplest
	to implement and gives exact values
	"""
	n = len(A)  # The input matrix is squared

	table = [[0]*2*n for _ in xrange(n)]  # Create an empty table

	# Copy initial values
	for i in range(n):
		for j in range(n):
			table[i][j] = A[i][j]
		table[i][i+n] = 1  # Diagonal matrix

	# State: table = [A|I]
	#print(np.array(table))

	# Pivoting
	for i in range(n):  # For each row
		# First we normalize the current row (first idx = 1)
		scalar = table[i][i]  # We have guaranty that this value won't be 0 (otherwise
							  # proba=1.0 so it would  have been a stable state)
		for j in range(2*n):
			table[i][j] /= scalar

		# Then, we substract the row to all the next and previous ones
		for j in range(n):
			if j != i:
				scalar = table[j][i]
				for k in range(2*n):
					table[j][k] -= scalar * table[i][k]

	# State: table = [I|A^-1]
	#print(np.array(table))

	B = [table[i][n:] for i in range(n)]  # Paste the result
	return B

def lcm(a, b):
	"""Return lowest common multiple."""
	return a * b // gcd(a, b)

def lcmm(args):
	"""Return lcm of args."""  
	if len(args) < 1:
		return 1 
	res = args[0]
	for i in range(len(args)):
		res = lcm(res, args[i])
	return res

def answer(m):
	# your code here	
	if sum(m[0]) == 0:
		return [1, 1]
	order = []
	for i in range(len(m)):
		if  all(v == 0 for v in m[i]):
			order.append(i)
	
	num_t = len(order)
	num_s = len(m) - num_t

		
	for i in range(len(m)):
		if	i not in order:
			order.append(i)		
			
	m = [m[i] for i in order]
	for i in range(len(m)):
		m[i] = [m[i][j] for j in order]
		
	for i in range(num_t):
		m[i][i] = 1	

	m_rowsum = [sum(m[i]) for i in range(len(m))]
	
	for i in range(len(m)):
		m[i] = [Fraction( m[i][j],m_rowsum[i]) for j in range(len(m_rowsum))]
		
	R = [m[i][0:num_t] for i in range(num_t,len(m))] 
	Q = [m[i][num_t:len(m)] for i in range(num_t,len(m))]  
	
	for i in range(len(Q)):
		for j in range(len(Q)):
			if	i == j:
				Q[i][j] = 1 - Q[i][j]
			else: 	
				Q[i][j] = 0 - Q[i][j]
		
			
	F = getMatrixInverse(Q)  # F = -(I-Q)^-1 (WARNING: Opposite sign)
	
	res = matmult(F, R)	
	if	len(res) > 1:
		res = res[0]
	d = [0] * len(res)
	for i in range(len(res)):
		d[i] = res[i].denominator
		
	c = lcmm(d)

	res =  [ x*c for x in res ]
	result = [ x.numerator for x in res ]
	result.append(c)
	return result	
	
	
if __name__ == "__main__":
	print("google")
	print(answer( [[0,1,0,0,0,1],  [4,0,0,3,2,0],  		[0,0,0,0,0,0],  		[0,0,0,0,0,0],  		[0,0,0,0,0,0],  		[0,0,0,0,0,0]]  ))
#	print(answer( [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]))

#	a =  [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [1, 0, 0, 0, 0]]
#	a[2][2] = Fraction(1,2) 
#	a = np.array(a)
#	print(a.sum(axis=1)[:,None])
	
	
	
	
	
	
	
	
	
	

	
	

	