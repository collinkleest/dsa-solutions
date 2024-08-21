from node import Node
from linked_list import LinkedList

# test print list
node_1 = Node("ckk")
node_2 = Node("collin")
node_3 = Node("kleest")
ll = LinkedList(node_1)
ll.insert(node_2)
ll.insert(node_3)
print('---- before delete ----')
ll.print_list()
ll.delete_node(node_2)
print('---- after delete ----')
ll.print_list()