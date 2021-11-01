import sys

def fill_square(square, board, answer):
	x,y = square
	# 사각형의 범위 
	for i in range(x, x+10):
		for j in range(y, y+10):
			# 처음 칠하는 부분이면 +1 
			if board[i][j] == 0:
				answer += 1
			board[i][j] = 1
	return board, answer

N = int(sys.stdin.readline())
squares = []
for _ in range(N):
	squares.append(list(map(int, sys.stdin.readline().split())))

answer = 0
# 빈 도화지 
board = [[0] * 101 for _ in range(101)]
for square in squares:
	board, answer = fill_square(square, board, answer)

print(answer)
