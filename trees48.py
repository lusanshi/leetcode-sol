#! usr/bin/python3

from treenode import TreeNode

# def isValidBST(root: TreeNode) -> bool:
# if not root:
#     return True
# lnode, rnode = root.left, root.right
# if not lnode and not rnode:
#     return True
# if not lnode:
#     while rnode:
#         if rnode.val <= root.val:
#             return False
#         rnode = rnode.left
#     return self.isValidBST(root.right)
# if not rnode:
#     while lnode:
#         if lnode.val >= root.val:
#             return False
#         lnode = lnode.right
#     return self.isValidBST(root.left)
# while lnode:
#     if lnode.val >= root.val:
#         return False
#     lnode = lnode.right
# while rnode:
#     if rnode.val <= root.val:
#         return False
#     rnode = rnode.left
# return self.isValidBST(root.left) and self.isValidBST(root.right)

import sys
test = TreeNode(4)
test.left = TreeNode(2)
test.right = TreeNode(6)
test.left.left = TreeNode(1)
test.left.right = TreeNode(3)
test.right.left = TreeNode(5)
test.right.right = TreeNode(7)


def inordtrv(arr: list, root: TreeNode):
    #    root = self
    if not root:
        return
    inordtrv(arr, root.left)
    arr.append(root.val)
    inordtrv(arr, root.right)


gen = []
inordtrv(gen, test)
print(gen)
# while True:
#     try:
#         print(next(gen))
#     except StopIteration:
#         sys.exit()
