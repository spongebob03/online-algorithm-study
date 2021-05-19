def solution(board, moves):
    answer = 0
    stack = []
    n = len(board)
    lines = [[] for _ in range(n)]
    
    # 0을 제외한 원소만 해당 '열' 리스트에 추가
    for i in range(n-1, -1, -1):
        for j in range(n):
            if board[i][j] != 0:
                lines[j].append(board[i][j])
    
    # 플레이
    for move in moves:
        if not lines[move-1]:
            continue
        curr = lines[move-1].pop()

        if stack and stack[-1] == curr:
            stack.pop()
            answer += 2
        else:
            stack.append(curr)

    return answer


if __name__ == '__main__':
    print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))