/*
 * @lc app=leetcode.cn id=334 lang=java
 *
 * [334] 递增的三元子序列
 */

// @lc code=start
class Solution {
    public boolean increasingTriplet(int[] nums) {
        if (nums.length == 0) {
            return false;
        }
        int min = nums[0];
        int mid = Integer.MIN_VALUE;
        for (int i: nums) {
            if (min < mid) {
                if (i > mid) {
                    return true;
                }
                if (i <= min) {
                    min = i;
                } else if (i < mid) {
                    mid = i;
                }
            } else if (i <= min) {
                min = i;
            } else {
                mid = i;
            }
        }

        return false;
    }
}
// @lc code=end

