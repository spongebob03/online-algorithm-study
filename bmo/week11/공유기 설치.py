n, c = 5, 3
array = [1, 2, 8, 4, 9]
array.sort()

start = array[1] - array[0]
end = array[-1] - array[0]
result = 0

while start <= end:
    gap = (start + end) // 2
    location = array[0]
    count = 1

    for i in range(1, n):
        if location + gap <= array[i]:
            location = array[i]
            count += 1
        
    if count >= c:
        start = gap + 1
        result = gap
    else:
        end = gap - 1

print(result)