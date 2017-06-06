#!/usr/bin/python


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        w = {}
        base = 0
        Max = 0
        curr = 0
        for i in range(len(s)):
            if s[i] in w and w[s[i]] >= base:
                base = w[s[i]] + 1
                curr = i - w[s[i]]
                w[s[i]] = i
            else:
                w[s[i]] = i
                curr += 1
                if curr > Max:
                    Max = curr
        return Max

if __name__ == "__main__":
    print("Longest Substring Without Repeating Characters")
    s = Solution()
    print(s.lengthOfLongestSubstring("a"))
