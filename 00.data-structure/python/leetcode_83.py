# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def add(self, val):
        cur = self

        while cur.next is not None:
            cur = cur.next

        cur.next = ListNode(val, None)

    def print(self):
        print("[ ", end="")
        cur = self
        print(cur.val, end=" ")

        while cur.next is not None:
            cur = cur.next
            print(cur.val, end=" ")

        print("]")


def delete_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    prev, head pointer
    prev == head : remove node
    prev < head : keep going
    """

    if head is None:
        return head

    prev = head
    cur = head.next

    while cur is not None:
        if prev.val == cur.val:
            prev.next = cur.next
            cur = cur.next
        else:
            prev = cur
            cur = cur.next

    return head


if __name__ == '__main__':
    head = ListNode(1)
    head.add(1)
    head.add(2)
    head.add(3)
    head.add(3)
    head.print()

    new_head = delete_duplicates(head)
    new_head.print()
