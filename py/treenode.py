#! usr/bin/python3
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def inordtrv(self):
        root = self
        if not root:
            return
        inordtrv(root.left)
        print(root.val)
        inordtrv(root.right)
