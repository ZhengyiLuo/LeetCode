class Solution:
    digits = {
            "I": 1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }

    
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        four = "IV"
        forty = "XL"
        fourh = "CD"

        nine = "IX"
        nity = "XC"
        nineh = "CM"

        num = 0
        while four in s:
            num += 4
            s = s.replace(four, "", 1)

        while forty in s:
            num += 40
            s = s.replace(forty, "", 1)

        while fourh in s:
            num += 400
            s = s.replace(fourh, "", 1)

        while nine in s:
            num += 9
            s = s.replace(nine, "", 1)

        while nity in s:
            num += 90
            s = s.replace(nity, "", 1)

        while nineh in s:
            num += 900
            s = s.replace(nineh, "", 1)
        
        for k, v in self.digits.items():
            
            while k in s:
                num += v
                s = s.replace(k, "", 1)
        return num


if __name__ == "__main__":
    s = Solution()
    print(s.romanToInt("MDCCCLXXXIV"))