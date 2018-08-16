
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_len = len(s)
        p_len = len(p)
        T = [ [False] * (p_len + 1) for i in range((s_len + 1))]
        T[-1][-1] = True
        
        for j in range(p_len):
            for i in range(-1, s_len):
                
                first = p[j] == '.' and T[i-1][j-1] if s_len > 0 and i >= 0 else False
                second = p[j] == s[i] and T[i-1][j-1] if s_len > 0 and i >= 0  else False
                
                third = p[j+1] == '*' and (T[i][j-1] or (( (p[j] == s[i] if s_len > 0 and i >= 0  else False) or p[j] == '.') and (T[i-1][j] if s_len > 0 else False) ) ) if j + 1 < p_len else False
                forth = p[j] == '*' and T[i][j-1]
                T[i][j] = first or second or third or forth

                # print(j, p[j], i, s[i], T[i][j])
                # print(first ,  second , third , forth)

        # for i in range(len(T)):
        #     print(i, T[i])

        return T[s_len -1 ][p_len - 1]


if __name__ == "__main__":
    s = Solution()
    print(s.isMatch("mississippi", "mis*is*p*.") == False)
    print(s.isMatch("aa", "a") == False)
    print(s.isMatch("aa", "a*") == True)
    print(s.isMatch("ab", ".*") == True)
    print(s.isMatch("aab", "c*a*b")== True)
    print(s.isMatch("faaba", "fa*aba")== True)
    print(s.isMatch("aaa", ".a")== False)
    print(s.isMatch("aaa", ".*")== True)
    print(s.isMatch("a", "ab*")== True)
    print(s.isMatch("", ".b*")== False)
    print(s.isMatch("a", ".*..a*")== False)
