#! usr/bin/python3


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def lnprint(self):
        l = []
        while self is not None:
            l.append(self.val)
            self = self.next
        print(l)
