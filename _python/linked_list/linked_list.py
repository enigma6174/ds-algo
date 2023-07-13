from node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def get_head(self):
        return self.head

    def get_length(self):
        return self.length

    def is_empty(self):
        if self.head is None:
            return True
        return False

    def insert_at_head(self, data):
        node = Node(data)

        # If list is empty adjust the head to node
        if self.is_empty():
            self.head = node
            self.length += 1
            return self.head

        # If list is non-empty point the node to head of the list and adjust head node
        node.next = self.head
        self.head = node
        self.length += 1

        return self.head

    def insert_at_tail(self, data):
        node = Node(data)

        # If list is empty adjust head to node
        if self.is_empty():
            self.head = node
            self.length += 1
            return self.head

        # If list is non-empty traverse to end of list and add node
        # Use another pointer to traverse till end of lise
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = node
        self.length += 1

        return self.head

    def insert_at_k(self, data, k):
        node = Node(data)

        # If k is more than length of linked list perform insert_at_tail()
        if k > self.length:
            self.head = self.insert_at_tail(data)

        # If k is 0 then perform insert_at_head()
        elif k == 0:
            self.head = self.insert_at_head(data)

        else:
            # For all other cases, traverse till index k-1
            index = 0
            temp = self.head
            while index < k-1:
                temp = temp.next
                index += 1

            # Point to the node at index k
            # Adjust the next of node at index k-1 to inserted node
            node.next = temp.next
            temp.next = node
            self.length += 1

        return self.head

    def search(self, key):
        if self.is_empty():
            return False
        temp = self.head
        while temp is not None:
            if temp.data == key:
                return True
            temp = temp.next
        return False

    def delete_at_head(self):
        if self.head.next is None:
            self.head = None
            self.length -= 1
            return self.head

        temp = self.head
        self.head = self.head.next
        temp.next = None

        del temp
        self.length -= 1

        return self.head

    def delete_at_tail(self, mode=1):
        if self.head.next is None:
            self.head = self.delete_at_head()
            return self.head

        # Use tail pointer to traverse to end of list
        # Use second pointer to traverse to second last node
        # Delete last node
        if mode == 1:

            # Traverse to last node of  list
            tail = self.head
            while tail.next is not None:
                tail = tail.next

            # Traverse to second last node of list
            # Break link between second last and last node of list
            temp = self.head
            while temp.next != tail:
                temp = temp.next
            temp.next = None

            # Delete last node
            del tail
            self.length -= 1

            return self.head

        # Use pointer to check if next node does not point to null
        # If next node does not point to null keep traversing
        # Delete last node when reached second last node
        if mode == 2:

            # Traverse to second last node of list
            temp = self.head
            while temp.next.next is not None:
                temp = temp.next

            # Delete last node from second last node
            temp.next = None
            self.length -= 1

            return self.head

    def delete_by_key(self, key):
        # Search if the key is present in the list
        if not self.search(key):
            return

        if self.head.data == key:
            self.head = self.delete_at_head()
            return self.head

        # Use current pointer to traverse till next node data does not equal key
        temp = self.head
        while temp.next.data != key:
            temp = temp.next

        # When the current pointer stops next node is node_to_delete
        node_to_delete = temp.next

        # Point current pointer to the next node of node_to_delete
        temp.next = node_to_delete.next
        node_to_delete.next = None

        # Delete the required node
        del node_to_delete
        self.length -= 1

        return self.head
