def fixed_point_search(array, start, end):
    while start <= end:
        mid = (start+end)//2
        # 고정값이 있으면 고정값 출력 
        if array[mid] == mid:
            return mid
        # 현재 인덱스보다 값이 큰 경우, 오른쪽으로 이동
        elif array[mid] > mid:
            end = mid - 1
        # 현재 인덱스보다 값이 작은 경우, 왼쪽으로 이동
        else:
            start = mid + 1
    
    # 고정값이 없다면 -1 출력 
    return -1
    
def solution(n, array):
    N = len(array)
    return fixed_point_search(array, start=0, end=N-1)

