import sys
import heapq

INF = int(1e9)

# 입력 받아오기 
inputs = list(map(int, sys.stdin.read().split()))
N = inputs[0]
M = inputs[1]
routes = inputs[2:]

graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

for i in range(0, len(routes), 2):
    a, b = routes[i], routes[i+1]
    # 양방향
    graph[a].append((b,1))
    graph[b].append((a,1))

# 다익스트라 알고리즘 
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue 
        for i in graph[now]:
            # i[0]: 헛간 번호
            # i[1]: 거리 
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))
                
dijkstra(1)

# 가장 먼 헛간의 최단거리 
max_dist = max(distance[1:])
# 가장 먼 헛간의 최단거리만큼 떨어진 헛간들의 리스트 
max_barns = [i for i, dist in enumerate(distance) if dist == max_dist]
# 가장 먼 헛간의 최단거리만큼 떨어진 헛간들 중 헛간 번호가 가장 작은 것, 가장 먼 헛간의 최단거리, 가장 먼 헛간의 최단거리만큼 떨어진 헛간들의 개수
print(min(max_barns), max_dist, len(max_barns), sep=' ')