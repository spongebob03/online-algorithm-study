# 플로이드 워셜인가?
def floyd(graph, n):
    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

if __name__ == '__main__':
    INF = int(1e9)
    f = open('bmo/week18/input1.txt', 'r')
    n, m, k, x = map(int, f.readline().split())

    graph = [[INF] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        graph[i][i] = 0

    for _ in range(m):
        a, b = map(int, f.readline().split())
        graph[a][b] = 1

    floyd(graph, n)

    answer = []
    for i in range(1, n+1):
        if graph[x][i] == k:
            answer.append(i)
    
    if not answer:
        print(-1)
    else:
        for idx in answer:
            print(idx)
    
