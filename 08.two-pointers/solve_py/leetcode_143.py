from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode(val={self.val}, next={self.next})"


def solve(head: Optional[ListNode]):
    """
    head 의 노드와 tail 의 노드를 번갈아 가며 reorder
    """
    # 1. find middle node
    cur = head
    cnt = 0

    while cur:
        cur = cur.next
        cnt += 1

    if cnt <= 1:
        return

    # divide
    left_tail = None
    mid = head
    for _ in range(cnt // 2):
        left_tail = mid
        mid = mid.next

    if left_tail:
        left_tail.next = None

    #  reverse
    stack = []

    while mid:
        stack.append(mid)
        mid = mid.next

    right = stack[-1]
    while stack:
        tmp = stack.pop()
        if stack:
            tmp.next = stack[-1]
        else:
            tmp.next = None

    # merge
    prev_right = None
    left = head
    while left and right:
        tmp = left.next
        left.next = right
        left = tmp

        prev_right = right
        tmp = right.next
        right.next = left
        right = tmp

    if right:
        prev_right.next = right

    cur = head
    print(cur)
    # while cur:
    #     print(cur)
    #     cur = cur.next


if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    solve(head)

    head2 = ListNode(1)
    solve(head2)

    head3 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    solve(head3)

    head4 = ListNode(1, ListNode(4))
    solve(head4)
