from typing import List
from collections import deque


def solve(equations: List[List[str]], values: List[float], queries: List[List[str]]):
    """
    weighted matrix
    equation 개수 <= 20 : matrix 는 최대 20 * 20 = 400 size
    노드는 최대 5개의 문자로 이루어 질 수 있음 ex. abcde
    """
    graph = {}

    for i in range(len(equations)):
        if equations[i][0] not in graph:
            graph[equations[i][0]] = []
        graph[equations[i][0]].append((equations[i][1], values[i]))

        if equations[i][1] not in graph:
            graph[equations[i][1]] = []
        graph[equations[i][1]].append((equations[i][0], 1 / values[i]))

    answers = []
    for x, y in queries:
        if x not in graph or y not in graph:
            answers.append(-1.0)
            continue

        visited = {node: False for node in graph}

        # x -> ... -> y 경로 찾아야 함
        q = deque()
        q.append((x, 1.0))
        visited[x] = True
        answer = -1.0

        while q:
            n, weight = q.popleft()
            visited[n] = True

            if n == y:
                answer = weight
                break

            # 인접 노드 가져오기
            for neighbor in graph[n]:
                # neighbor[0] 을 이미 방문했다면 pass
                if visited[neighbor[0]]:
                    continue
                q.append((neighbor[0], neighbor[1] * weight))

        answers.append(answer)

    print(graph)

    return answers


solve([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]])
solve([["a","b"],["b","c"],["bc","cd"]], [1.5,2.5,5.0], [["a","c"],["c","b"],["bc","cd"],["cd","bc"]])
solve([["a","b"]], [0.5], [["a","b"],["b","a"],["a","c"],["x","y"]])
solve([["a","b"],["c","d"]], [1.0,1.0], [["a","c"],["b","d"],["b","a"],["d","c"]])
solve([["a","b"],["b","c"],["a","c"],["d","e"]], [2.0,3.0,6.0,1.0], [["a","c"],["b","c"],["a","e"],["a","a"],["x","x"],["a","d"]])
