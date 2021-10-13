import itertools

def get_point(line1, line2):
    a, b, e = line1
    c, d, f = line2
    if a * d - b * c == 0:
        return None
    x = (b * f - e * d) / (a * d - b * c)
    y = (e * c - a * f) / (a * d - b * c)

    if x - int(x) != 0 or y - int(y) != 0:
        return None
    return (int(x), int(y))

def draw_star(star_pos):
    # x, y 분리해내기, 각 끝 알아내기
    mrow = max(pos[0] for pos in star_pos)
    mcol = min(pos[1] for pos in star_pos)

    trans_pos = []
    for x, y in star_pos:
        row = (y - mrow) * (-1)
        col = (x - mcol)
        trans_pos.append((row, col))
    
    m = max(pos[1] for pos in trans_pos)
    n = max(pos[0] for pos in trans_pos)
    graph = [["."] * (m+1) for _ in range(n+1)]

    for r, c in trans_pos:
        graph[r][c] = "*"
    return graph

def solution(line):
    answer = []
    n = len(line)
    star_pos = []
    for l1, l2 in itertools.combinations([i for i in range(n)], 2):
        star_point = get_point(line[l1], line[l2])
        if star_point:
            star_pos.append(star_point)
    
    for stars in draw_star(star_pos):
        answer.append(''.join(stars))
    return answer

if __name__ == '__main__':
    line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]	
    solution(line)