import sys
# N: 공의 개수, M: 무게의 범위
N, M = map(int, sys.stdin.readline().split())
balls = list(map(int, sys.stdin.readline().split()))

# nC2
total = N * (N-1) / 2

# 같은 무게의 공을 고르는 경우 
duplicates = 0
for m in range(1, M+1):
    dups = balls.count(m)
    if dups > 1:
        # dups C 2 
        duplicates += dups * (dups-1) / 2

print(int(total - duplicates))