class Utils(object):

  def binarySearch(self, blist, num):
    begin = 0
    end = len(blist) - 1
    found = False

    while begin <= end and not found:
      midpoint = (begin + end) // 2
      if blist[midpoint] == num:
        found = True
      else:
        if num < blist[midpoint]:
          end = midpoint - 1
        else:
          begin = midpoint + 1

    if found or num > blist[midpoint]:
      return midpoint
    else:
      return midpoint - 1

  def countSort(self, inputlist, scope):
    count = [0] * (scope + 1)
    for i in range(len(inputlist)):
      count[inputlist[i]] += 1
    start = 0
    for i in range(len(count)):
      while count[i] != 0:
        inputlist[start] = i
        count[i] -= 1
        start += 1

    return inputlist

  def quickSort(self, array):
    if len(array) <= 1:
      return array
    else:
      partition = self.partition(array, len(array) // 2)
      pivot = partition[1]
      input = partition[0]
      if pivot == 0:
        return [input[0]] + self.quickSort(input[1:len(array)])
      elif pivot == len(array) - 1:
        return self.quickSort(input[0:len(array) - 1]) + [input[len(array) - 1]]

      return self.quickSort(input[0:pivot]) + self.quickSort(input[pivot:len(array)])

  def aSwap(self, array, start, end):
    temp = array[start]
    array[start] = array[end]
    array[end] = temp

  def partition(self, array, index):
    if None == array or index > len(array) - 1:
      raise ValueError("Input is invlid")

    start = 0
    end = len(array) - 1
    var = array[index]

    self.aSwap(array, index, end)
    end -= 1
    while start < end:
      if array[start] > var:
        self.aSwap(array, start, end)
        end -= 1
      else:
        start += 1
    result = array[0: start] + [var] + array[start: len(array) - 1]
    return (result, start)


if __name__ == "__main__":
  utils = Utils()
#  print(utils.binarySearch([1,2,3,4,5], 5))
  array = [1, 2, 3, 4, 5, 6, 2, 3, 4, 1, 3]
  print utils.quickSort(array)
