
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_value = 0
        i = 0
        j = len(height) - 1
        while i <= j:
            max_value = max(self.area(i, j, height), max_value)
            if height[i] > height[j]:
                j -= 1
            elif height[i] == height[j]:
                i += 1
                j -= 1
            else: 
                i += 1

        return max_value

    def area(self, i, j, height):
        return min(height[i], height[j]) * (j - i)
            
        

if __name__ == "__main__":
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))