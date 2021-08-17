def solution(food_times, k):
    n = len(food_times)
    idx = 0

    while k >= 0:
        for i in range(n):
            idx = i % n
            if food_times[idx] == 0:
                continue
            food_times[idx] -= 1

            if k == 0:
                return idx + 1
            k -= 1
            
    return -1

if __name__ == '__main__':
    food_times =  [3, 1, 2]	
    k = 5
    print(solution(food_times, k))