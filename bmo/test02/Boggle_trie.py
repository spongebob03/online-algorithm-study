import sys
import collections

class Node(object):
	def __init__(self, char, data=None):
		self.char = char
		self.data = data
		self.children = {}
		self.found = False

class Trie(object):
	def __init__(self):
		self.head = Node(None)

	def insert(self, string):
		curr_node = self.head
		for char in string:
			if char not in curr_node.children:
				curr_node.children[char] = Node(char)
			curr_node = curr_node.children[char]
		curr_node.data = string

	def search(self, string):
		curr_node = self.head
		for char in string:
			if char not in curr_node.children:
				return False
			curr_node = curr_node.children[char]
		if (curr_node.found) or curr_node.data == None:
			return False
		else:
			curr_node.found = True
			return True

	def prefix(self, string):
		curr_node = self.head
		for char in string:
			if char not in curr_node.children:
				return False
			curr_node = curr_node.children[char]
		return True

	def initalize(self):
		queue = collections.deque(self.head.children.values())
		while queue:
			curr_node = queue.popleft()
			if curr_node.data != None:
				curr_node.found = False
			queue.extend(curr_node.children.values())

mr = [0, 0, 1, -1, 1, -1, 1, -1]
mc = [1, -1, 0, 0, 1, -1, -1, 1]
scoreDict = {1:0, 2:0, 3:1, 4:1, 5:2, 6:3, 7:5, 8:11}

W = int(sys.stdin.readline().strip())
trie = Trie()
for _ in range(W):
	trie.insert(sys.stdin.readline().strip())
sys.stdin.readline()

def dfs(row, col, word, checked, count, node):
	if (trie.search(word)):
		global total
		global score
		global maxWord
		score += scoreDict[count]
		total += 1
		if count > len(maxWord):
			maxWord = word
		elif count == len(maxWord) and word < maxWord:
			maxWord = word

	if count == 8:
		return

	for move in range(8):
		nextRow = row + mr[move]
		nextCol = col + mc[move] 
		if(0<=nextRow<=3 and 0<=nextCol<=3 and not checked[nextRow][nextCol]):
			checked[nextRow][nextCol] = True
			if (board[nextRow][nextCol] in node.children):
				dfs(nextRow, nextCol, word+board[nextRow][nextCol], checked, count+1, node.children[board[nextRow][nextCol]])
			checked[nextRow][nextCol] = False


N = int(sys.stdin.readline().strip())
for t in range(N):
	board = [sys.stdin.readline().rstrip() for _ in range(4)]
	checked = [[False for _ in range(4)] for _ in range(4)]

	total = 0
	score = 0
	maxWord = ''
	trie.initalize()
	for i in range(4):
		for j in range(4):
			if board[i][j] in trie.head.children:
				checked[i][j] = True
				dfs(i, j, board[i][j], checked, 1, trie.head.children[board[i][j]])
				checked[i][j] = False
	print(score, maxWord, total)
	if (t < N-1):
		sys.stdin.readline()