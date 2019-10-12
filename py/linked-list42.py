#! usr/bin/python3
from listnode import ListNode


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    queue = []
    if not head.next:
        return None
    node = head
    while node:
        queue.append(node)
        if len(queue) > n+1:
            del queue[0]
        node = node.next
    queue[-(n-1)].next = queue[-n].next
    return head


head = ListNode(0)
node = head
for i in range(1, 5):
    node.next = ListNode(i)
    node = node.next

head.lnprint()
ans = removeNthFromEnd(head, 3)
ans.lnprint()
