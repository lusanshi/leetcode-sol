#
# @lc app=leetcode.cn id=165 lang=python3
#
# [165] 比较版本号
#

# @lc code=start
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1, version2 = version1.split('.'), version2.split('.')
        len1, len2 = len(version1), len(version2)
        if len1 > len2:
            version2.extend(['0' for _ in range(len1-len2)])
        elif len1 < len2:
            version1.extend(['0' for _ in range(len2-len1)])
        for i, j in zip(version1, version2):
            if int(i) > int(j):
                return 1
            if int(i) < int(j):
                return -1
        else:
            return 0
# @lc code=end

