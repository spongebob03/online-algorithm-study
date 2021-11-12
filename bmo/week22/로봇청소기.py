def print_graph(graph):
    for row in graph:
        print(row)
if __name__ == '__main__':
    f = open('input.txt', 'r')

    n, m = map(int, f.readline().split())
    graph = []

    #d - 0:북(-1, 0), 1:동(0, 1), 2:남(1, 0), 3:서(-1, 0)
    x, y, d = map(int, f.readline().split())

    for _ in range(n):
        graph.append(list(map(int, f.readline().split())))
    
    