from collections import defaultdict
from math import inf

class Graph():
    def __init__(self, N, road):
        self.N = N
        self.road = road 
        # 소요시간 적은 순으로 정렬
        self.road.sort(key=lambda x:x[-1])
        
        # 한 번에 갈 수 있는 다리가 있는 경우 
        self.neighbor = defaultdict(list)
        # 소요시간 
        self.distance = [[inf for n in range(N+1)] for n in range(N+1)]
        
        for r in road:
            self.neighbor[r[0]].append(r[1])
            self.neighbor[r[1]].append(r[0])
            # 두 마을을 연결하는 다리가 2개 이상일 수 있으므로 최솟값만 
            if self.distance[r[0]][r[1]] == self.distance[r[1]][r[0]] == inf:
                self.distance[r[0]][r[1]], self.distance[r[1]][r[0]] = r[2], r[2]
            
    # 출발지에서 도착지로 가는 경로를 list of list로 반환 
    def path(self, start, end, real_start, hist = [[]]):
        
        # 한 번에 갈 수 있는 길이 있는 경우 
        if end in self.neighbor[start]:
            if start in hist[-1]:
                hist[-1] += [end]
            else:
                hist[-1] += [start, end]
        
        # 경유가 필요한 경우 
        else:
            for n in self.neighbor[start]:  
                if start == real_start:
                    hist.append([])
                
                if not hist or (hist and n not in hist[-1]):
                    if start in hist[-1]:
                        hist[-1] += [n]
                    else:
                        hist[-1] += [start, n]
                        
                    self.path(n, end, real_start, hist)
        return hist
    
    # 출발지에서 도착지로 가는 경로를 입력 받으면 소요시간을 계산 
    def get_time(self, p):
        # 경로가 비어 있는 경우 갈 수 없으므로 K의 최댓값보다 큰 값을 반환 
        if not p:
            return 500001
        
        time = 0 
        for i in range(len(p)-1):
            time += self.distance[p[i]][p[i+1]]
        return time 
    
    
def solution(N, road, K):
    # 항상 1번 마을은 갈 수 있으므로 1로 초기화 
    answer = 1 
    graph = Graph(N, road)
    
    for i in range(2, N+1):
        hist = graph.path(1, i, 1, hist=[[]])
        
        for h in hist:
            t = graph.get_time(h)
            if t <= K:
                answer += 1 
                break 
    
    return answer