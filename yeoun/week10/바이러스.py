import sys

# 입력 받아오기 
inputs = list(map(int, sys.stdin.read().split()))
# 총 컴퓨터 개수 
N = inputs[0]

# 인접 리스트 
adjs = []
for i in range(0,len(inputs[2:]),2):
    adjs.append(inputs[2:][i:i+2])

# 인접 행렬
graph = [[] for _ in range(N+1)]

for adj in adjs:
    a, b = adj
    graph[a].append(b)
    graph[b].append(a)

    
def dfs(start, graph, visited):
    visited[start] = True
    
    for adj in graph[start]:
        if not visited[adj]: 
            dfs(adj, graph, visited)
            
    return visited


visited = [False] * (N+1)
visited = dfs(1, graph, visited)

print(sum(visited)-1)
