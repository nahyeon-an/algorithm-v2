"""
nums -> 가장 길게 연결된 엘리먼트의 길이를 리턴
O(n) -> 모든 원소를 한번씩 돌면서 즉시 정렬 필요함
ex) nums = [100, 4, 200, 1, 3, 2] -> [1,2,3,4] ans = 4

연속된 : 1 씩 차이나는 숫자들
"""


def solve(nums: list[int]):
    par = {n: n for n in nums}

    def get_parent(parent, x):
        if parent[x] != x:
            parent[x] = get_parent(parent, parent[x])
        return parent[x]

    def union(parent, x, y):
        parent_x = get_parent(parent, x)
        parent_y = get_parent(parent, y)
        if parent_x < parent_y:
            parent[y] = parent_x
        elif parent_x > parent_y:
            parent[x] = parent_y
        else:
            parent[x] = parent_x
            parent[y] = parent_y

    for n in nums:
        if n - 1 in par:
            union(par, n, n - 1)
        if n + 1 in par:
            union(par, n, n + 1)

    print(par)

    counts = {}
    max_length = 0
    for val in par.values():
        root = get_parent(par, val)
        if root not in counts:
            counts[root] = 0

        counts[root] += 1
        max_length = max(max_length, counts[root])

    return max_length


if __name__ == '__main__':
    solve([100, 4, 200, 1, 3, 2])
    solve([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
    solve([1, 0, 1, 2])
    solve([7,-2,9,9,1,9,8,-4,6,-6,-6,4,1,3,6,3,5,-2,3,4,-6,1,5,-9,6,1,2,-2,1])
    solve([7,9,9,1,9,8,6,4,1,3,6,3,5,3,4,1,5,6,1,2,1])
