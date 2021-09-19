import sys
from collections import deque

# 0과 1은 더하기, 나머지 수는 곱하기로 처리해야 함
s = [int(num) for num in sys.stdin.readline()]
s = deque(s)
# 첫 번째 숫자 
prev = s.popleft()

while s:
    current = s.popleft()
    # 연산하는 숫자 중 적어도 하나가 0 또는 1이면 더하기 
    if prev < 2 or current < 2:
        prev = prev + current
    # 그외는 모두 곱하기 
    else:
        prev = prev * current

print(prev)
