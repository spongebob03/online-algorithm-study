import sys

INF = int(1e9)

# 입력 받아오기 
inputs = list(map(int, sys.stdin.read().split()))
# 도시의 개수 
n = inputs[0]
# 버스의 개수 
m = inputs[1]
# 버스 노선
routes = inputs[2:]

graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(0, len(routes), 3):
    a, b, c = routes[i], routes[i+1], routes[i+2]
    # 여러 노선 중 비용이 최소인 것만 
    graph[a][b] = min(graph[a][b], c)

# 플로이드 워셜 알고리즘 
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
            
for a in range(1, n+1):
    for b in range(1, n+1):
        # 자기 자신으로 가는 경우나 INF일 경우 0  
        if b == a or graph[a][b] == INF:
            print(0, end=' ')
        else:
            print(graph[a][b], end=' ')
    print()
        