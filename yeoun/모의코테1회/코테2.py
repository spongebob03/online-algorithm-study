# https://www.acmicpc.net/problem/13913
import heapq
INF = 1e9
inputs = list(map(int, input().split()))
N, K = inputs
distance = [INF] * (K+2)
from_table = [INF] * (K+2)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    from_table[start] = start
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in [(1, now+1), (1, now-1), (1, 2*now)]:
            cost = dist + i[0]
            if i[1] in range(0, len(distance)) and cost < distance[i[1]]:
                heapq.heappush(q, (cost, i[1]))
                distance[i[1]] = cost
                from_table[i[1]] = now

                
dijkstra(N)


print(distance[K])

now = K
path = []
while now != N:
    path.append(now)
    now = from_table[now]
    
path += [N]

for p in path[::-1]:
    print(p, end=' ')