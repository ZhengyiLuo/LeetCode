# Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

# For example, given nums = [-2, 0, 1, 3], and target = 2.

# Return 2. Because there are two triplets which sums are less than 2:

# [-2, 0, 1]
class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        result = set()
        smallest = sys.maxint
        result = None
        for x in range(0, len(nums) - 2):
            h = len(nums) - 1
            l = x + 1
            ttarget = target - nums[x]
            while l < h:
                difference = nums[l] + nums[h] - ttarget
                if abs(difference) < smallest:
                    result = nums[x] + nums[l] + nums[h]
                    smallest = abs(difference)
                if difference > 0:
                    h = h - 1
                elif difference <= 0:
                    l = l + 1

        return result


if __name__ == "__main__":
    print("3Sum Closet")
    s = Solution()
    array = [-1,0,1,2,-1,-4]
    print(s.threeSum(array))
