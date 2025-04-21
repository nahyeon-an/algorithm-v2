from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


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
    cycle 이 존재하면 시작 노드를 리턴 else None
    """
    cur = head
    i = 0
    visited = {}

    while cur:
        if cur in visited:
            return cur
        visited[cur] = i
        cur = cur.next
        i += 1

    return None


list1 = make_list([3, 2, 0, -4], 1)
solve(list1)

list2 = make_list([1, 1], 0)
solve(list2)

list3 = make_list([1], -1)
solve(list3)
