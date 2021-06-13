class Node:

    def __init__(self, item, left, right):
        self.data = item
        self.left = left
        self.right = right

    # 전위 순회
    def preorder(self):
        traversal = []
        traversal.append(self.data)
        if self.left:
            traversal += self.left.preorder()
        if self.right:
            traversal += self.right.preorder()
        return traversal

    # 중위 순회
    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self.data)
        if self.right:
            traversal += self.right.inorder()
        return traversal
    
    # 후위 순회
    def postorder(self):
        traversal = []
        if self.left:
            traversal += self.left.postorder()
        if self.right:
            traversal += self.right.postorder()
        traversal.append(self.data)
        return traversal

class BinaryTree:

    def __init__(self, r):
        self.root = r
    
    def preorder(self):
        if self.root:
            return self.root.preorder()
        else:
            return []

    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []

    def postorder(self):
        if self.root:
            return self.root.postorder()
        else:
            return []

def solution():
    n= int(input())
    tree = {}

    for _ in range(n):
        node, left, right = input().split()
        if left == '.':
            left = None
        if right == '.':
            right = None
        tree[node] = Node(node, left, right)
    
    btree = BinaryTree(tree['A'])
    print(btree.inorder())

solution()