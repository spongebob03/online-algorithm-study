# visited 처리를 해야할 것 같은데 중복되는 알파벳이 있는 단어의 경우 어찌할지....
import sys

score_dict = {1:0,2:0,3:1,4:1,5:2,6:3,7:5,8:11}
dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

def alphabet_search(cur, board, alphabet):
	candidates = []
	i,j = cur
	for x,y in zip(dx,dy):
		if (i+x) in range(4) and (j+y) in range(4):
			if board[i+x][j+y] == alphabet:
				candidates.append((i+x, j+y))
	return candidates

def word_search(word, board):
	k = 0
	starts = []
	for i in range(4):
		for j in range(4):
			if board[i][j] == word[k]:
				starts.append((i,j))
	while starts and k+1 < len(word):
		k += 1
		for start in starts:
			starts = alphabet_search(start, board, word[k])
	return True if k == len(word)-1 else False

def play_boggle(board):
	found = []
	count = 0
	score = 0
	for word in words:
		if word_search(word, board):
			found.append(word)
			count += 1
			score += score_dict[len(word)]
	found.sort(key=lambda x:(-len(x),x))
	return score, found[0], count

W = int(sys.stdin.readline())
words = []
for _ in range(W):
	words.append(sys.stdin.readline().strip())

sys.stdin.readline()

N = int(sys.stdin.readline())
for n in range(N):
	board = []
	for _ in range(4):
		board.append(list(sys.stdin.readline()))
	score, word, num = play_boggle(board)
	print(score, word, num)

	if n < N-1:
		sys.stdin.readline()