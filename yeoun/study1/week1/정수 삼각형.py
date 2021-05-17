def solution(triangle):
    N = len(triangle)
    # triangle과 같은 shape의 0으로 초기화된 list 
    dp = [[0]*i for i in range(1,N+1)]
    depth = 1
    
    # dp를 각 위치에서 가능한 최댓값으로 채우기 
    while depth < len(triangle):
        for idx, val in enumerate(triangle[depth]):
            # idx == 0인 경우, 윗 줄의 0번째 값만 접근 가능 
            if idx == 0:
                dp[depth][idx] = dp[depth-1][idx] + triangle[depth-1][idx]
            # idx == depth인 경우(해당 줄의 마지막 값인 경우), 윗 줄의 마지막 값만 접근 가능 
            elif idx == depth:
                dp[depth][idx] = dp[depth-1][idx-1] + triangle[depth-1][idx-1]
            # 0 < idx and idx < depth인 경우, 윗 줄에서 자신과 index가 같은 값과 자신보다 index가 1만큼 작은 값에 접근 가능 
            else: 
                dp[depth][idx] = max(dp[depth-1][idx] + triangle[depth-1][idx], dp[depth-1][idx-1] + triangle[depth-1][idx-1])

        depth += 1
    
    # dp의 마지막 줄의 값들을 각각 해당하는 triangle의 값과 더해 최댓값을 반환 
    return max([a+b for a,b in zip(dp[-1], triangle[-1])])
    