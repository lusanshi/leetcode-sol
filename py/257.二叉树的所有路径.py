#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        path = []
        for i in self.binaryTreePaths(root.left)+self.binaryTreePaths(root.right):
            path.append('%d->%s' % (root.val, i))
        if not path:
            path.append(str(root.val))
        return path


# @lc code=end

