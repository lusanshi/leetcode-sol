/*
 * @lc app=leetcode.cn id=27 lang=java
 *
 * [27] 移除元素
 */

// @lc code=start
class Solution {
    public int removeElement(int[] nums, int val) {
        int offset = 0;
        for (int i = 0; i < nums.length; i++){
            if (nums[i] == val){
                offset++;
            } else if (offset > 0){
                nums[i-offset] = nums[i];
            }
        }
        return nums.length - offset;
    }
}
// @lc code=end

