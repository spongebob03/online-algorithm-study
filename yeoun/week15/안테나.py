import sys

# 집의 개수
N = int(sys.stdin.readline())
# 집의 위치
houses = list(map(int, sys.stdin.readline().split()))
# 정렬
houses.sort()
# 정중앙의 집 
print(houses[N//2-1])