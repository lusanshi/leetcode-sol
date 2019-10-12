#! usr/bin/python3
from listnode import ListNode


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    if not l2 or not l1:
        return l1 or l2
    if l1.val > l2.val:
        l1, l2 = l2, l1
    head = l1
    while l1.next and l2:
        if l2.val < l1.next.val:
            next1, next2 = l1.next, l2.next
            l1.next, l2.next = l2, next1
            l1, l2 = l2, next2
        else:
            l1 = l1.next
    if l2:
        l1.next = l2
    return head


arr1 = [-10, -9, -6, -4, 1, 9, 9]
arr2 = [-5, -3, 0, 7, 8, 8]
l1 = ListNode(arr1[0])
node = l1
for i in arr1[1:]:
    node.next = ListNode(i)
    node = node.next
ListNode.lnprint(l1)

l2 = ListNode(arr2[0])
node = l2
for i in arr2[1:]:
    node.next = ListNode(i)
    node = node.next
ListNode.lnprint(l2)

l0 = mergeTwoLists(l1, l2)
ListNode.lnprint(l0)
