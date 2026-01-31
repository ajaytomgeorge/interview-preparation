class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
#Driver Code Ends
root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.right.left = Node(19)
root.right.right = Node(25)

def check_bst(root, min, max):
    if not root:
        return True
    if min> root.data or root.data > max:
        return False
    
    return check_bst(root.left, min, root.data) and check_bst(root.right, root.data, max)


# print(check_bst(root, float('-inf'), float('inf')) )

def print_inorder(root):
    if not root:
        return
    print_inorder(root.left)
    print(root.data)
    print_inorder(root.right)
def reverseTree(root):
    if not root:
        return
    reverseTree(root.left)
    reverseTree(root.right)
    root.left, root.right = root.right, root.left



print_inorder(root)
print("After reverse")
reverseTree(root)
print_inorder(root)