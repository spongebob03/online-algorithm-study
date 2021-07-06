import sys

INF = int(1e9)

# 입력 받아오기 
inputs = list(map(int, sys.stdin.read().split()))
# 학생 수 
N = inputs[0]
# 비교한 결과의 수 
M = inputs[1]
# 성적 비교 결과 
scores = inputs[2:]

graph = [[INF]*(N+1) for _ in range(N+1)]

for i in range(0, len(scores), 2):
    low, high = scores[i], scores[i+1]
    graph[low][high] = 1
    

# 플로이드 워셜 알고리즘 
for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
            
answer = []
for n in range(1, N+1):
    transposedGraph = list(zip(*graph))
    # 그래프의 n번째 가로줄, n번째 세로줄에서 0이 아닌 index들 + 자기 자신의 index를 합치면 1 ~ N이 되는 경우 순위를 알 수 있음 
    if set([i for i,x in enumerate(graph[n]) if x != INF] + [i for i,x in enumerate(transposedGraph[n]) if x != INF] + [n]) == set(range(1,N+1)):
        answer.append(n)

# 순위를 알 수 있는 학생의 수  
print(len(answer))


