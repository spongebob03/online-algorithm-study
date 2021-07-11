def floyd(graph, n):
    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

if __name__ == '__main__':
    INF = int(1e9)
    f = open('bmo/week12/input1.txt', 'r')
    n = int(f.readline())
    m = int(f.readline())

    graph = [[INF] * (n+1) for _ in range(n+1)]
    for a in range(1 , n+1):
        for b in range(1, n+1):
            if a == b:
                graph[a][b] = 0

    for _ in range(m):
        a, b, c = map(int, f.readline().split())
        if graph[a][b] > c:
            graph[a][b] = c
    
    floyd(graph, n)
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] == INF:
                print(0, end=' ')
            else:
                print(graph[i][j], end=' ')
        print()
