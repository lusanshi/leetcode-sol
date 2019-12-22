#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#

# @lc code=start


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        max_squre = 0
        max_i, max_j = len(matrix), len(matrix[0])
        for i, row in enumerate(matrix):
            for j in range(len(row)):
                k = 0
                while matrix[i+k][j+k] == '1':
                    zero = False
                    for n in range(k):
                        if matrix[i+n][j+k] == '0' or matrix[i+k][j+n] == '0':
                            zero = True
                            break
                    if zero:
                        break
                    k += 1
                    if i+k >= max_i or j+k >= max_j:
                        break
                max_squre = max(max_squre, k)
        return max_squre*max_squre

# @lc code=end
