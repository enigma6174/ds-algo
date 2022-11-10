# Node class for linked list
# Next pointer will be used for all the types of linked list
# Prev pointer will only be used for specialized linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# Linked list implementation
# Each node has two items - 'data' and 'next'
# Information is stored in 'data' and address of the next node is stored in 'next'
class LinkedList:

    # Initialize the linked list head pointer
    def __init__(self):
        self.head = None

    # Helper method to get the head pointer
    def get_head(self):
        return self.head

    # Helper method to check if linked list is empty
    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    # Helper method to print the linked list
    def print_list(self):
        if self.is_empty():
            return False
        
        # Create a pointer to head
        # Keep iterating over the linked list till the next of a node is None
        temp = self.head
        while temp.next is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print(temp.data, end="\n")
        return True

    # Insertion at head
    def insert_at_head(self, data):
        # Create a node
        node = Node(data)
        # Point to the head
        node.next = self.head
        # Point the head to the node that got added
        self.head = node
        # Return the linked list
        return self.head

    # Insertion at tail
    def insert_at_tail(self, data):
        # If the linked list is empty then insert at head
        if self.is_empty():
            self.insert_at_head(data)
            return self.head
        
        # If the linked list is not empty 
        # Create a new node
        node = Node(data)
        # Traverse till the end of the linked list
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        # Point the next of last node to new node
        temp.next = node
        # Return the linked list
        return self.head

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

    # Insert a node after the node that contains data
    def insert_after(self, key, data):
        # Search if the key is present in the linked list
        flag = self.search(key)
        if not flag:
            return self.head

        # Create a new node
        node = Node(data)

        # Find the position of insertion
        temp = self.head
        while temp.data is not key:
            temp = temp.next

        # Insert the node after the required node
        node.next = temp.next
        temp.next = node

        # Return the linked list
        return self.head 

    # Delete the first node 
    def delete_at_head(self):
        # Return if linked list empty
        if not self.head:
            return None

        # If only one node is present
        if self.head.next is None:
            self.head = None
            return self.head
        
        # If more than one node present
        self.head = self.head.next
        return self.head

    # Delete a node with given key
    def delete(self, key):
        # Search if the key is present in the linked list
        flag = self.search(key)
        if not flag:
            return self.head

        # When the key is in the first node
        if self.head.data is key:
            self.head = self.delete_at_head()
            return self.head

        # Find the position for deletion
        temp = self.head
        while temp.next.data is not key:
            temp = temp.next
        
        # Delete the required node
        node = temp.next
        temp.next = node.next
        node = None

        # Return the linked list
        return self.head
    

# Doubly linked list implementation
# Each node has 3 items - 'data', 'prev' and 'next'
# Information is stored in 'data'
# Address of the next node is stored in 'next' and previous node in 'prev'
class DoublyLinkedList:

    # Initialize the linked list head pointer
    def __init__(self):
        self.head = None

    # Helper method to get the head pointer
    def get_head(self):
        return self.head

    # Helper method to check if linked list is empty
    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    # Helper method to print the linked list
    def print_list(self):
        if self.is_empty():
            return False

    # Method to insert