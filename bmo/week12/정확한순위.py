INF = int(1e9)

def floyd(graph, n):
    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

def solution(graph, n):
    floyd(graph, n)

    answer = 0
    for i in range(1, n+1):
        count = 0
        for j in range(1, n+1):
            if graph[i][j] != INF or graph[j][i] != INF:
                count += 1
        if count == n:
            answer += 1
    print(answer)

if __name__ == '__main__':
    f = open('bmo/week12/input2.txt', 'r')
    n, m = map(int, f.readline().split())
    graph = [[INF]* (n+1) for _ in range(n+1)]
    for a in range(1, n+1):
        graph[a][a] = 0

    for _ in range(m):
        a, b = map(int, f.readline().split())
        graph[a][b] = 1
        
    solution(graph, n)