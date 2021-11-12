from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])

    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    # 출발점에서의 distance를 잘 저장

if __name__ == '__main__':
    f = open('bmo/week18/input1.txt', 'r')
    n, m, k, x = map(int, f.readline().split())

    graph = [[] for _ in range(n+1)]

    for i in range(m):
        source, des = map(int, f.readline().split())
        graph[source].append(des)

    visited = [False] * (n+1)
    bfs(graph, x, visited)