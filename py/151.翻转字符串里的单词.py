#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 翻转字符串里的单词
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        import re
        s = s.strip()
        s = re.sub(r'\s{2,}', ' ', s)
        words = s.split(' ')
        words.reverse()
        return ' '.join(words)
            
        
# @lc code=end

