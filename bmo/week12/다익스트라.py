import heapq

def dijkstra(start):
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

if __name__ == '__main__':
    INF = int(1e9)

    f = open('input.txt', 'r')
    n, m = map(int, f.readline().split())
    start = int(f.readline())

    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)

    for _ in range(m):
        a, b, c = map(int, f.readline().split())
        graph[a].append((b, c))

    dijkstra(start)

    for i in range(1, n+1):
        if distance[i] == INF:
            print("INF")
        else:
            print(distance[i])