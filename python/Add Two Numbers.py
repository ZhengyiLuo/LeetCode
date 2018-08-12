#!/usr/bin/python

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        

class Solution(object):
    def toLinkedlist(self, n):
        strnum = str(n)
        r = ListNode(int(strnum[len(strnum)-1]))
        res = r
        for i in range(len(strnum)-2, -1, -1):
            r.next = ListNode(int(strnum[i]))
            r = r.next	
        return res
        
    def toString(slef, r):
        num = ''
        while r != None: 
            num =  str(r.val) + num
            r = r.next
        print(num)
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        r = result
        addon = 0
        length1 = 0
        length2 = 0

        l1temp = l1
        l2temp = l2
        while l1temp != None:
            length1 += 1
            l1temp = l1temp.next

        while l2temp != None:
            length2 += 1
            l2temp = l2temp.next
        length = min(length1, length2)

        for i in range(length):
            var = l1.val + l2.val + addon
            l1 = l1.next
            l2 = l2.next
            if var < 10:
                r.val = var
                addon = 0
            else:
                r.val = var - 10
                addon = 1
            r.next = ListNode(0)
            r = r.next

        if length1 > length:
            while l1 != None:
                if l1.val + addon > 9:
                    r.val = l1.val + addon - 10
                    addon = 1
                else:
                    r.val = l1.val + addon
                    addon = 0

                r.next = ListNode(0)
                r = r.next
                l1 = l1.next

        elif length2 > length:
            while l2 != None:
                if l2.val + addon > 9:
                    r.val = l2.val + addon - 10
                    addon = 1
                else:
                    r.val = l2.val + addon
                    addon = 0
                r.next = ListNode(0)
                r = r.next
                l2 = l2.next

        if addon > 0:
            r.val = addon

        r = result
        while r.next.next != None:
            r = r.next

        if r.next.val == 0:
            r.next = None

        return result

if __name__ == "__main__":
    s = Solution()
    l2 = ListNode(1)
    l2.next = ListNode(1)
    l1 = ListNode(5)
#    l1.next = ListNode(2)
    r = s.addTwoNumbers(l1, l2)
    r = s.toLinkedlist(51)
    s.toString(r)
   