#You need to pass a message to the bunny prisoners, but to avoid detection, the code you agreed to use is... obscure, to say the least. The bunnies are given food on standard-issue prison plates that are stamped with the numbers 0-9 for easier sorting, and you need to combine sets of plates to create the numbers in the code. The signal that a number is part of the code is that it is divisible by 3. You can do smaller numbers like 15 and 45 easily, but bigger numbers like 144 and 414 are a little trickier. Write a program to help yourself quickly create large numbers for use in the code, given a limited number of plates to work with.
#
#You have L, a list containing some digits (0 to 9). Write a function answer(L) which finds the largest number that can be made from some or all of these digits and is divisible by 3. If it is not possible to make such a number, return 0 as the answer. L will contain anywhere from 1 to 9 digits.  The same digit may appear multiple times in the list, but each element in the list may only be used once.
#
#Languages
#=========
#
#To provide a Python solution, edit solution.py
#To provide a Java solution, edit solution.java
#
#Test cases
#==========
#
#Inputs:
#	(int list) l = [3, 1, 4, 1]
#Output:
#	(int) 4311
#
#Inputs:
#	(int list) l = [3, 1, 4, 1, 5, 9]
#Output:
#	(int) 94311
#
#Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.
# did not pass.... wtf.....

import bisect

def answer(l):
	Reminder = [[],[],[]]
	for i in l:
		if i % 3 == 0:
			Reminder[0].append(i)
		elif i % 3 == 1:
			Reminder[1].append(i)	
		elif i % 3 == 2:
			Reminder[2].append(i)
	print(Reminder)
	if	len(Reminder[2]) > len(Reminder[1]):
		diff = 	(len(Reminder[2]) - len(Reminder[1])) % 3
		if diff == 1:
			Reminder[2] = sorted(Reminder[2])
			Reminder[2] = Reminder[2][diff : len(Reminder[2])]
		elif diff == 2:
			if len(Reminder[2]) % 3 == 0:
				Reminder[1] = sorted(Reminder[1])
				Reminder[1] = Reminder[1][diff : len(Reminder[1])] 
			else:
				Reminder[2] = sorted(Reminder[2])
				Reminder[2] = Reminder[2][diff : len(Reminder[2])]
							
				
	elif len(Reminder[1]) > len(Reminder[2]):
		diff = 	(len(Reminder[1]) - len(Reminder[2])) % 3
		if diff == 1:
			Reminder[1] = sorted(Reminder[1])
			Reminder[1] = Reminder[1][diff : len(Reminder[1])] 
		elif diff == 2:
			if len(Reminder[1]) % 3 == 0:
				Reminder[2] = sorted(Reminder[2])
				Reminder[2] = Reminder[2][diff : len(Reminder[2])] 
			else:
				Reminder[1] = sorted(Reminder[1])
				Reminder[1] = Reminder[1][diff : len(Reminder[1])]
			
	num = list(reversed(sorted(Reminder[0] + Reminder[1] + Reminder[2])))
						
	s = ''.join(map(str, num))		
	if	s != '':
		return int(s)	
	else:
		return 0	

	
	
if __name__ == "__main__":
	print("google")
	print(answer( [3, 1, 4, 1, 5, 9]))
	

	
	




