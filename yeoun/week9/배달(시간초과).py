from collections import defaultdict
from math import inf

# recursive 
# 시작점에서 목적지까지 가능한 모든 path를 list of list로 반환 
def __help(dest, neighbor, path, candidates):
    
    if dest in neighbor[path[-1]]:
        if dest not in path:
            candidates.append(path + [dest])
    
    # 한 번에 갈 수 있어도 돌아가는 것이 더 적은 시간이 소요될 수 있으므로 else 사용하지 않음
    for alternative in neighbor[path[-1]]:
        if alternative not in path:
            __help(dest, neighbor, path + [alternative], candidates)
        
    return candidates

# path가 주어지면 소요 시간을 계산 
def get_time(candidate, distance):
    time = 0 
    for i in range(len(candidate)-1):
        time += distance[candidate[i]][candidate[i+1]]
    return time 

def solution(N, road, K):
    answer = 1 
    
    # 한 번에 갈 수 있는 도로가 있는 마을들 
    neighbor = defaultdict(list)
    # inf로 초기화 
    distance = [[inf for n in range(N+1)] for n in range(N+1)]
    
    road.sort(key=lambda x:x[-1])
    for r in road:
        neighbor[r[0]].append(r[1])
        neighbor[r[1]].append(r[0])
        if distance[r[0]][r[1]] == distance[r[1]][r[0]] == inf:
            distance[r[0]][r[1]], distance[r[1]][r[0]] = r[2], r[2]
    
    # 항상 출발지는 1번 마을 
    path = [1]
    # 도착지는 2번 ~ N번 마을까지 
    for dest in range(2, N+1):
        candidates = __help(dest, neighbor, path, candidates = [])
    
        for candidate in candidates:
            time = get_time(candidate, distance) 
            # 소요시간이 K 이하면 answer + 1 
            if time <= K:
                answer += 1 
                break 
        
    return answer 