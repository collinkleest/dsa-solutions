from node import Node

class LinkedList:
    head: Node

    def __init__(self, node):
        self.head = node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
        return

    def insert(self, node: Node) -> None:
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = node
        return
    
    def get_last(self):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        return current_node
    
    def delete_node(self, node: Node):
        node.data = node.next.data
        node.next = node.next.next
    
    def reverse(self):
        current_node = self.head
        prev = None

        while current_node:
            next = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = next
        
        self.head = prev
    