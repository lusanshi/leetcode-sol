/*
 * @lc app=leetcode.cn id=67 lang=java
 *
 * [67] 二进制求和
 */

// @lc code=start
class Solution {
    public String addBinary(String a, String b) {
        if (a.length() < b.length()) {
            String swap = a;
            a = b;
            b = swap;
        }
        char[] ca = new StringBuffer(a).reverse().toString().toCharArray();
        char[] cb = new StringBuffer(b).reverse().toString().toCharArray();
        char[] results = new char[ca.length + 1];
        int offset = 0;
        for (int i = 0; i < cb.length; i++) {
            if (offset == 1) {
                if (ca[i] == cb[i]) {
                    results[i] = '1';
                    if (ca[i] == '0') {
                        offset = 0;
                    }
                } else {
                    results[i] = '0';
                }
            } else if (ca[i] == cb[i]) {
                results[i] = '0';
                if (ca[i] == '1') {
                    offset = 1;
                }
            } else {
                results[i] = '1';
            }
        }
        for (int i = cb.length; i < ca.length; i++) {
            if (offset == 1) {
                if (ca[i] == '0') {
                    results[i] = '1';
                    offset = 0;
                } else {
                    results[i] = '0';
                }
            } else {
                results[i] = ca[i];
            }
        }
        results[ca.length] = offset == 1 ? '1' : ' ';
        return new StringBuffer(new String(results)).reverse().toString().trim();
    }
}
// @lc code=end
