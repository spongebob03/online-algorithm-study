import sys

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
            
    
def makeTree(cur_node, arr):
    if cur_node[0] != '.':
        temp = TreeNode(cur_node[0])  
        root = temp
        
        cur_left_node = None
        cur_right_node = None
        
        for a in arr:
            if a[0] == cur_node[1]:
                cur_left_node = a 
            if a[0] == cur_node[2]:
                cur_right_node = a 
                
        if cur_left_node:
            root.left = makeTree(cur_left_node, arr)
        if cur_right_node:
            root.right = makeTree(cur_right_node, arr)
    else:
        root = None
        
    return root

# 입력 받아오기 
inputs = list(sys.stdin.read().split())
N = int(inputs[0])

nodes = []
for i in range(0,len(inputs[1:]),3):
    nodes.append(inputs[1:][i:i+3])

# 트리 구조로 만들기 
tree = makeTree(nodes[0], nodes)

# 전위순회
def preorder(tree, result):
    if tree:
        # 루트 
        result += tree.val
        # 왼쪽 자식, 오른쪽 자식
        children = [tree.left, tree.right]
        for child in children:
            if child:
                result = preorder(child, result)
    return result

# 중위순회
def inorder(tree, result):
    if tree:
        # 왼쪽 자식
        if tree.left:
            result = inorder(tree.left, result)
        # 루트
        result += tree.val
        # 오른쪽 자식 
        if tree.right:
            result = inorder(tree.right, result)
    return result

# 후위순회
def postorder(tree, result):
    if tree:
        # 왼쪽 자식, 오른쪽 자식 
        children = [tree.left, tree.right]
        for child in children:
            if child:
                result = postorder(child, result)
        # 루트 
        result += tree.val
    return result

print(preorder(tree, result=''))
print(inorder(tree, result=''))
print(postorder(tree, result=''))