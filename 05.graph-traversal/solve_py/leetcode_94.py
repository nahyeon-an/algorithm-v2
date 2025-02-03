"""
binary tree 가 주어짐 -> inorder (중위) 순회
"""
from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: TreeNode = left
        self.right: TreeNode = right

    def add(self, val):
        queue = deque([self])

        while queue:
            cur = queue.popleft()

            if cur.val is None:
                continue

            if cur.left is not None:
                queue.append(cur.left)
            else:
                cur.left = TreeNode(val=val)
                break

            if cur.right is not None:
                queue.append(cur.right)
            else:
                cur.right = TreeNode(val=val)
                break

    def print(self):
        queue = deque([(self, 0)])
        results = []

        while queue:
            cur, level = queue.popleft()

            if len(results) <= level:
                results.append([])

            results[level].append(cur.val)

            if cur.left is not None:
                queue.append((cur.left, level + 1))

            if cur.right is not None:
                queue.append((cur.right, level + 1))

        for i, nums in enumerate(results):
            print(f"{i}: {nums}")


def inorder_traversal(root: Optional[TreeNode]) -> List[int]:

    results = []

    def recursive(node: TreeNode):
        if node is None or node.val is None:
            return

        recursive(node.left)
        results.append(node.val)
        recursive(node.right)

    recursive(root)

    return results

root = TreeNode(val=1)
root.add(None)
root.add(2)
root.add(3)
inorder_traversal(root)
