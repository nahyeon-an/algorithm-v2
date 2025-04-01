"""
Invert binary tree
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node(val={self.val}, left={self.left}, right={self.right})"

def solve(root: Optional[TreeNode]):
    if root is None:
        return

    tmp = root.left
    root.left = root.right
    root.right = tmp

    solve(root.left)
    solve(root.right)

    return root


if __name__ == '__main__':
    # root = TreeNode(val=2, left=TreeNode(val=1), right=TreeNode(val=3))
    root = TreeNode(val=4, left=TreeNode(val=2, left=TreeNode(val=1), right=TreeNode(val=3)), right=TreeNode(val=7, left=TreeNode(val=6), right=TreeNode(val=9)))
    solve(root)
    print(root)
    print(solve(None))
