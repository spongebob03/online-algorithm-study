import sys

# 입력 받아오기 
inputs = sys.stdin.readlines()
# 행성의 수
N = int(inputs[0])

# 각 행성의 좌표 
coords = []
for planet in inputs[1:]:
    x, y, z = map(int, planet.split())
    coords.append((x, y, z))

# 각 행성 사이의 거리
edges = []
for i, coord in enumerate(coords):
    for j, other in enumerate(coords):
        if i < j:
            x, y, z = coord
            a, b, c = other
            cost = min(abs(x-a), abs(y-b), abs(z-c))
            edges.append((cost, i, j))
edges.sort()

# 각 행성의 부모를 자기 자신으로 초기화 
parent = [0] * N
for i in range(N):
    parent[i] = i
    
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
        
result = 0
# 크루스칼 알고리즘 
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        
print(result)