# Create a list
words = ["the", "quick", "brown", "fox"]
print(words)

# Accessing an item from the list
item = words[0] # O(1)
print(item)

# Traversing a list - O(n)
for word in words:
    print(word)

# Insert an item at the end of the list - O(1)
words.append("jumps")
print(words)

# Delete an item from the end of the list - O(1)
words.pop()
print(words)

# Inserting an element at position i in the list - O(n)
words.insert(3, "lazy")
print(words)