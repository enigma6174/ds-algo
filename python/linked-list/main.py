# Node class for linked list
# Next pointer will be used for all the types of linked list
# Prev pointer will only be used for specialized linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# Linked list implementation
class LinkedList:

    # Initialize the linked list head pointer
    def __init__(self):
        self.head = None

    # Helper method to check if linked list is empty
    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    # Helper method to print the linked list
    def print_list(self):
        if self.is_empty():
            return

        # Traverse over the list
        temp = self.head
        while temp.next is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print(temp.data, end="\n")

    # Search for a key in the linked list
    def search(self, key):
        temp = self.head
        while temp is not None and temp.data is not key:
            temp = temp.next
        if temp is not None:
            return True
        else:
            return False

    # Insertion at head
    def insert_at_head(self, node):
        node.next = self.head
        self.head = node

    # Insertion at tail
    def insert_at_tail(self, data):
        node = Node(data)

        if self.is_empty():
            self.insert_at_head(node)
            return self.head

        # Insertion at the end of the linked list
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = node

    # Insert a node after the node that contains data
    def insert(self, key, data):
        if not self.search(key):
            return
        # Create a new node
        node = Node(data)
        # Find the position for insertion
        temp = self.head
        while temp.data is not key:
            temp = temp.next
        # Insert the node after the required node
        node.next = temp.next
        temp.next = node

    # Delete the first node
    def delete_at_head(self):
        # Return if linked list empty
        if not self.head:
            return
        # If only one node is present
        if self.head.next is None:
            self.head = None
            return

        # If more than one node present
        self.head = self.head.next

    # Delete a node with given key
    def delete(self, key):
        if not self.search(key):
            return
        # When the key is in the first node
        if self.head.data is key:
            self.delete_at_head()
        # Find the position for deletion
        temp = self.head
        while temp.next.data is not key:
            temp = temp.next
        # Delete the required node
        node = temp.next
        temp.next = node.next
        node = None


# Doubly linked list implementation
class DoublyLinkedList:

    # Initialize the linked list head pointer
    def __init__(self):
        self.head = None
        self.tail = None

    # Helper method to check if linked list is empty
    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    # Helper method to print the linked list
    def print_list(self, mode="head"):
        if self.is_empty():
            return

        # Print the list from head
        if mode == "head":
            temp = self.head
            while temp.next is not None:
                print(temp.data, end=" -> ")
                temp = temp.next
            print(temp.data, end="\n")

        # Print the list from tail
        if mode == "tail":
            temp = self.tail
            while temp.prev is not None:
                print(temp.data, end=" -> ")
                temp = temp.prev
            print(temp.data, end="\n")

    # Helper method to insert in empty list
    def insert_empty(self, node):
        self.head = node
        self.tail = node

    # Helper method to delete when linked list has one node
    def delete_single_node(self):
        self.head = None
        self.tail = None

    # Search for a key in the linked list
    def search(self, key):
        temp = self.head
        while temp is not None and temp.data is not key:
            temp = temp.next
        # If the key is found return true else return false
        if temp is not None:
            return True
        else:
            return False

    # Insertion at head
    def insert_at_head(self, data):
        # Create new node
        node = Node(data)
        # If list is empty
        if self.is_empty():
            return self.insert_empty(node)
        # Point the prev of current node to head
        node.next = self.head
        # Adjust the head pointer
        self.head.prev = node
        self.head = node

    # Insertion at tail
    def insert_at_tail(self, data):
        # Create new node
        node = Node(data)
        # If list is empty
        if self.is_empty():
            return self.insert_empty()
        # Point the next of tail to current node
        self.tail.next = node
        # Adjust the tail pointer
        node.prev = self.tail
        self.tail = node

    # Insert data D after a node with key K
    def insert(self, key, data):
        if not self.search(key):
            return
        node = Node(data)
        # If key is in the tail
        if key == self.tail.data:
            self.insert_at_tail(data)
            return
        # Find the position for insertion
        temp = self.head
        while temp is not None and temp.data is not key:
            temp = temp.next
        # Insert the node after temp node
        node.next = temp.next
        temp.next = node
        node.next.prev = node
        node.prev = temp

    # Delete at head
    def delete_at_head(self):
        if self.head.next is None:
            self.delete_single_node()
        # Adjust the head pointer for deletion
        self.head = self.head.next
        self.head.prev = None

    # Delete at tail
    def delete_at_tail(self):
        if self.head.next is None:
            self.delete_single_node()
        # Adjust the tail pointer for deletion
        self.tail = self.tail.prev
        self.tail.next = None

    # Delete a node with key K
    def delete(self, key):
        if not self.search(key):
            return
        # If the key is in the head
        if self.head.data == key:
            self.delete_at_head()
            return
        # If the key is in the tail
        if self.tail.data == key:
            self.delete_at_tail()
            return
        # Find the deletion position
        temp = self.head
        while temp is not None and temp.data is not key:
            temp = temp.next
        # Delete the required node and adjust the pointers
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        temp.next = None
        temp.prev = None
