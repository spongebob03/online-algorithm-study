def solution(m, n, puddles):
    # 학교가 있는 곳의 좌표가 (m,n)이므로 (열,행)
    # (행,열)로 좌표를 바꿔주기 위해 순서 바꿈 
    puddles = [(puddle[1]-1, puddle[0]-1) for puddle in puddles]
    
    town = {}
    for i in range(n):
        for j in range(m):
            # 집
            if (i,j) == (0,0):
                town[(i,j)] = 1
                
            # 물 웅덩이 
            elif (i,j) in puddles:
                town[(i,j)] = 0
                
            # 왼쪽에 길이 없는 경우
            elif j-1 < 0:
                town[(i,j)] = town[(i-1,j)]
            
            # 위쪽에 길이 없는 경우
            elif i-1 < 0:
                town[(i,j)] = town[(i,j-1)] 
            
            # 왼쪽과 위쪽 모두 길이 있는 경우 
            else:
                # 왼쪽과 위쪽의 길까지 다다르는 경우의 수를 더함 
                town[(i,j)] = town[(i,j-1)] + town[(i-1,j)]
    
    
    return town[(n-1, m-1)] % 1000000007