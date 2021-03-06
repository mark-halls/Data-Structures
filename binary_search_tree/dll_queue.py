import sys

sys.path.append("../doubly_linked_list")
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # because we need to keep track of the front and back of the queue
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_head(value)

    def dequeue(self):
        if self.size < 1:
            return
        self.size -= 1
        return self.storage.remove_from_tail()

    def len(self):
        return self.size
