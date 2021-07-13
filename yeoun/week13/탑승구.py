import sys
import heapq

# 입력 받아오기 
inputs = list(map(int, sys.stdin.read().split()))
# 탑승구 개수
G = inputs[0]
# 비행기 개수 
P = inputs[1]
# 각 비행기의 도킹 가능 번호 
dockings = inputs[2:]

# 도킹 가능하면 True, 아니면 False 
def dock(dockings):
    # 도킹해야 할 비행기 개수 
    N = len(dockings)
    # max heap
    q = [(-1)*d for d in dockings]
    heapq.heapify(q)
    
    while q:
        max_gate = heapq.heappop(q)
        # 게이트 최댓값이 N 이상이면, 최댓값 게이트에 비행기 도킹
        if max_gate * (-1) >= N:
            N -= 1 
        else:
            break
            
    # 도킹해야 할 비행기가 남아있지 않으면 True, 남아 있으면 False 
    return True if len(q) == 0 else False   
    
    
# 최댓값: 탑승구 개수 
max_val = G
# 최솟값: 1 
min_val = 1 

answer = None 
# 이진 탐색 
while min_val <= max_val:
    mid_val = (min_val + max_val) // 2 
    # 도킹 가능하면 우선 answer에 현재 중간값 저장
    # 더 많은 비행기 도킹할 수 있는지 확인 
    if dock(dockings[:mid_val]):
        answer = mid_val
        min_val = mid_val + 1 
    # 도킹할 수 없으면 중간값 줄이기 
    else:
        max_val = mid_val - 1 

print(answer)
    