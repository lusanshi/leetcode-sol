#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from functools import reduce
        id = lambda s: reduce(lambda x, y: x * y, map(lambda i: i + 255, map(ord, s)))
        hdic = {}
        for i in strs:
            if not i:
                fp = 0
            else:
                fp = id(i)
            if fp in hdic:
                hdic[fp].append(i)

            else:
                hdic[fp] = [i]

        ret = []
        for i in hdic:
            ret.append(hdic[i])
        return ret
        
# @lc code=end

