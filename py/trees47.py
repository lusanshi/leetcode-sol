#! usr/bin/python3
from treenode import TreeNode


def maxDepth(root: TreeNode) -> int:
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    else:
        return max(maxDepth(root.left), maxDepth(root.right)) + 1


t = TreeNode(1)
t.right = TreeNode(2)
print(maxDepth(t))
