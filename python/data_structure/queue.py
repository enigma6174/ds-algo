from linkedlist import LinkedList


# Queue implementation using singly linked list
class Queue:
    # Initialize the queue
    def __init__(self):
        self.queue = LinkedList()
        self.length = 0

    # Method to check if the queue is empty
    def is_empty(self):
        return self.length == 0

    # Meth
