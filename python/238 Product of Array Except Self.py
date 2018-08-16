class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        forward = [0] * len(nums)
        backward = [0] * len(nums)
        res = [0] * len(nums)
        pord = 1
        
        for i in range(len(nums)):
            pord *= nums[i]
            forward[i] = pord
        
        pord = 1

        for i in range(len(nums)-1, -1, -1):
            pord *= nums[i]
            backward[i] = pord

        res[0] = backward[1]
        for i in range(1, len(nums) - 1):
            res[i] = forward[i-1]  * backward[i+1]

        res[-1] = forward[-2]

        return res

if __name__ == "__main__":
    s = Solution()

    print(s.productExceptSelf([1,2,3,4]))