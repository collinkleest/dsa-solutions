from node import Node
from doubly_linked_list import DoublyLinkedList

# test print list
node_1 = Node("ckk")
node_2 = Node("collin")
node_3 = Node("kleest")
ll = DoublyLinkedList()
ll.insert(node_1)
ll.insert(node_2)
ll.insert(node_3)
ll.print_reverse()