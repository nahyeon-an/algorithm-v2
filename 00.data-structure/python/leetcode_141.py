from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return f"Node(val={self.val}, next={self.next})"


def make_list(arr, pos):
    head = None
    prev = None
    tail_next = None

    for i in range(len(arr)):
        cur = ListNode(arr[i])
        if i == pos:
            tail_next = cur
        if i == 0:
            head = cur
            prev = head
            continue
        prev.next = cur
        prev = prev.next

    prev.next = tail_next

    return head


def solve(head: Optional[ListNode]):
    """
    cycle 이 존재하면 true, else false 를 리턴해라
    """
    cur = head
    i = 0
    visited = {}

    while cur:
        if cur in visited:
            return True
        visited[cur] = i
        cur = cur.next
        i += 1

    return False


list1 = make_list([3, 2, 0, -4], 1)
solve(list1)

list2 = make_list([1, 1], 0)
solve(list2)

list3 = make_list([1], -1)
solve(list3)
