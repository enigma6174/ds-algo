// Array implementation
class ArrayImplementation {
  // When array is created initialize with two properties (length and buffer)
  constructor() {
    this.length = 0; // keep a track of the length of the array
    this.buffer = []; // hold the data
  }

  validateArray() {
    if (this.length === 0) throw Error("cannot delete from empty array");
  }

  validateIndex(i) {
    if (i >= this.length) throw Error("array index out of bounds");
    if (i < 0) throw Error("negative index not allowed");
  }

  // Method to return the data at index i
  at(index) {
    try {
      this.validateIndex(index);
      return this.buffer[index];
    } catch (e) {
      console.error(e);
    }
  }

  // Method to insert item into the array
  push(item) {
    this.buffer[this.length] = item; // insert item at current empty index
    this.length += 1; // increment length
    return this.buffer;
  }

  // Method to remove item from the array
  pop() {
    try {
      this.validateArray();
      const item = this.buffer[this.length - 1]; // save the last item
      delete this.buffer[this.length - 1]; // remove the last item
      this.length -= 1; // decrement the current length
      return item;
    } catch (e) {
      console.error(e);
    }
  }

  // Method to insert item at index i in the array
  insert(item, index) {
    try {
      // Insert into the array if array empty or after last index
      if (index === this.length || (index == 0 && this.length === 0)) {
        this.buffer[index] = item;
        this.length += 1;
        return this.buffer;
      }
      // Validate the index
      this.validateIndex(index);

      // Insert the element at required index
      let temp = this.buffer[index];
      this.buffer[index] = item;

      // Shift every element one index to the right
      // Start from the index where element is inserted
      for (let i = index; i < this.length - 1; i++) {
        let v = this.buffer[i + 1];
        this.buffer[i + 1] = temp;
        temp = v;
      }

      // Add last element to the array and increase length
      buffer[this.length] = temp;
      this.length += 1;

      return this.buffer;
    } catch (e) {
      console.error(e);
    }
  }

  // Method to delete item at index i in the array
  remove(index) {
    try {
      // Validate the index
      this.validateIndex(index);
      this.validateArray();

      // Shift every element one index to the left
      // Start from the index where element is deleted
      for (let i = index; i < this.length - 1; i++) this.buffer[i] = this.buffer[i + 1];

      // Delete the duplicate at the end and update length
      delete this.buffer[this.length - 1];
      this.length -= 1;

      return this.buffer;
    } catch (e) {
      console.error(e);
    }
  }

  // Method to return the array
  get() {
    return this.buffer;
  }
}
