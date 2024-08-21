from __future__ import annotations
from typing import Any

class Node:
    data: Any
    next: Node
    prev: Node

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None