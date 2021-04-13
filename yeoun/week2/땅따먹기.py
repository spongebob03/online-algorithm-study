def solution(land):
    N = len(land)
    # land 같은 shape의 0으로 초기화된 list 
    dp = [[0]*4 for i in range(N)]
    depth = 1

    # dp를 각 위치에서 가능한 최댓값으로 채우기 
    while depth < N:
        for idx, val in enumerate(land[depth]):
            possible_idx = [i for i in [0,1,2,3] if i != idx]
            
            max_val = 0
            for i in possible_idx:
                val = dp[depth-1][i] + land[depth-1][i]
                if max_val < val:
                    max_val = val 
            
            dp[depth][idx] = max_val

        depth += 1

    # dp의 마지막 줄의 값들을 각각 해당하는 triangle의 값과 더해 최댓값을 반환 
    return max([a+b for a,b in zip(dp[-1], land[-1])])