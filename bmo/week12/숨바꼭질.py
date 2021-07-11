import heapq

def dijkstra(graph, start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)

        if distance[now] < dist:
            continue

        for e, c in graph[now]:
            cost = dist + c

            if cost < distance[e]:
                distance[e] = cost
                heapq.heappush(queue, (cost, e))

    return max(distance[1:])

if __name__ == '__main__':
    INF = int(1e9)
    f = open('bmo/week12/input4.txt','r')
    n, m = map(int, f.readline().split())
    
    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)

    for _ in range(m):
        a, b = map(int, f.readline().split())
        graph[a].append((b, 1))
        graph[b].append((a, 1))

    max_dist = dijkstra(graph, 1)
    print(distance.index(max_dist), max_dist, distance.count(max_dist))
