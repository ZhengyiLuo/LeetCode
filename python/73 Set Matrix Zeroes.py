class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        is_row_0 = False
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i != 0:
                        matrix[i][0] = 0
                    else:
                        is_row_0 = True
                    matrix[0][j] = 0
        
        for i in range(len(matrix)):
            if matrix[i][0] == 0 and i != 0:
                for j in range(len(matrix[0])):
                    matrix[i][j] = 0
        
        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(len(matrix)):
                    matrix[i][j] = 0

        if is_row_0:
            for j in range(len(matrix[0])):
                    matrix[0][j] = 0     

if __name__ == "__main__":
    s = Solution()
    l = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    s.setZeroes(l)
    print(l)
            

