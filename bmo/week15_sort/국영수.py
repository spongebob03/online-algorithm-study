if __name__ == '__main__':
    f = open('bmo/week15_sort/input1.txt')
    n = int(f.readline())
    info = []
    for i in range(n):
        name, k, m, e = f.readline().split()
        k, m, e = map(int, [k, m, e])
        info.append((k, m, e, name))

    info.sort(key=lambda x: (-x[0], x[1], -x[2], x[3]))

    for s in info:
        print(s[3])