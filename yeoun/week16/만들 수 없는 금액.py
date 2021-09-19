import sys

N = sys.stdin.readline()
coins = list(map(int, sys.stdin.readline().split()))
coins.sort()

# 주어진 동전으로 만들 수 있는 모든 금액을 구함
def possible_amount(coins):
    first2 = coins[:2]
    # 가장 금액이 작은 두 동전으로 이루어진 집합
    amounts = set(first2)
    # 가장 금액이 작은 두 동전의 합
    amounts.add(sum(first2))
    # 세 번째 동전부터 하나씩 꺼내면서, 각 amount 값에 동전 금액 만큼 더함
    for i in range(len(coins[2:])):
        amounts |= set([a + coins[i+2] for a in amounts])
    return list(amounts)

possibles = possible_amount(coins)

# 가장 작은 만들 수 있는 금액
prev = possibles.pop(0)
# 1이 아니면 1원을 만들 수 없는 거니까 1을 프린트
if prev != 1:
    print(1)
else:
    for p in possibles:
        # 연속된 숫자가 아니면 
        if prev + 1 != p:
            print(prev+1)
            break
        else:
            prev += 1
