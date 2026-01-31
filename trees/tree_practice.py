class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
#Driver Code Ends
root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.right.left = Node(9)
root.right.right = Node(25)


def check_bst(root, min, max):
    if root is None:
        return True
    if min > root.data or max < root.data:
        return False

    return (check_bst(root.left,min,root.data) and check_bst(root.right,root.data,max))


print(check_bst(root,float('-inf'), float('+inf')))