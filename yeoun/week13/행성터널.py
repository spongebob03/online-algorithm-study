import sys

# 입력 받아오기
inputs = sys.stdin.readlines()
# 행성의 수
N = int(inputs[0])

# 각 행성의 좌표
coords = []
for num, planet in enumerate(inputs[1:]):
    x, y, z = map(int, planet.split())
    coords.append((num, x, y, z))
    
# (거리, 행성1, 행성2)
edges = []

# x축 기준으로 정렬 후 거리 저장
coords.sort(key=lambda x: x[1])
for i in range(N-1):
    edges.append((coords[i + 1][1] - coords[i][1], coords[i][0], coords[i+1][0]))

# y축 기준으로 정렬 후 거리 저장
coords.sort(key=lambda x: x[2])
for i in range(N-1):
    edges.append((coords[i + 1][2] - coords[i][2], coords[i][0], coords[i+1][0]))

# z축 기준으로 정렬 후 거리 저장
coords.sort(key=lambda x: x[3])
for i in range(N-1):
    edges.append((coords[i + 1][3] - coords[i][3], coords[i][0], coords[i+1][0]))

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