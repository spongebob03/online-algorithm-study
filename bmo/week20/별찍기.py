def draw_star(n) :
    if n == 3 :
        paper[0][:3] = [1] * 3
        paper[1][:3] = [1, 0, 1]
        paper[2][:3] = [1] * 3
        return

    a = n//3
    draw_star(a)

    for i in range(3) :
        for j in range(3) :
            if i == 1 and j == 1 :
                continue
            for k in range(a):
                paper[a * i + k][a * j:a * (j+1)] = paper[k][:a] # 핵심

def print_star(paper):
    for i in paper :
        #print(''.join(i))
        for j in i :
            print('*', end='') if j else print(' ', end='')
        print()

if __name__ == '__main__':
    N = int(input())      

    # 별을 찍을 도화지
    # 0, 1: 별을 찍을 여부
    paper = [[0 for i in range(N)] for i in range(N)]
    
    draw_star(N) 

    print_star(paper) 