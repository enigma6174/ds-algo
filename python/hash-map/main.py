class HashMap:

    # Initialize the hash map with a size of 10^6
    def __init__(self):
        self.size = 10 ^ 6
        self.hash_table = [[] for _ in range(self.size)]

    # Method to insert a (key, value) pair in the hash map - O(1) 
    def put(self, key, value):

        # Generate the hash value from the key
        hash_value = hash(key) % self.size

        # Get the bucket from the hash value
        bucket = self.hash_table[hash_value]

        found_key = False
        for index, item in enumerate(bucket):
            item_key, item_value = item

            # Check if the key already exists
            if item_key == key:
                found_key = True
                break
        
        # If the key already exists update the value
        # Otherwise insert a new (key, value) pair into the bucket
        if found_key:
            bucket[index] = (key, value)
        else:
            bucket.append((key, value))

    # Method to return the value for the key - O(1)
    def get(self, key):

        # Generate the hash value from the key
        hash_value = hash(key) % self.size

        # Get the bucket from the hash value
        bucket = self.hash_table[hash_value]

        found_key = False
        for _, item in enumerate(bucket):
            item_key, item_record = item
            
            if item_key == key:
                found_key = True
                break

        # If the key is found return the value
        # Otherwise return null
        if found_key:
            return item_record
        else:
            return None

    # Method to delete a given key - O(1) 
    def remove(self, key):

        # Generate the hash value from the key
        hash_value = hash(key) % self.size

        # Get the bucket from the hash value
        bucket = self.hash_table[hash_value]

        found_key = False
        for index, item in enumerate(bucket):
            item_key, item_value = item

            if item_key == key:
                found_key = True
                break

        # If the key is found delete the corresponding entry
        if found_key:
            bucket.pop(index)


    # Return a string representation of the hash map
    def __str__(self):
        return "".join(str(item) for item in self.hash_table)

    