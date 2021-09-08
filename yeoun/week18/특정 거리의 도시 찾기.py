import sys
from collections import defaultdict, deque

# N: 도시의 개수
# M: 도로의 개수
# K: 타겟 최단 거리
# X: 출발 도시
N, M, K, X = map(int, sys.stdin.readline().split())

INF = 300001
# X에서 각 도시까지의 거리 INF로 초기화
dist = [INF for _ in range(N+1)]
# X에서 X까지의 거리는 0
dist[X] = 0
# 재방문 방지
visited = [False for _ in range(N + 1)]

# 단방향 도로의 출발지가 key, 도착지가 value
roads = defaultdict(list)
for _ in range(M):
    k, v = map(int, sys.stdin.readline().split())
    roads[k].append(v)

def bfs(start):
    q = deque([start])
    visited[start] = True
    while q:
        cur = q.popleft()
        for node in roads[cur]:
            if not visited[node]:
                visited[node] = True
                dist[node] = min(dist[node], dist[cur] + 1)
                q.append(node)
    return dist

result = bfs(X)

answer = [i for i,d in enumerate(result) if d == K]
if not answer:
    print(-1)
else:
    for ans in answer:
        print(ans)