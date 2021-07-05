import heapq

def solution(N, road, K):
    INF = int(1e9)
    graph = [[] for _ in range(N+1)]
    distance = [INF] * (N+1)
    
    # 간선 정보 저장하기 
    for r in road:
        a, b, c = r
        # 양방향
        graph[a].append((b,c))
        graph[b].append((a,c))
    
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
    
    # K 이하의 시간에 배달이 가능한 마을의 개수 
    return len([d for d in distance if d <= K])
