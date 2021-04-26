import heapq

def solution(A, B):
    answer = 0

    # 큰 것부터 정렬한 리스트 
    A.sort(reverse=True)

    # 큰 것부터 정렬한 힙 (MaxHeap)
    B = [-b for b in B]
    heapq.heapify(B)

    for a in A:
        if a >= -B[0]:
            continue
        else:
            heapq.heappop(B)
            answer += 1 
    
    return answer