"""
symmetric tree
root 는 binary tree
invert left & is same left and right
"""
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert(root: Optional[TreeNode]):
    if root is None:
        return

    tmp = root.left
    root.left = root.right
    root.right = tmp

    invert(root.left)
    invert(root.right)

    return root


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]):
    if p is None and q is None:
        return True
    elif p is None or q is None:
        return False

    queue = deque()
    queue.append([p, q])

    while queue:
        n1, n2 = queue.popleft()

        if n1.val != n2.val:
            return False

        if n1.left is not None and n2.left is not None:
            queue.append([n1.left, n2.left])
        elif n1.left is None and n2.left is None:
            pass
        else:
            return False

        if n1.right is not None and n2.right is not None:
            queue.append([n1.right, n2.right])
        elif n1.right is None and n2.right is None:
            pass
        else:
            return False

    return True

def solve(root: Optional[TreeNode]):
    if not root:
        return False

    inverted = invert(root.left)
    answer = is_same_tree(inverted, root.right)

    return answer


if __name__ == '__main__':
    root = TreeNode(val=1, left=TreeNode(val=2, left=TreeNode(val=3), right=TreeNode(val=4)), right=TreeNode(val=2, left=TreeNode(val=4), right=TreeNode(val=3)))
    solve(root)

    root = TreeNode(val=1, left=TreeNode(val=2, right=TreeNode(val=3)), right=TreeNode(val=2, right=TreeNode(val=3)))
    solve(root)
