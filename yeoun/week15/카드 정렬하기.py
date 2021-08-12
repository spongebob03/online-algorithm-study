import sys
import heapq

# 카드 묶음의 개수
N = int(sys.stdin.readline())
# 각 카드 묶음의 크기
cards = []
for i in range(N):
    cards.append(int(sys.stdin.readline()))
heapq.heapify(cards)

result = []
while len(cards) > 1:
    # 최솟값 2개 뽑아 섞기
    mix = heapq.heappop(cards) + heapq.heappop(cards)
    result.append(mix)
    # 섞은 뭉텅이를 다시 cards에 넣기
    heapq.heappush(cards, mix)

print(sum(result))
# python3 solution.py < input.txt