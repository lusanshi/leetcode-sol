#! usr/bin/python3
from treenode import TreeNode


def isSymmetric(root: TreeNode) -> bool:
    return cmp(root, root)


def cmp(l: TreeNode, r: TreeNode) -> bool:
    if l and r and l.val == r.val:
        return cmp(l.left, r.right) and cmp(l.right, r.left)
    elif not l and not r:
        return True
    else:
        return False
