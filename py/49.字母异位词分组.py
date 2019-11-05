#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        asc_sum = lambda x: sum(map(ord, x))
        ret = []
        for i in strs:
            for group in ret:
                if set(group[0]) == set(i) and asc_sum(group[0]) == asc_sum(i):
                        group.append(i)
                        break
            else:
                ret.append([i])

        return ret
        
# @lc code=end

