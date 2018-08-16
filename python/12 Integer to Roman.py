import math
class Solution:
    digits = {
            1: "I",
            5: "V",
            10:"X",
            50:"L",
            100:"C",
            500:"D",
            1000:"M",
        }
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        num_str = str(num)[::-1]
        res = ''

        if len(num_str) >= 4:
           res += self.digits[1000]* math.floor(num / 1000)
           num = num % 1000

        if len(num_str) >= 3:
            if num_str[2] == '9':
                res += self.digits[100] + self.digits[1000]
            elif num_str[2] == '4':
                res += self.digits[100] + self.digits[500]
            else:
                res += self.digits[500]* int(num / 500) + self.digits[100]* math.floor((num % 500) / 100)
            num = num % 100
            
        if len(num_str) >= 2:
            if num_str[1] == '9':
                res += self.digits[10] + self.digits[100]
            elif num_str[1] == '4':
                res += self.digits[10] + self.digits[50]
            else:
                res += self.digits[50]* int(num / 50)+ self.digits[10]* math.floor((num % 50) / 10)
            num = num % 10
        
        if len(num_str) >= 1:
            if num_str[0] == '9':
                res += self.digits[1] + self.digits[10]
            elif num_str[0] == '4':
                res += self.digits[1] + self.digits[5]
            else:
                res += self.digits[5]* int(num / 5) + (self.digits[1]* math.floor((num % 5) / 1)) 
        return res

        
        

if __name__ == "__main__":
    s = Solution()
    print(s.intToRoman(1000))