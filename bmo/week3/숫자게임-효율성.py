import heapq

def solution(A, B):
    answer = 0
    if min(A) > max(B):
        return 0

    # 내림차순
    A.sort(reverse = True)
    
    # MaxHeap
    B = [-x for x in B]
    heapq.heapify(B)

    for a in A:
        if a >= B[0] * (-1):
            continue
        else:
            heapq.heappop(B)
            answer += 1
    return answer