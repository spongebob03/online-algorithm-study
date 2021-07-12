import sys

# 입력 받아오기 
inputs = list(map(int, sys.stdin.read().split()))
# 여행지의 수
N = inputs[0]
# 여행 계획 속 여행지의 개수 
M = inputs[1]
# 연결 정보
graph = inputs[2:(N*N)+2]
links = []
for i, g in enumerate(graph):
    if g == 1:
        # 상삼각행렬 내 좌표로 변환 
        link = sorted((i//5+1, i%5+1))
        if link not in links:
            links.append(link)

# 여행 계획
# 여행 계획 내 여행지가 같은 집합에 있으면 가능 
plans = inputs[(N*N)+2:]

# x가 속한 집합 찾기 
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 집합 합치기 
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a 
    else:
        parent[a] = b

# 부모 테이블을 자기 자신으로 초기화 
parent = [0] * (N+1)
for i in range(1, N+1):
    parent[i] = i

# 연결되어 있으면 같은 집합으로 합치기 
for a, b in links:
    union_parent(parent, a, b)

# 계획에 있는 도시들이 속한 집합들 
plan_parents = []
for plan in plans:
    plan_parents.append(find_parent(parent, plan))

# 계획에 있는 모든 도시들이 같은 집합에 속해있으면 성공 
if len(set(plan_parents)) == 1:
    print('YES')
else:
    print('NO')
