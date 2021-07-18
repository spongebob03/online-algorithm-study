def binary_search(array, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == mid:
            return array[mid]
        elif array[mid] < mid:
            start = mid + 1
        else:
            end = mid -1
            
    return -1

if __name__ == '__main__':
    n = int(input())
    array = list(map(int, input().split()))

    print(binary_search(array, 0, n-1))