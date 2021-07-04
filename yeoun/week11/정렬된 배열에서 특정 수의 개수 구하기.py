# 이진 탐색 소스코드 구현(재귀 함수)
def binary_search(array, target, start, end, result):
    if start > end:
        # x인 원소가 하나도 없다면 -1 출력 
        return len(result) if len(result) > 0 else -1 
    
    mid = (start + end) // 2 
    
    # 중간값이 타겟인 경우 
    if array[mid] == target:
        # 현재 인덱스를 result 집합에 추가 
        result.add(mid)
        # 현재 인덱스보다 작은 쪽, 큰 쪽 모두 가보기 
        binary_search(array, target, start, mid - 1, result)
        binary_search(array, target, mid + 1, end, result)
        
    # 중간값이 타겟보다 큰 경우 
    elif array[mid] > target:
        binary_search(array, target, start, mid - 1, result)
        
    # 중간값이 타겟보다 작은 경우 
    else:
        binary_search(array, target, mid + 1, end, result)
        
    # x인 원소가 하나도 없다면 -1 출력 
    return len(result) if len(result) > 0 else -1 

def solution(N, x, array):
    return binary_search(array, x, 0, N-1, result=set())
    