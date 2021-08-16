arr = '1111011'

def solution(arr):
    group = [0, 0]

    group[int(arr[0])] += 1
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            group[int(arr[i+1])] += 1
            
    return min(group)

print(solution(arr))