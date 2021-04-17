def rotation(key):
    m = len(key)
    rotate_key = [[0] * len(key[0]) for _ in range(len(key))]
    for row in range(m):
        for i in range(m):
            rotate_key[i][m-1 - row] = key[row][i]
    return rotate_key

def check(bigLock):
    n = len(bigLock) // 3
    for i in range(n, n * 2):
        for j in range(n, n * 2):
            if bigLock[i][j] != 1:
                return False
    return True
    
def solution(key, lock):
    n = len(lock)
    m = len(key)
    #자물쇠를 가운데 배치
    bigLock = [[0] * 3 * n for _ in range(3 * n)]
    for i in range(n):
        bigLock[n + i][n : 2 * n] = lock[i]
    
    for angle in range(4):
        key = rotation(key)
        for row in range(n * 2):
            for col in range(n * 2):

                for i in range(m):
                    for j in range(m):
                        bigLock[row+i][col+j] += key[i][j]

                if check(bigLock):
                    return True
                
                for i in range(m):
                    for j in range(m):
                        bigLock[row+i][col+j] -= key[i][j]
    
    return False