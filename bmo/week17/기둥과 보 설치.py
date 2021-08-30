PILLAR, PLANE = 0, 1

def pillar_valid(x, y, build):
    return y == 0 or ((x-1, y) in build[PLANE] or (x, y) in build[PLANE]) or (x, y-1) in build[PILLAR]
def plane_valid(x, y, build):
    return ((x-1, y) in build[PLANE] and (x+1, y) in build[PLANE]) or ((x, y-1) in build[PILLAR] or (x+1, y-1) in build[PILLAR])

def solution(n, build_frame):
    answer = []
    build = [[],[]] # 딕셔너를리ㄹ 쓰ㄴ 더 좋ㅡ듯 자구 중ㅛ
    
    for x, y, a, b in build_frame:
        if b == 0: 
            build[a].remove((x, y))
            for i, j in build[PILLAR]:
                if not pillar_valid(i, j, build):
                    build[a].append((x, y))
            for i, j in build[PLANE]:
                if not plane_valid(i, j, build):
                    build[a].append((x, y))
        else:
            if a == PILLAR and pillar_valid(x, y, build):
                build[a].append((x, y))
            elif a == PLANE and plane_valid(x, y, build):
                build[a].append((x, y))
                
    # print(build[PILLAR], "\n", build[PLANE], "\n")
    for a in (PILLAR, PLANE):
        for x, y in build[a]:
            answer.append([x, y, a])
    answer.sort()
    return answer

if __name__ == '__main__':
    n = 5
    build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]	
    result = solution(n, build_frame)
    print(result)