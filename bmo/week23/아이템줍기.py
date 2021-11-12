def print_graph(graph):
    for row in graph:
        print(row)

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    graph = [[0] * 21 for _ in range(21)] # 일단 예시 10 * 10 2배 배경
    for x1, y1, x2, y2 in rectangle:
        graph[y1*2][x1*2:(x2+1)*2] = [1] * ((x2+1 - x1)*2)
        graph[y2*2][x1*2:(x2+1)*2] = [1] * ((x2+1 - x1)*2)
        for i in range(y1*2+1, y2*2):
            graph[i][x1*2] = 1
            graph[i][x2*2] = 1
    # 2배
    # BFS
    print_graph(graph)
    return answer

if __name__ == '__main__':
    rectangle = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
    solution(rectangle, 1, 3, 7, 8)