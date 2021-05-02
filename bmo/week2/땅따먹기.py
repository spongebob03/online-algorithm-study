def solution(land):
    for row in range(1, len(land)):
        for col, score in enumerate(land[row]):
            land[row][col] += max(land[row-1][:col] + land[row-1][col+1:])

    return max(land[-1])