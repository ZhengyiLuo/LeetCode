#!/usr/bin/python
import bisect


def getKey(item):
    return item[0]


class Solution(object):
    def lengthOfLIS(self, nums):
        if len(nums) == 0:
            return 0
        tail = [nums[0][1]]
        for i in range(1, len(nums)):
            if nums[i][1] > tail[len(tail) - 1]:
                tail.append(nums[i][1])
            else:
                insert = bisect.bisect_left(tail, nums[i][1])
                tail[insert] = nums[i][1]
        return len(tail)

    def maxEnvelopes(self, envelopes):
        sdoll = sorted(envelopes, key=lambda s: (s[0], -s[1]))
        return self.lengthOfLIS(sdoll)


if __name__ == "__main__":
    slu = Solution()
    a = slu.maxEnvelopes([[2, 5], [0, 9], [0, 0]])
    print(a)
