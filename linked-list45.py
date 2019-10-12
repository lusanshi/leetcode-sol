#! usr/bin/python3
from listnode import ListNode


def isPalindrome(head: ListNode) -> bool:
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    for i in range(len(arr)//2):
        if arr[i] != arr[-i-1]:
            return False
    return True


arr1 = [1, 2]

l1 = ListNode(arr1[0])
node = l1
for i in arr1[1:]:
    node.next = ListNode(i)
    node = node.next
ListNode.lnprint(l1)

print(isPalindrome(l1))
