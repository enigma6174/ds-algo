Organize items sequentially (ie. one after other in the memory). Simplest and most widely used data structure. They have the smallest footprint because the data is stored in contiguous memory locations. If we need to store continuous data and iterate over it one by one, arrays are the best choice.

static array - fixed in size, can only add that many items as specified when creating the array. This is because arrays are contiguous memory locations and once defined we may not be able to add new item later on if the memory is not free.

dynamic array - variable in size, can add more items easily. If the array is full it will create a new array at new memory location with all the array items with more memory.

When to use?

- fast lookup
- fast push/pop
- ordered/sequential data

When to avoid?

- slow insert
- slow delete
- fixed size (depends on programming language)
