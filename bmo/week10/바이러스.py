def dfs(graph, v, visited,r):
    visited[v] = True
    r.add(v)

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited, r)
    return r

# input & run DFS
if __name__ == '__main__':
    n = int(input())
    graph = [[] for _ in range(n+1)]
    
    m = int(input())
    visited = [False] * (n+1)
    
    for _ in range(m):
        i, j = list(map(int, input().split()))
        
        graph[i].append(j)
        graph[j].append(i)
    
    for _ in range(1, n+1):
        graph[i].sort()
    
    count = 1
    r = set()
    r = dfs(graph, 1, visited, r)
    print(len(r)-1)
    