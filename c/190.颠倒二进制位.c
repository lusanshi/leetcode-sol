/*
 * @lc app=leetcode.cn id=190 lang=c
 *
 * [190] 颠倒二进制位
 */

// @lc code=start
uint32_t reverseBits(uint32_t n) {
    int i = 0;
    uint32_t s = 0;
    while(i < 32){
        if (i > 0) s <<= 1;
        s += n & 1;
        n >>= 1;
        i++;
    }
    return s;
}
// @lc code=end
