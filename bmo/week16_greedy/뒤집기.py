arr = '1111011'

def solution(arr):
    group = [0, 0]

    for i in range(1, len(arr)):
        if arr[i-1] != arr[i]:
            group[int(arr[i-1])] += 1
            
            if i == len(arr) - 1:
                group[int(arr[i])] += 1

    return min(group)

print(solution(arr))