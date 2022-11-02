// Create an array
const numbers = [234, 2411, 987, 785, 34, 452];
console.log(numbers);

// Accessing the array item - O(1)
const item = numbers[0];
console.log(item);

// Traversing the array - O(n)
for (const number of numbers) {
  console.log(number);
}

// Add item to end of array - O(1)
numbers.push(0);
console.log(numbers);

// Remove an item from the end of array - O(1)
numbers.pop();
console.log(numbers);

// Insert an item at the beginning of the array - O(n)
numbers.unshift(0);
console.log(numbers);

// Insert an item at position i in the array - O(n)
let i = 3;
numbers.splice(i, 0, -999);
console.log(numbers);


