import heapq
import operator
#Shit this is wrong.....
class Solution(object):
	def scheduler(self, a, b):
		t = [0] * len(a)
		s = [0] * len(a)
		o = [0] * len(a)
		if a[0] > b[0]:
			t[0] = a[0]
			s[0] = 'a'
			o[0] = 'a'
		else:
			t[0] = b[0]
			s[0] = 'b'
			o[0] = 'b'	
		
		for i in range(1, len(a)):
			if s[i-1] == 'a': 
				c1 = t[i-1] + a[i]
				c2 = t[i-2] + b[i] if s[i-2] == 'a' else  t[i-2] +b[i-1] + b[i]
				if c1 >= c2:
					t[i] = c1
					s[i] = 'a'
					o[i] = 'a'
				else :
					if s[i-2] == 'a':
						t[i] = c2
						s[i] = 'b'
						o[i] = 'b'
						o[i-1] = 'm'
					else :
						t[i] = c2
						s[i] = 'b'
						o[i] = 'b'
						o[i-1] = 'b'	
						o[i-2] = 'b'	
							
				
			else: 
				c1 = t[i-1] + b[i]
				c2 = t[i-2] + a[i] if s[i-2] == 'b' else  t[i-2] +a[i-1] + a[i]
				if c1 >= c2:
					t[i] = c1
					s[i] = 'b'
					o[i] = 'b'
				else :
					if s[i-2] == 'b':
						t[i] = c2
						s[i] = 'a'
						o[i] = 'a'
						o[i-1] = 'm'
					else :
						t[i] = c2
						s[i] = 'a'
						o[i] = 'a'
						o[i-1] = 'a'	
						o[i-2] = 'a'	

		return t, s, o
		
		
		
if __name__ == "__main__":
	s = Solution
	a = (2,2,2,2, 5,6,3)
	b = (2,2,2,3, 1,6,35)
	print(s.scheduler(s, a, b)[0])
	print(s.scheduler(s, a, b)[1])
	print(s.scheduler(s, a, b)[2])