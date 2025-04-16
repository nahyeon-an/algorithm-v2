from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode(val={self.val}, next={self.next})"


def find_middle(head):
    if not head or not head.next:
        return None

    slow, fast = head, head
    prev = None

    while fast and fast.next:
        prev = slow
        slow = slow.next  # 1개의 노드를 움직임
        fast = fast.next.next  # 2개의 노드를 움직임

    if prev:
        prev.next = None

    return slow


def reverse(head):
    prev = None
    while head:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node
    return prev


def merge(node1, node2):
    while node1 and node2:
        n1_next = node1.next
        n2_next = node2.next

        node1.next = node2
        if not n1_next:
            break
        node2.next = n1_next

        node1 = n1_next
        node2 = n2_next


def solve(head: Optional[ListNode]):
    """
    head 의 노드와 tail 의 노드를 번갈아 가며 reorder
    """
    # 1. find middle node
    mid = find_middle(head)
    if not mid:
        return

    # 2. reverse
    right = reverse(mid)

    # 3. merge
    merge(head, right)

    print(head)


if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    solve(head)

    head2 = ListNode(1)
    solve(head2)

    head3 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    solve(head3)

    head4 = ListNode(1, ListNode(4))
    solve(head4)
