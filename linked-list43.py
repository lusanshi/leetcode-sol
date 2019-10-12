#! usr/bin/python3
from listnode import ListNode
# Recursive


def reverseList(head: ListNode) -> ListNode:
    if not head.next:
        return head
    start = reverseList(head.next)
    node = start
    while node.next:
        node = node.next
    node.next = head
    head.next = None
    return start
# Iteration


def reverseList0(head: ListNode) -> ListNode:
    if not head:
        return
    pre = head
    cur = head.next
    while cur:
        temp = cur.next
        cur.next = pre
        pre = cur
        cur = temp
    head.next = None
    return pre


head = ListNode(0)
node = head
for i in range(1, 5):
    node.next = ListNode(i)
    node = node.next

head.lnprint()
ans = reverseList0(head)
ans.lnprint()
