# 2배해서 k와 가까워지는 수로 가기
n, k = map(int, input().split())
history = [n]

m = k // 2
if k % 2 == 1:
    m += 1

while n != m:
    if (n-1) * 2 == m:
        n -= 1
        history.append(n)
        continue
    elif (n+1) * 2 == m:
        n += 1
        history.append(n)
        continue
    
    if abs(n - m) > abs(2*n - m):
        n = 2 * n
    else:
        if m > n:
            n += 1
        else:
            n -= 1
    history.append(n)

n *= 2
history.append(n)

if n != k and n > k:
    n -= 1
elif n != k and n < k:
    n += 1

print(len(history))
print(' '.join(map(str, history)) + " " + str(k))