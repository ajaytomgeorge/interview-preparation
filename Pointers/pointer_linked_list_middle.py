from ast import While
class Node:
    def __init__(self, data, right:"Node"=None):
        self.data = data
        self.right = right


orignal_node = start_node = Node(1)
for i in range(2,12):
    print(i)
    start_node.right = Node(i)
    start_node = start_node.right



slow = fast =orignal_node
prevous = slow
while fast and fast.right:
    print("start data", slow.data)
    slow = slow.right
    print("end data", fast.data)
    fast = fast.right.right


print("Middle value is",slow.data)
