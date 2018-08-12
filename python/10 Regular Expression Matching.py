#class Solution:
#	def isMatch(self, s, p):
#		"""
#		:type s: str
#		:type p: str
#		:rtype: bool
#		"""
#		s_len = len(s)
#		p_len = len(p)
#		t = [ [False] * (s_len + 1) for i in range((p_len + 1))]
#		t[p_len][s_len] = True
#
#		for j in range(p_len - 1, -1, -1):
#			for i in range(s_len - 1, -1, -1):
#				prev = t[j + 1][i + 1]
#				prev_j = t[j][i + 1]
#				prev_i = t[j + 1][i]
#				first = s[i] == p[j] and prev
#				second = p[j] == '.' and prev
#				
#				thrid = False
#				if j - 1 >= 0:				
#					thrid = (p[j] == '*' and (s[i] == p[j - 1] or p[j-1] == '.'))  and (prev or prev_j)
#					
#				forth = False
#				if j - 1 >= 0:				
#					forth = (p[j - 1] == '.') and prev
#				
#				fifth = False
#				if	j + 1 < p_len:
#					fifth = (p[j + 1] == '*' and prev_i) or (p[j] == '*' and prev_i)
#					
#				sixth = False
#				if j + 2 < p_len:
#					sixth = p[j + 2] == '*' and s[i] == p[j] and t[j + 3][i + 1]
#				
#				t[j][i] = first or second or thrid or forth or fifth or sixth
#				
#				
#				
##				print(j, p[j], i, s[i], t[j][i])
##				print(first ,  second , thrid , forth, fifth, sixth)	
###
##		for i in reversed(range(len(t))):
##			print(i, list(reversed(t[i])))
#			
#		return t[0][0]
class Solution(object):
	def isMatch(self, s, p):
		"""
		:type s: str
		:type p: str
		:rtype: bool
		"""

	return True 



if __name__ == "__main__":
	s = Solution()
	print(s.isMatch("mississippi", "mis*is*p*."))
	print(s.isMatch("aa", "a"))	
	print(s.isMatch("aa", "a*"))	
	print(s.isMatch("ab", ".*"))	
	print(s.isMatch("aab", "c*a*b"))	
	print(s.isMatch("faaba", "fa*aba"))	
	print(s.isMatch("aaa", ".a"))
	print(s.isMatch("aaa", ".*"))	
	print(s.isMatch("a", "ab*"))	