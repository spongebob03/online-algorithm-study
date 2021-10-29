from collections import deque

def update_rank(graph, a, b):
    if graph[a][b]:
        graph[a][b] = False
        graph[b][a] = True
        indegree[a] += 1
        indegree[b] -= 1
    else:
        graph[a][b] = True
        graph[b][a] = False
        indegree[a] += 1
        indegree[b] -= 1

if __name__ == '__main__':
    f = open('bmo/week20/input1.txt', 'r')

    for tc in range(int(f.readline())):
        n = int(f.readline())

        indegree = [0] * (n+1)
        graph = [[False] * (n+1) for i in range(n+1)]

        data = list(map(int, f.readline().split()))

        for i in range(n):
            for j in range(i+1, n):
                # data[i] 상위 -> data[j] 하위
                graph[data[i]][data[j]] = True
                indegree[data[j]] += 1

        for i in range(int(f.readline())):
            a, b = map(int, f.readline().split())

            update_rank(graph, a, b)

        result = []
        queue = deque()

        for i in range(1, n+1):
            if indegree[i] == 0:
                queue.append(i)

        only = True
        cycle = False

        for i in range(n):
            if len(queue) == 0:
                cycle = True
                break
            
            if len(queue) >= 2:
                only = False
                break

            now = queue.popleft()
            result.append(now)

            for i in range(1, n+1):
                if graph[now][i]:
                    indegree[i] -= 1

                    if indegree[i] == 0:
                        queue.append(i)

        if cycle:
            print("IMPOSSIBLE")
        elif not only:
            print("?")
        else:
            print(' '.join(list(map(str, result))))