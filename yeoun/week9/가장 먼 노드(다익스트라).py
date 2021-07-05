import heapq

def solution(n, edge):
    INF = int(1e9)
    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)
    
    # 간선 정보 저장하기 
    for e in edge:
        a, b = e
        # 양방향
        # 거리는 모두 1로 통일 
        graph[a].append((b,1))
        graph[b].append((a,1))
    
    # 다익스트라 알고리즘 
    def dijkstra(start):
        q = []
        distance[start] = 0
        heapq.heappush(q, (0, start))
        
        while q:
            # 최단거리 노드
            dist, now = heapq.heappop(q)
            # 이미 방문했거나 최솟값이 아닌 경우 
            if distance[now] < dist:
                continue 
            # 연결된 노드들에 대해 
            for i in graph[now]:
                cost = dist + i[1]
                # 현재 정보보다 더 적은 시간이 필요한 경우 갱신
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))
    
    dijkstra(start=1)
    max_dist = max(distance[2:])
    
    return len([d for d in distance if d == max_dist])
