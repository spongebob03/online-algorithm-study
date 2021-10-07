def solution(n, weak, dist):
    answer = 0
    # 가장 멀리 갈 수 있는 친구부터 
    dist.sort(reverse=True)
    round_dist = {}
    # 원형 건물에서 각 이웃한 약한 지점 사이의 거리 
    for i in range(len(weak)):
        if i < len(weak) - 1:
            round_dist[(i,i+1)] = weak[i+1] - weak[i]
        else:
            round_dist[(i,0)] = n - (weak[i]-weak[0])
    # 거리가 짧은 순대로 정렬 
    round_dist = {k:v for k,v in sorted(round_dist.items(), key=lambda x:x[1])}
    
    # 지금까지 점검한 지점들의 튜플의 리스트 
    cover = []
    for d in dist:
        # 한 친구가 지나온 거리 
        covered = 0 
        for point in round_dist:
            if covered + round_dist[point] <= d:
                covered += round_dist[point] 
                cover.append(point)
        # 한 친구의 점검이 끝날 때마다 + 1 
        answer += 1 
        # 모든 약한 지점을 점검한 경우 
        if len(cover) + 1 == len(weak):
            break
    
    return answer