class Array:
    def __init__(self):
        self.length = 0
        self.buffer = []

    # Helper method to validate empty array
    def validate_array(self):
        if self.length == 0:
            raise Exception("cannot delete from empty array")

    # Helper method to validate incorrect index
    def validate_index(self, i):
        if i >= self.length:
            raise Exception("array index out of bounds")
        
        if i < 0:
            raise Exception("negative indexing not allowed")

    # Get the element at index i - O(1)
    def at(self, index):
        try:
            self.validate_index(index)
            return self.buffer[index]
        except Exception as e:
            print(e)

    # Insert an element at the end of the array - O(1)
    def push(self, item):
        self.buffer.append(item)
        self.length += 1
        return self.buffer

    # Remove an element from the end of the array - O(1) 
    def pop(self):
        try:
            self.validate_array()

            # Save the item and delete from array
            item = self.buffer[self.length - 1]
            del self.buffer[self.length - 1]

            # Update length of array and return popped item
            self.length -= 1
            return item
        except Exception as e:
            print(e)

    # Insert an element at index i - O(n) 
    def insert(self, item, index):
        try:
            # If the index is last index or array is empty direct insertion
            if (index == self.length or (index == 0 and self.length == 0)):
                self.buffer.append(item)
                self.length += 1
                return self.buffer

            # Validate the index for insertion
            self.validate_index(index)

            # Insert the element at the required index
            temp = self.buffer[index]
            self.buffer[index] = item

            # Shift elements to the right
            for i in range(index, self.length - 1):
                v = self.buffer[i+1]
                self.buffer[i+1] = temp
                temp = v
            
            # Add the last element to the array
            # Increment the length
            self.buffer.append(temp)
            self.length += 1

            return self.buffer
        except Exception as e:
            print(e)

    # Method to remove item from index i - O(n)
    def remove(self, index):
        try:
            # Validate the array and index
            self.validate_array()
            self.validate_index(index)

            # Shift elements left from the index
            for i in range(index, self.length-1):
                self.buffer[i] = self.buffer[i+1]

            # Delete the last entry
            del self.buffer[self.length]

            # Update the length
            self.length -= 1

            return self.buffer
        except Exception as e:
            print(e)

    # Method to return the array
    def get(self):
        return self.buffer
