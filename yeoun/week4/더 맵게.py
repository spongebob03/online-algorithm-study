import heapq

def solution(scoville, K):
    # 섞은 횟수
    answer = 0
    
    # 오름차순 정렬됨 
    heapq.heapify(scoville)
    
    # 최솟값이 K보다 작으면 반복 
    while scoville[0] < K:
        # 섞을 수 없으면 -1 반환 
        if len(scoville) < 2:
            return -1 
        # 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
        new_scoville = heapq.heappop(scoville) + heapq.heappop(scoville) * 2    
        # 새로운 스코빌 지수를 삽입함 
        heapq.heappush(scoville, new_scoville)
        answer += 1 
    
    return answer