from collections import defaultdict

class Graph():
    def __init__(self, N, vertex):
        self.N = N
        self.vertex = vertex 
        self.neighbor = defaultdict(list)
        
        for v in vertex:
            self.neighbor[v[0]].append(v[1])
            self.neighbor[v[1]].append(v[0])

            
    def path(self, end, start = 1, real_start = 1, hist = [[]]):
        
        # 한 번에 갈 수 있는 길이 있는 경우 
        if end in self.neighbor[start]:
            if start in hist[-1]:
                hist[-1] += [end]
            else:
                hist[-1] += [start, end]
        
        # 경유가 필요한 경우 
        else:
            for n in self.neighbor[start]:  
                if start == real_start and hist[-1]:
                    hist.append([])
                
                if not hist or (hist and n not in hist[-1]):
                    if start in hist[-1]:
                        hist[-1] += [n]
                    else:
                        hist[-1] += [start, n]
                        
                    self.path(end = end, start = n, real_start = 1, hist = hist)  

        return hist
    
    
    
def solution(n, edge):
    path_len = []
    graph = Graph(n, edge)
    
    for i in range(2, n+1):
        hist = graph.path(i, hist = [[]])
        hist.sort(key = lambda x: len(x))
        path_len.append(len(hist[0]))
    
    max_path_len = max(path_len)
    
    return path_len.count(max_path_len)