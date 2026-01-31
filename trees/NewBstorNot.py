# Helper function to check if a tree is
# BST within a given range
def isBstUtil(node, min_val, max_val):
    if node is None:
        return True

    # If the current node's data 
    # is not in the valid range, return false
    if node.data < min_val or node.data > max_val:
        return False

    # Recursively check the left and 
    # right subtrees with updated ranges
    return (isBstUtil(node.left, min_val, node.data - 1) and
            isBstUtil(node.right, node.data + 1, max_val))
            
# Function to check if the entire binary tree is a BST
def isBST(root):
    return isBstUtil(root, float('-inf'), float('inf'))