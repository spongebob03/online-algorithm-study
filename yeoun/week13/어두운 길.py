import sys

# 입력 받아오기 
inputs = list(map(int, sys.stdin.read().split()))
# 집의 수 
N = inputs[0]
parent = [0] * N 
for i in range(N):
    parent[i] = i
    
# 도로의 수 
M = inputs[1]

# (도로의 길이, 도로가 잇는 집1, 도로가 잇는 집2)
edges = []
total_cost = 0
for i in range(0, len(inputs[2:]), 3):
    a, b, cost = inputs[2:][i], inputs[2:][i+1], inputs[2:][i+2]
    edges.append((cost, a, b))
    total_cost += cost
    
# 도로 길이가 짧은 순으로 정렬
edges.sort()

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b 

# 크루스칼 알고리즘 
min_cost = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        min_cost += cost 
        
print(total_cost - min_cost)