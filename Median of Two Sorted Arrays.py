#!/usr/bin/python


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        start1 = 0
        end1 = len(nums1)
        start2 = 0
        end2 = len(nums2)
        mid = (len(nums1) + len(nums2)) // 2
        mid1 = (start1 + end1) // 2
        mid2 = (start2 + end2) // 2

        while mid1 + mid2 <= mid:
            if mid1 < mid2:
                start1 = mid + 1
                end2 = mid2 - 1
            elif mid1 < mid2:
                end1 = mid1 - 1
                start2 = mid2 + 1

        if mid1 == start1 or mid1 == end1:
            mid = mid - mid1
            while mid2 <= mid1:
                if mid2 > mid:

#    def binarySearch(self, blist, num):
#        begin = 0
#        end = len(blist) - 1
#        found = False
#
#        while begin <= end and not found:
#            midpoint = (begin + end) // 2
#            if blist[midpoint] == num:
#                found = True
#            else:
#                if num < blist[midpoint]:
#                    end = midpoint - 1
#                else:
#                    begin = midpoint + 1
#
#        if found or num > blist[midpoint]:
#            return midpoint
#        else:
#            return midpoint - 1




if __name__ == "__main__":
    print("Median of Two Sorted Arrays")
    s = Solution()
    listinput = [1, 2, 3, 4]
    print s.binarySearch(listinput, 5)
