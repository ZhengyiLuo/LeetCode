# Given an array S of n integers, find three integers in S such that the
# sum is closest to a given number, target. Return the sum of the three
# integers. You may assume that each input would have exactly one
# solution.

#     For example, given array S = {-1 2 1 -4}, and target = 1.

#     The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
import sys
import Utils
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
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
    array = [0,0,0]
    print(s.threeSumClosest(array, 1))
