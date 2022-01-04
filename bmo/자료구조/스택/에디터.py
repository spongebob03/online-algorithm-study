f = open('input.txt', 'r')

arr = [s for s in f.readline()[:-1]]
n = len(arr)
cursor = n

m = int(f.readline())

for _ in range(m):
    cmd = f.readline()
    if cmd[0] == 'L' and cursor > 0:
        cursor -= 1
    elif cmd[0] == 'D' and cursor < n:
        cursor += 1
    elif cmd[0] == 'B':
        if cursor > 0 and n > 0:
            arr.pop(cursor-1)
            cursor -= 1
            n -= 1
    elif cmd[0] == 'P':
        c = cmd.split()[1]
        arr.insert(cursor, c)
        cursor += 1
        n += 1

print(''.join(arr))