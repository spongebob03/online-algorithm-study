def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(1, len(arr)):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]

    return arr

if __name__ == '__main__':
    result = bubble_sort([4,6,6,7,8,2,3,1])
    print('result: ', result)