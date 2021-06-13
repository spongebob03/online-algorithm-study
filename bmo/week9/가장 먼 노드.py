from collections import deque

def bfs(graph, start):
    visited = {}
    queue = deque([[start, 0]])

    while queue:
        node, length = queue.popleft()
        if node not in visited:
            visited[node] = length
            queue += ([[node, length+1] for node in set(graph[node]).difference(set(visited))])
    print(visited)
    return visited

def solution(n, vertex):
    graph = {}
    for source, dest in vertex:
        graph[source] = graph.get(source, []) + [dest]
        graph[dest] = graph.get(dest, []) + [source]

    distance = bfs(graph, 1)
    distance = list(distance.values())
    return distance.count(max(distance))


if __name__ == '__main__':
    print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))