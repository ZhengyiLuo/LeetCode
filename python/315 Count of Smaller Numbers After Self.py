import bisect
class Solution:
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = []
        res = [0] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            point = bisect.bisect_left(l, nums[i])
            bisect.insort_left(l, nums[i])
            res[i] = point
        return res
        

if __name__ == "__main__":
    s = Solution()
    print(s.countSmaller([5,2,6,1]))