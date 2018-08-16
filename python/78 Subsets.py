class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        if len(nums) == 0:
            return [[]]
        
        return self.combineset(nums[0], self.subsets(nums[1:])) + self.subsets(nums[1:])
        
    
    def combineset(self, e, nums):
        res = []
        for l in nums:
            res.append([e] + l)
        
        return res

if __name__ == "__main__":
    s = Solution()
    [print(i) for i in s.subsets([1,2,3,4])]