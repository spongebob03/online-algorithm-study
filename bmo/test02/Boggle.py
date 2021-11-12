def check(board, dic):
    SCORE = {1:0, 2:0, 3:1, 4:1, 5:2, 6:3, 7:5, 8:11}
    match = set()
    score = 0

    # 부분 그래프로 만들 수 있는 단어 매칭 (부분 그래프가 아니다)
    for r in range(2):
        for c in range(2):
            sub = set()
            for i in range(3):
                sub |= set(board[r+i][c:c+3])
            # 단어 매칭
            for key, value in dic.items():
                if value & sub == value:
                    match.add(key)

    # 점수 카운트
    max_word = ""
    max_length = 0
    print(match)
    for word in match:
        length = len(word)
        score += SCORE[length]
        if length > max_length:
            max_word = word
            max_length = length

    print(score, max_word, len(match))

if __name__ == '__main__':
    f = open('bmo/test02/input.txt', 'r')

    w = int(f.readline())
    dic = {}
    for _ in range(w):
        word = f.readline()[:-1]
        dic[word] = set(word)

    f.readline()
    b = int(f.readline())

    for _ in range(b):
        board = []
        for i in range(4):
            board.append(f.readline()[:-1])
        f.readline()
        check(board, dic)