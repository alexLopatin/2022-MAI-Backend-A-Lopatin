class Node:
    next: 'Node' = None
    prev: 'Node' = None
    value: str

    def __init__(self, value: str, prev: 'Node' = None):
        self.value = value
        self.prev = prev


class LinkedList:
    begin: 'Node' = None
    end: 'Node' = None

    def prepend(self, value: str) -> 'Node':
        if self.begin is not None:
            self.begin.prev = Node(value, self.end)
            self.begin.prev.next = self.begin

            self.begin = self.begin.prev
        else:
            self.init(value)
        return self.begin

    def remove(self, node: 'Node') -> None:
        if node == self.begin:
            self.begin = node.next
            return

        if node == self.end:
            self.end = node.prev
            self.end.next = None
            return

        node.next.prev = node.prev
        node.prev.next = node.next

    def hoist(self, node: 'Node') -> None:
        if node == self.begin:
            return

        prev_begin = self.begin
        self.begin = node
        prev_begin.prev = node

        node.prev.next = node.next
        if self.end == node:
            self.end = node.prev

        if node.next is not None:
            node.next.prev = node.prev

        node.next = prev_begin
        node.prev = None

    def init(self, value: str):
        self.begin = Node(value)
        self.end = self.begin

    def print(self):
        cur = self.begin

        while cur is not None:
            print(cur.value)
            cur = cur.next
