from python.data_structure.array import Array
from python.data_structure.linkedlist import LinkedList


# Stack implementation using array
class ArrayStack:
    # Initialize the stack
    def __init__(self):
        self.stack = Array()
        self.length = 0

    # Method to check if stack is empty
    def is_empty(self):
        return self.length == 0

    # Method to push an element into the stack
    def push(self, data):
        self.stack.push(data)
        self.length += 1

    # Method to pop an element from the stack
    def pop(self):
        if self.is_empty():
            return None
        self.length -= 1
        return self.stack.pop()

    # Method to return the size of the stack
    def size(self):
        return self.length

    # Method to return the topmost element of the stack
    def peek(self):
        if self.is_empty():
            return None
        return self.stack.at(self.length - 1)


# Stack implementation using linked list
# Insert at head to keep O(1) time for stack operations
class LinkedStack:
    # Initialize the pointers and size
    def __init__(self):
        self.stack = LinkedList()
        self.length = 0

    # Method to check if stack is empty
    def is_empty(self):
        return self.stack.is_empty()

    # Method to push element into the stack
    def push(self, data):
        self.stack.insert_at_head(data)
        self.length += 1

    # Method to pop element from stack
    def pop(self):
        if self.is_empty():
            return None
        self.length -= 1
        return self.stack.delete_at_head()

    # Method to return the size of the stack
    def size(self):
        return self.length

    # Method to return the topmost element of the stack
    def peek(self):
        if self.is_empty():
            return None
        return self.stack.get_head_data()
