def binary_search1(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target and (mid == 0 or array[mid-1] < target):
            return mid
        elif array[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1
    return None

def binary_search2(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target and (mid == len(array) - 1 or array[mid+1] > target):
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

if __name__ == '__main__':
    n, x = map(int, input().split())
    array = list(map(int, input().split()))
    
    start = binary_search1(array, x, 0, n-1)
    end = binary_search2(array, x, 0, n-1)

    print(end - start + 1) if (start, end) != (None, None) else print(-1)