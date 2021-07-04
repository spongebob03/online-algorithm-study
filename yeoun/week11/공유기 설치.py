import sys

# 입력 받아오기 
inputs = list(map(int, sys.stdin.read().split()))

# 집의 개수
N = inputs[0]
# 설치할 공유기의 개수 
C = inputs[1]
# 집의 좌표들
homes = inputs[2:]

# 오름차순으로 정렬
homes.sort()

# 최대 떨어진 거리
max_gap = homes[-1] - homes[0]
# 최소 떨어진 거리 
min_gap = 1 
answer = None

# 이진 탐색 
while min_gap <= max_gap:
    # 떨어진 거리의 중간값 
    mid_gap = (max_gap + min_gap) // 2
    
    # 현재 공유기를 설치한 집의 좌표 
    current = homes[0]
    # mid_gap에 따라 설치할 수 있는 공유기의 개수 
    count = 1
    
    for i in range(1, N):
        # 직전에 설치한 공유기보다 mid_gap 이상 떨어진 곳에 공유기 설치
        if homes[i] >= current + mid_gap:
            current = homes[i]
            count += 1 
    
    # C 이상의 공유기를 설치할 수 있는 경우 
    if count >= C:
        # 격차를 늘림 
        min_gap = mid_gap + 1 
        # 현재 격차를 answer로 중간 저장 
        answer = mid_gap
    # C보다 적은 공유기만 설치할 수 있는 경우 
    else:
        # 격차를 줄임 
        max_gap = mid_gap - 1 

print(answer)