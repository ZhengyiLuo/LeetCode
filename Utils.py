
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
