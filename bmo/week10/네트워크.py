def dfs(graph, v, visited):
    visited[v] = True

    for i in range(len(graph)):
        if graph[v][i] == 1 and not visited[i]:
            dfs(graph, i, visited)

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for start in range(n):
        if not visited[start]:
            dfs(computers, start, visited)
            answer += 1
    
    return answer