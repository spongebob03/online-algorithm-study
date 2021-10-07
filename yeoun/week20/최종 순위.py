# '?' 경우 모르겠어서 구현 안 했는데 통과... 
import sys
from collections import defaultdict
from itertools import combinations


def compute_ranking(prev_ranking, changed_pairs):
    '''
    prev_ranking: [5,4,3,2,1]
    changed_pairs: [[2,4, [3,4]] 인 경우
    '''
    # 5
    M = len(prev_ranking)
    # [(5,4), (5,3), (5,2), (5,1), (4,3), (4,2), ... (2,1)]
    combs = list(combinations(prev_ranking, 2))
    # ranking = {5:[4,3,2,1], 4:[3,2,1], 3:[3,1], 2:[1]}
    # 자신보다 순위가 낮은 팀 번호의 목록을 value로 갖는 dictionary
    ranking = defaultdict(list)
    for comb in combs:
        k, v = comb
        ranking[k].append(v)
    ranking[prev_ranking[-1]] = []

    # 순위가 바뀐 경우 업데이트
    for change_pair in changed_pairs:
        a, b = change_pair
        if a in ranking[b]:
            ranking[b].remove(a)
            ranking[a].append(b)
        elif b in ranking[a]:
            ranking[a].remove(b)
            ranking[b].append(a)


    # 자신보다 순위가 낮은 팀의 번호들의 개수가 업데이트 후에도 4,3,2,1,0 이라면 순위 결정 가능
    if set([len(v) for k, v in ranking.items()]) == set(list(range(0,M))):
        print(*[k for k, v in sorted(ranking.items(), key=lambda x: -len(x[1]))])
        return

    # 순위 결정 불가능
    else:
        print('IMPOSSIBLE')
        return


# 테스트 케이스 개수
N = int(sys.stdin.readline())

for _ in range(N):
    # 팀의 수
    M = int(sys.stdin.readline())
    prev_ranking = list(map(int, sys.stdin.readline().split()))

    changed_pairs = []
    changed_num = int(sys.stdin.readline())
    for _ in range(changed_num):
        changed_pairs.append(list(map(int, sys.stdin.readline().split())))

    compute_ranking(prev_ranking, changed_pairs)

