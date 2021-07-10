import heapq
INF = int(1e9)

def dijkstra(graph, n):
    distance = [[INF] * n for _ in range(n)]

    queue = [(graph[0][0], 0, 0)]
    distance[0][0] = graph[0][0]

    DELTAS = ((1, 0), (0, 1))
    while queue:
        dist, x, y = heapq.heappop(queue)

        if distance[x][y] < dist:
            continue

        for dx, dy in DELTAS:
            next_x = x + dx
            next_y = y + dy

            if next_x < 0 or next_x >= n or next_y < 0 or next_y >= n:
                continue

            cost = dist + graph[next_x][next_y]
            if cost < distance[next_x][next_y]:
                distance[next_x][next_y] = cost
                heapq.heappush(queue, (cost, next_x, next_y))

    return distance[n-1][n-1]

if __name__ == '__main__':
    f = open('bmo/week12/input3.txt', 'r')
    t = int(f.readline())
    for _ in range(t):
        n = int(f.readline())
        graph = []
        for _ in range(n):
            graph.append(list(map(int, f.readline().split())))

        print(dijkstra(graph, n))