from itertools import combinations 
from collections import Counter

def solution(orders, course):
    answer = []
    combs = []
    
    for order in orders:
        for c in course:
            # (A,B)와 (B,A)가 따로 만들어지지 않도록 order를 알파벳 정렬 
            order = list(order)
            order.sort()
            combs += list(combinations(order, c))
    
    # 길이 긴 순으로 정렬, 같은 길이라면 빈도가 높은 순대로 정렬 
    combs = sorted(Counter(combs).items(), reverse=True, key=lambda x: (len(x[0]), x[1]))
    
    prev_len = 0
    max_count = 0
    for comb in combs:
        menu, count = comb
        # 주문 횟수가 2보다 작은 경우, 각 길이의 가장 많이 함께 주문된 메뉴 구성이 아닌 경우
        if count < 2 or (count < max_count and len(menu) == prev_len): 
            continue
        answer.append(''.join(menu))
        max_count = count
        prev_len = len(menu)
    
    # 최종 답을 알파벳 순으로 정렬
    answer.sort()
    
    return answer