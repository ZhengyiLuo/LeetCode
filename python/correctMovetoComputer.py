class Solution(object):
	def scheduler(self, f, s):
		a = [0] * len(f)
		b = [0] * len(s)
		a[1], a[2], b[1],b[2] =  f[1], f[1] + f[2], s[1], s[1] + s[2]
		for i in range(3, len(s)):
			if a[i-2] + f[i-1] + f[i] > b[i-2] + s[i]:
				a[i] = a[i-2] + f[i-1] + f[i] 
			else : 	
				a[i] = b[i-2] + s[i] 
			if b[i-2] + s[i-1] + s[i] > a[i-2] + f[i]:
				b[i] = b[i-2] + s[i-1] + s[i] 
			else : 	
				b[i] = a[i-2] + f[i] 
		return a, b
	

if __name__ == "__main__":
	s = Solution
	a = (0,6, 5,7,3)
	b = (0,3, 1,6,35)
	r = s.scheduler(s, a, b)
	print(r[0])
	print(r[1])

