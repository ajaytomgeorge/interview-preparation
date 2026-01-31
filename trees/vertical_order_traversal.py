from collections import defaultdict, deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def verticalTraversal(root):
    if not root:
        return []

    # x -> list of (y, val)
    node_map = defaultdict(list)

    # Queue: (node, x, y)
    queue = deque([(root, 0, 0)])

    while queue:
        node, x, y = queue.popleft()
        node_map[x].append((y, node.val))

        if node.left:
            queue.append((node.left, x-1, y+1))
        if node.right:
            queue.append((node.right, x+1, y+1))

    # Sort by x, then by y, then value
    result = []
    for x in sorted(node_map.keys()):
        # sort by y, then val
        col = sorted(node_map[x], key=lambda p: (p[0], p[1]))
        result.append([val for y, val in col])

    return result
