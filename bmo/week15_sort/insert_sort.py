def insert_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break
    return arr

if __name__ == '__main__':
    result = insert_sort([4,6,6,7,8,2,3,1])
    print('result: ', result)