/*
 * @lc app=leetcode.cn id=58 lang=java
 *
 * [58] 最后一个单词的长度
 */

// @lc code=start
class Solution {
    public int lengthOfLastWord(String s) {
        // String[] ls = s.split("\\s");
        // if (ls.length == 0){
        // return 0;
        // }
        // return ls[ls.length-1].length();
        int offset = 0;
        char[] cs = s.trim().toCharArray();
        if (cs.length == 0) {
            return offset;
        }
        for (int i = 0; i < cs.length; i++) {
            if (cs[i] == ' ') {
                offset = i;
            }
        }
        if (offset > 0) {
            offset += 1;
        }
        return cs.length - offset;
    }
}
// @lc code=end
