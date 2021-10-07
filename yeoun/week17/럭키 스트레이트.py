x = input()
half = len(x) // 2
right = sum([int(num) for num in x[:half]])
left = sum([int(num) for num in x[half:]])

if right == left:
	print("LUCKY")
else:
	print("READY")