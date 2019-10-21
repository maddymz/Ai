class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def createMinimalBST(array):
    if not array:
        return None
    
    mid = len(array) //2
    root = Node(array[mid])
    root.left = createMinimalBST(array[:mid])
    root.right = createMinimalBST(array[mid+1:])
    
    return root

def preOrderTraversal(node):
    if not node:
        return
    print("root", node.val)
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)

def inOrderTraversal(node):
    if not node:
        return
    
    preOrderTraversal(node.left)
    print("root", node.val)
    preOrderTraversal(node.right)

root = createMinimalBST([1,2,3,4,5,6,7])
print ('preorder traversal')
print (preOrderTraversal(root))
print ('inorder traversal')
print (inOrderTraversal(root))