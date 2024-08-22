from typing import Any
from node import Node

class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, key: Any):
        """Inserts a new node with the given key into the BST."""
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root: Node, key: Any):
        """Helper method to insert a new node with the given key."""
        if key < root.val:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)