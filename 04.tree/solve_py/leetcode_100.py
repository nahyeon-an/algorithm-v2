"""
same tree

same?
- 구조가 같고
- 노드의 값이 같음

p, q 를 동시에 모든 노드 방문하면서 비교
"""
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solve(p: Optional[TreeNode], q: Optional[TreeNode]):

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

        # 왼쪽 서브트리 비교
        if (n1.left and not n2.left) or (not n1.left and n2.left):
            return False
        if n1.left and n2.left:
            queue.append((n1.left, n2.left))

        # 오른쪽 서브트리 비교
        if (n1.right and not n2.right) or (not n1.right and n2.right):
            return False
        if n1.right and n2.right:
            queue.append((n1.right, n2.right))

    return True


if __name__ == '__main__':
    p = TreeNode(val=1, left=TreeNode(val=2), right=TreeNode(val=3))
    q = TreeNode(val=1, left=TreeNode(val=2), right=TreeNode(val=3))
    print(solve(p, q))

    p = TreeNode(val=1, left=TreeNode(val=2))
    q = TreeNode(val=1, right=TreeNode(val=2))
    print(solve(p, q))

    p = TreeNode(val=1, left=TreeNode(val=2), right=TreeNode(val=1))
    q = TreeNode(val=1, left=TreeNode(val=1), right=TreeNode(val=2))
    print(solve(p, q))

    p = TreeNode(val=1)
    q = TreeNode(val=1, right=TreeNode(val=2))
    print(solve(p, q))

