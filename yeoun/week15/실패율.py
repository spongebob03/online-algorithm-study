from collections import Counter

def solution(N, stages):
    # 사용자 명
    players = len(stages)
    failure = {}
    # 오름차순 정렬
    stages.sort()
    counter = Counter(stages)
    for stage in counter:
        # 1-N
        if stage in range(1,N+1):
            # (현재 스테이지에 멈춰있는 사용자 수) / (현재 스테이지까지 올라온 사용자 수)
            failure[stage] = counter[stage] / players
            players -= counter[stage]
    # 1-N 중 stages 값이 없으면 모두 0으로 
    for i in range(1,N+1):
        if i not in failure:
            failure[i] = 0
    # 실패율이 높고, 스테이지 번호는 낮은 순으로 정렬 
    failure = dict(sorted(failure.items(), key=lambda item: (-item[1], item[0])))
    return list(failure.keys())
