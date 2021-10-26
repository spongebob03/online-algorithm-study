# 100%에서 틀림.. 돌겠어요
import sys
N = int(sys.stdin.readline())
graph = [N] * (N+1)
prev_graph = [N] * (N+1)
graph[1] = 0

for i in range(1,N):
    if i*3 <= N:
        if graph[i*3] > graph[i]+1:
            prev_graph[i*3] = i
        graph[i*3] = min(graph[i]+1, graph[i*3])
    if i*2 <= N:
        if graph[i*2] > graph[i]+1:
            prev_graph[i*2] = i
        graph[i*2] = min(graph[i]+1, graph[i*2])
    if i+1 <= N:
        if graph[i+1] > graph[i]+1:
            prev_graph[i+1] = i
        graph[i+1] = min(graph[i]+1, graph[i+1])

print(graph[-1])
i = N 
hist = [N]
while prev_graph[i] > 1:
    hist.append(prev_graph[i])
    i = prev_graph[i]
print(*(hist+[1]))