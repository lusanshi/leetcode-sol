/*
 * @lc app=leetcode.cn id=73 lang=java
 *
 * [73] 矩阵置零
 */

// @lc code=start
class Solution {
    public void setZeroes(int[][] matrix) {
        Set<Integer> row = new HashSet<>();
        Set<Integer> col = new HashSet<>();
        int m = matrix.length;
        int n = matrix[0].length;
        for (int r = 0; r < m; r++) {
            for (int i = 0; i < n; i++) {
                if (matrix[r][i] == 0) {
                    col.add(i);
                    row.add(r);
                }
            }
        }
        for (int i : row) {
            for (int k = 0; k < n; k++) {
                matrix[i][k] = 0;
            }
        }
        for (int i : col) {
            for (int k = 0; k < m; k++) {
                matrix[k][i] = 0;
            }
        }
    }
}
// @lc code=end

