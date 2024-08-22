from node import Node
from binary_search_tree import BinarySearchTree

def find_greatest(node: Node) -> Node:
    if not node.right:
        return node
    find_greatest(node.right)

# initialize key array
keys = [18, 12, 1, 6, 14, 3]
# initialize our bst
bst = BinarySearchTree()
# insert keys into bst as nodes
for k in keys:
    bst.insert(k)

n = find_greatest(bst.root)
print(n.val)