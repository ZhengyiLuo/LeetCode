import heapq
import operator
class Solution(object):
	def topKFrequent(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: List[int]
		"""
		d = {}
		hp = []
		result = []
		for i in nums:
			if i in d: 
				d[i] += 1
			else: d[i] = 1
		for e in d.items():
			heapq.heappush(hp, e)
		for i in heapq.nlargest(k, d.items(),key=operator.itemgetter(1)):
			result.append(i[0])
		return result
		
if __name__ == "__main__":
	s = Solution
	l = (1,2,3,4,5,5,5,5,5,5)
	print(s.topKFrequent(s, l, 2))