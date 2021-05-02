import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville:
        min1 = heapq.heappop(scoville)
        if min1 >= K:
            return answer

        if not scoville:
            return -1
        
        min2 = heapq.heappop(scoville)

        heapq.heappush(scoville, min1 + min2 * 2)
        answer += 1 