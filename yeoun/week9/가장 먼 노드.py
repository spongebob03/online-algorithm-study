from collections import defaultdict, deque

def solution(n, vertex):    
    # 한 번에 갈 수 있는 간선이 있는 노드들
    neighbor = defaultdict(list)

    for v in vertex:
        neighbor[v[0]].append(v[1])
        neighbor[v[1]].append(v[0])
        
    # 출발지는 1번 노드
    hist = deque([(1,0)])
    # key: 노드 번호, value: 1번 노드로부터의 거리 
    distance = {}
    
    while hist:
        node = hist.popleft()
        # 현재 노드에 이웃한 노드들에 대해 
        for n in neighbor[node[0]]:
            if n not in distance and n != 1:
                distance[n] = node[1] + 1 
                hist.append((n, node[1]+1))
                    
    # 1번 노드로부터 가장 멀리 떨어진 노드의 거리 
    max_distance = max(distance.values())
    return len([k for k, v in distance.items() if v == max_distance])
