def solution(dirs):
    position = [(0, 0)]
    path = set()
    direction = {
        'U': (0, 1),
        'D': (0, -1),
        'L': (-1, 0),
        'R': (1, 0)
    }
    for dir in dirs:
        x, y = position[-1]
        dx, dy = direction[dir]
        next_x = x + dx
        next_y = y + dy

        if -5 <= next_x <= 5 and -5 <= next_y <= 5:
            position.append((next_x, next_y))
            path.add(((x, y), (next_x, next_y)))
            path.add(((next_x, next_y), (x, y)))
            
    return len(path) // 2

if __name__ == '__main__':
    result = solution("ULURRDLLU")
    print(result)