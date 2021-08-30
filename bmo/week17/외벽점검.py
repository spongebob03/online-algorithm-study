def reverse_gap(n, pos1, pos2):
    return min(pos1, pos2) + (n - max(pos1, pos2))

def solution(n, weak, dist):
    answer = 0
    m = len(weak)
    gaps = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            gap1 = abs(weak[i] - weak[j])
            gap2 = reverse_gap(n, weak[i], weak[j])
            # print(f'각 취약지점 {weak[i]} 에서 {weak[j]} 거리: {gap1}, {gap2}')
            gaps[i][j] = min(gap1, gap2)
    for i in range(m):
        print(gaps[i])
    
    return answer

if __name__ == '__main__':
    n = 12
    weak = [1, 5, 6, 10]
    dist = [1, 2, 3, 4]
    solution(n, weak, dist)