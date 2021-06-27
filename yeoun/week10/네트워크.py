def dfs(node, computers, visited):
    visited[node] = True 
    
    for i, neighbor in enumerate(computers[node]):
        # 인접노드 중 자기 자신이 아니고 아직 방문하지 않은 노드에 대해 
        if neighbor > 0 and i != node and visited[i] == False:
            dfs(i, computers, visited)
    return visited

def solution(n, computers):
    answer = 1
    visited = [False] * n
    startNode = 0
    
    # 모두 방문할 때까지 
    while True: 
        visited = dfs(startNode, computers, visited)
        if False in visited:
            startNode = visited.index(False)
            answer += 1
        else:
            break

    return answer