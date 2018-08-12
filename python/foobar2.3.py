#!/usr/bin/python

#Bunny Prisoner Locating
#=======================
#
#Keeping track of Commander Lambda's many bunny prisoners is starting to get tricky. You've been tasked with writing a program to match bunny prisoner IDs to cell locations.
#
#The LAMBCHOP doomsday device takes up much of the interior of Commander Lambda's space station, and as a result the prison blocks have an unusual layout. They are stacked in a triangular shape, and the bunny prisoners are given numerical IDs starting from the corner, as follows:
#
#| 7
#| 4 8
#| 2 5 9
#| 1 3 6 10
#
#Each cell can be represented as points (x, y), with x being the distance from the vertical wall, and y being the height from the ground. 
#
#For example, the bunny prisoner at (1, 1) has ID 1, the bunny prisoner at (3, 2) has ID 9, and the bunny prisoner at (2,3) has ID 8. This pattern of numbering continues indefinitely (Commander Lambda has been taking a LOT of prisoners). 
#
#Write a function answer(x, y) which returns the prisoner ID of the bunny at location (x, y). Each value of x and y will be at least 1 and no greater than 100,000. Since the prisoner ID can be very large, return your answer as a string representation of the number.
#
#Languages
#=========
#
#To provide a Python solution, edit solution.py
#To provide a Java solution, edit solution.java
#
#Test cases
#==========c
#
#Inputs:
#	(int) x = 3
#	(int) y = 2
#Output:
#	(string) "9"
#
#Inputs:
#	(int) x = 5
#	(int) y = 10
#Output:
#	(string) "96"


def toLinkedlist(n):
	strnum = str(n)
	r = ListNode(int(strnum[len(strnum)-1]))
	res = r
	for i in range(len(strnum)-2, -1, -1):
		r.next = ListNode(int(strnum[i]))
		r = r.next	
	return res

def toString(r):
	num = ''
	while r != None: 
		num =  str(r.val) + num
		r = r.next
	return num

class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None
	
	
	def add(self, l1, l2):
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

#def answer(x, y):
#	# your code here
#	ans = ListNode(1)
#	for i in range(1,y):
#		ans = ans.add(ans, toLinkedlist(i))
#	for i in range(y+1,y+x):
#		ans = ans.add(ans, toLinkedlist(i))
#	return toString(ans)


def answer(x, y):
	# your code here
	ans = 1
	for i in range(1,y):
		ans = ans + i
	for i in range(y+1,y+x):
		ans = ans + i
	return str(ans)
	
	
if __name__ == "__main__":
	print("foobar..... fuck ")
	print(answer(100000, 1000000))
	