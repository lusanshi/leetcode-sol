#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from re import subn
        for letter in ransomNote:
            magazine, s = subn(letter, '', magazine, 1)
            if s != 1:
                return False
        else:
            return True
# @lc code=end

