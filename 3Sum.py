class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        result = set()
        for x in range(0, len(nums)-2):
            h = len(nums)-1
            l = x + 1
            ttarget = 0 - nums[x]
            while l < h:
                if nums[l] + nums[h] > ttarget:
                    h = h - 1
                elif nums[l] + nums[h] < ttarget:
                    l = l + 1
                else:
                    result.add((nums[x], nums[l], nums[h]))
                    h = h - 1
                    l = l + 1


        return list(result)


if __name__ == "__main__":
    print("3Sum Closet")
    s = Solution()
    array = [-1,0,1,2,-1,-4]
    print(s.threeSum(array))
