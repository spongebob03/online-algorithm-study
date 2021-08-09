def quick_sort(array, start, end):
    if start >= end:
        return 

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and array[pivot] >= array[left]:
            left += 1
        while right > start and array[pivot] <= array[right]:
            right -= 1
        
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

if __name__ == '__main__':
    arr = [4,6,6,7,8,2,3,1]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)