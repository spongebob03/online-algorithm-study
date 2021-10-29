import sys

N = int(sys.stdin.readline())
# 5kg 봉지로 최대한 옮길 때, 필요한 봉지의 개수 
q5 = N // 5

# 정확히 Nkg을 만들 수 없으면 -1 
answer = -1
# q5에서 하나씩 빼가면서 0까지 
# ex) q5가 3이면, i는 3,2,1,0
for i in range(q5,-1,-1):
    # 5kg으로 최대한 옮기고 남은 무게가 3의 배수일 때 
    if (N - i*5) % 3 == 0:
        answer = i + (N - i * 5) // 3
        break

print(answer) 