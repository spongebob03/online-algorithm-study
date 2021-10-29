# visited 처리를 해야할 것 같은데 중복되는 알파벳이 있는 단어의 경우 어찌할지....
import sys
from collections import deque
import copy

score_dict = {1: 0, 2: 0, 3: 1, 4: 1, 5: 2, 6: 3, 7: 5, 8: 11}
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


def dfs(board, cur, visited, word):
    if not word:
        return word
    word.popleft()
    x, y = cur
    visited[x][y] = True
    #print(word, visited)

    if word:
        for pos in alphabet_search(cur, board, word[0]):
            i, j = pos
            if not visited[i][j]:
                dfs(board, pos, visited, word)
    return word


def alphabet_search(cur, board, alphabet):
    candidates = []
    i, j = cur
    for x, y in zip(dx, dy):
        if (i + x) in range(4) and (j + y) in range(4):
            if board[i + x][j + y] == alphabet:
                candidates.append((i + x, j + y))
    return candidates


def word_search(word, board):
    q_word = deque(list(word))
    starts = []
    for i in range(4):
        for j in range(4):
            if board[i][j] == word[0]:
                starts.append((i, j))

    for start in starts:
        original_word = copy.deepcopy(q_word)
        visited = [[False] * 4 for _ in range(4)]
        output = dfs(board, start, visited, original_word)
        print(output)
        if not output:
            return True

    return False


def play_boggle(board):
    found = []
    count = 0
    score = 0
    for word in words:
        if word_search(word, board):
            found.append(word)
            count += 1
            score += score_dict[len(word)]
    found.sort(key=lambda x: (-len(x), x))
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

    if n < N - 1:
        sys.stdin.readline()