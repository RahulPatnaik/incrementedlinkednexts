class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

head = ListNode(0)
tempHead = head

for i in range(1,30):
    tempHead.next = ListNode(i)
    tempHead = tempHead.next

def incrementListNode(node, n):
    while n:
        if node.next:
            node = node.next
        else:
            return None
        n -= 1
    return node

i = 1
while head:
    print(head.val)
    head = incrementListNode(head, i)
    i += 1
