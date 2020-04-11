/*
 * @lc app=leetcode.cn id=3 lang=java
 *
 * [3] 无重复字符的最长子串
 */

// @lc code=start
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int maxSubLen = 0;
        char[] cs = s.toCharArray();
        int begin = 0;
        for (int k = 1; k < cs.length; k++) {
            int tmp = contain(cs, begin, k);
            if (k > tmp) {
                if (maxSubLen < k - begin) {
                    maxSubLen = k - begin;
                }
                begin = tmp + 1;
            }
        }
        return Math.max(maxSubLen, cs.length - begin);
    }

    public static int contain(char[] chars, int left, int right) {
        for (int i = left; i < right; i++) {
            if (chars[i] == chars[right]) {
                return i;
            }
        }
        return right;
    }
}
// @lc code=end

