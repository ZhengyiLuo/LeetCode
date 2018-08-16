class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        stack = []
        total = 0
        for i in range(len(height)):
            item = None
            while len(stack) > 0 and stack[-1][0] <= height[i]:
                item = stack.pop()
                
                if len(stack) > 0 and item[0] != height[i]:
                    total += (min(stack[-1][0],  height[i]) - item[0]) * (i - stack[-1][1] - 1)
               
                
            stack.append((height[i], i))
        
     
        print(total)
        return total

if __name__ == "__main__":
    s = Solution()
    s.trap([0,1,0,3,1,0,1,3,2,1,2,1])
    # s.trap([0,1,0,2,1,0,1,3,2,1,2,1])
    # s.trap([4,2,3])