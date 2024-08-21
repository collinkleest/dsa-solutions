from node import Node


class DoublyLinkedList:
    head: Node
    tail: Node
    
    def __init__(self, head=None, tail=None) -> None:
        self.head = head
        self.tail = tail

    def insert(self, node: Node) -> None:
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        return

    def print_reverse(self):
        current_node = self.tail
        while current_node.prev:
            print(current_node.data)
            current_node = current_node.prev
        if current_node.data:
            print(current_node.data)
        