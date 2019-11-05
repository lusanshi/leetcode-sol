#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()
        for i, row in enumerate(matrix):
            for j, item in enumerate(row):
                if item == 0:
                    rows.add(i)
                    cols.add(j)
        for row in rows:
            matrix[row] = [0] * len(matrix[row])
        for col in cols:
            for i in range(len(matrix)):
                matrix[i][col] = 0


        
# @lc code=end

