import sys

# 모험가 수
N = int(sys.stdin.readline())
# 공포도 리스트
scared = list(map(int, sys.stdin.readline().split()))
# 내림차순 정렬
scared.sort(reverse=True)

# 모험가 그룹의 수
count = 0
while scared:
    # 현재 공포도의 최댓값
    x = scared[0]
    if len(scared) < x:
        break
    # 공포도 크기만큼 모험가 수 지우기
    scared = scared[x:]
    count += 1

print(count)