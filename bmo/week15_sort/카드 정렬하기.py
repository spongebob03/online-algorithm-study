import heapq

f = open('bmo/week15_sort/input3.txt')
n = int(f.readline())

# two way optimal merge pattern
nums = []
for _ in range(n):
    nums.append(int(f.readline()))

heapq.heapify(nums)
history = 0

while nums:
    min1 = heapq.heappop(nums)
    if not nums:
        break
    min2 = heapq.heappop(nums)
    heapq.heappush(nums, min1+min2)
    history += min1 + min2

print(history)