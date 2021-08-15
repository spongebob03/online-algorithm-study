def select_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

if __name__ == '__main__':
    result = select_sort([4,6,6,7,8,2,3,1])
    print('result: ', result)