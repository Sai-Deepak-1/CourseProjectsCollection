### **1. Consumer with `forEach`**
Write a program to:
- Create a list of integers.
- Use a `Consumer` to print each integer prefixed with "Number:" using `forEach`.

---

### **2. Supplier with `Stream.generate`**
Write a program to:
- Use a `Supplier` to generate a stream of random integers between 1 and 50.
- Limit the stream to 10 elements and print them.

---

### **3. Function with `map`**
Write a program to:
- Create a list of words.
- Use a `Function` to calculate the length of each word.
- Transform the list into a list of word lengths using `map`.

---

### **4. Predicate with `filter`**
Write a program to:
- Create a list of integers.
- Use a `Predicate` to filter out odd numbers.
- Print only the even numbers from the list.

---

### **5. BiConsumer with `Map.forEach`**
Write a program to:
- Create a `Map` of products and their prices (e.g., "Apple" -> 50, "Banana" -> 30).
- Use a `BiConsumer` to print each product and its price in the format `Product: Price`.

---

### **6. BiFunction with `reduce`**
Write a program to:
- Create a list of floating-point numbers.
- Use a `BiFunction` to calculate the product of all the numbers in the list using `reduce`.

---

### **7. UnaryOperator with `map`**
Write a program to:
- Create a list of integers.
- Use a `UnaryOperator` to square each number in the list.
- Transform the list into a list of squared numbers using `map`.

---

### **8. BinaryOperator with `reduce`**
Write a program to:
- Create a list of integers.
- Use a `BinaryOperator` to find the maximum value in the list using `reduce`.

---

### **9. Parallel Stream Performance**
Write a program to:
- Create a range of numbers from 1 to 1,000,000.
- Calculate the sum using both sequential and parallel streams.
- Print the time taken for each method.

---

### **10. Parallel Stream with `forEachOrdered`**
Write a program to:
- Create a stream of integers from 1 to 10.
- Use a parallel stream to process the elements.
- Ensure that they are printed in order using `forEachOrdered`.

---

### **11. Combination of Functional Interfaces**
Write a program to:
- Create a list of strings representing names.
- Use a `Predicate` to filter out names shorter than 5 characters.
- Use a `Function` to convert the remaining names to uppercase.
- Use a `Consumer` to print each transformed name.

---

### **12. Stream Operations with Multiple Steps**
Write a program to:
- Create a list of integers.
- Filter out numbers greater than 50 using `filter`.
- Multiply the remaining numbers by 2 using `map`.
- Sort the resulting list and collect it into a new list.

---

### **13. Infinite Streams with `generate`**
Write a program to:
- Use a `Supplier` to create an infinite stream of current timestamps.
- Limit the stream to 5 elements and print them.

---

### **14. Real-World Example with `Map`**
Write a program to:
- Create a `Map` of students and their scores (e.g., "Alice" -> 85, "Bob" -> 92).
- Use a `Predicate` to filter students who scored above 90.
- Use a `Consumer` to print the names of these students.

---

### **15. Stream Pipeline with Collectors**
Write a program to:
- Create a list of strings representing names.
- Filter out names that start with "A".
- Sort the remaining names alphabetically.
- Collect the names into a comma-separated `String` and print it.