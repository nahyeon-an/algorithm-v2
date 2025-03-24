"""
unique binary search tree 2
모든 unique BST 의 구조를 리스트로 리턴해라
1 ~ n
1 <= n <= 8

divide and conquer
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val}, left = {self.left}, right = {self.right})"


def make_tress(start, end):
    """
    사용할 수 있는 숫자 n 개
    """
    if start > end:
        return [None]

    trees = []
    for val in range(start, end + 1):
        left = make_tress(start, val - 1)
        right = make_tress(val + 1, end)

        # left 와 right 의 조합
        for node1 in left:
            for node2 in right:
                node: TreeNode = TreeNode(val=val)
                node.left = node1
                node.right = node2
                trees.append(node)

    return trees

def solve(n: int):
    trees = make_tress(1, n)
    return trees


solve(1)
solve(2)
solve(3)
