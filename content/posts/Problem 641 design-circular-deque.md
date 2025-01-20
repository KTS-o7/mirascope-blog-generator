+++
title = 'Problem 641 Design Circular Deque'
date = 2025-01-20T22:09:47+05:30
draft = false
series = 'leetcode'
tags = ['array', 'linked list', 'design', 'queue']
toc = false
math = false
+++

# Problem Statement

**Link** - [Problem 641](https://leetcode.com/problems/design-circular-deque/?envType=daily-question&envId=2024-09-28)

## Question

<p>Design your implementation of the circular double-ended queue (deque).</p>

<p>Implement the <code>MyCircularDeque</code> class:</p>

<ul>
	<li><code>MyCircularDeque(int k)</code> Initializes the deque with a maximum size of <code>k</code>.</li>
	<li><code>boolean insertFront()</code> Adds an item at the front of Deque. Returns <code>true</code> if the operation is successful, or <code>false</code> otherwise.</li>
	<li><code>boolean insertLast()</code> Adds an item at the rear of Deque. Returns <code>true</code> if the operation is successful, or <code>false</code> otherwise.</li>
	<li><code>boolean deleteFront()</code> Deletes an item from the front of Deque. Returns <code>true</code> if the operation is successful, or <code>false</code> otherwise.</li>
	<li><code>boolean deleteLast()</code> Deletes an item from the rear of Deque. Returns <code>true</code> if the operation is successful, or <code>false</code> otherwise.</li>
	<li><code>int getFront()</code> Returns the front item from the Deque. Returns <code>-1</code> if the deque is empty.</li>
	<li><code>int getRear()</code> Returns the last item from Deque. Returns <code>-1</code> if the deque is empty.</li>
	<li><code>boolean isEmpty()</code> Returns <code>true</code> if the deque is empty, or <code>false</code> otherwise.</li>
	<li><code>boolean isFull()</code> Returns <code>true</code> if the deque is full, or <code>false</code> otherwise.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;MyCircularDeque&quot;, &quot;insertLast&quot;, &quot;insertLast&quot;, &quot;insertFront&quot;, &quot;insertFront&quot;, &quot;getRear&quot;, &quot;isFull&quot;, &quot;deleteLast&quot;, &quot;insertFront&quot;, &quot;getFront&quot;]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
<strong>Output</strong>
[null, true, true, true, false, 2, true, true, true, 4]

<strong>Explanation</strong>
MyCircularDeque myCircularDeque = new MyCircularDeque(3);
myCircularDeque.insertLast(1);  // return True
myCircularDeque.insertLast(2);  // return True
myCircularDeque.insertFront(3); // return True
myCircularDeque.insertFront(4); // return False, the queue is full.
myCircularDeque.getRear();      // return 2
myCircularDeque.isFull();       // return True
myCircularDeque.deleteLast();   // return True
myCircularDeque.insertFront(4); // return True
myCircularDeque.getFront();     // return 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= 1000</code></li>
	<li><code>0 &lt;= value &lt;= 1000</code></li>
	<li>At most <code>2000</code> calls will be made to <code>insertFront</code>, <code>insertLast</code>, <code>deleteFront</code>, <code>deleteLast</code>, <code>getFront</code>, <code>getRear</code>, <code>isEmpty</code>, <code>isFull</code>.</li>
</ul>


## Solution

```cpp
class MyCircularDeque {
private:
    vector<int>arr;
    int front;
    int rear;
    int capacity;
    int size;

public:
    MyCircularDeque(int k) {
        capacity = k;
        arr.resize(capacity);
        front = 0;
        rear = 0;
        size = 0;
    }
    
    bool insertFront(int value) {
        if (isFull()) 
            return false;
        front = (front - 1 + capacity) % capacity;
        arr[front] = value;
        size++;
        return true;
    }
    
    bool insertLast(int value) {
        if (isFull()) 
            return false;
        arr[rear] = value;
        rear = (rear + 1) % capacity;
        size++;
        return true;
    }
    
    bool deleteFront() {
        if (isEmpty()) 
            return false;
        front = (front + 1) % capacity;
        size--;
        return true;
    }
    
    bool deleteLast() {
        if (isEmpty()) 
            return false;
        rear = (rear - 1 + capacity) % capacity;
        size--;
        return true;
    }
    
    int getFront() {
        if (isEmpty()) 
            return -1;
        return arr[front];
    }
    
    int getRear() {
        if (isEmpty()) 
            return -1;
        return arr[(rear - 1 + capacity) % capacity];
    }
    
    bool isEmpty() {
        return size == 0;
    }
    
    bool isFull() {
        return size == capacity;
    }

};

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * MyCircularDeque* obj = new MyCircularDeque(k);
 * bool param_1 = obj->insertFront(value);
 * bool param_2 = obj->insertLast(value);
 * bool param_3 = obj->deleteFront();
 * bool param_4 = obj->deleteLast();
 * int param_5 = obj->getFront();
 * int param_6 = obj->getRear();
 * bool param_7 = obj->isEmpty();
 * bool param_8 = obj->isFull();
 */

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * MyCircularDeque* obj = new MyCircularDeque(k);
 * bool param_1 = obj->insertFront(value);
 * bool param_2 = obj->insertLast(value);
 * bool param_3 = obj->deleteFront();
 * bool param_4 = obj->deleteLast();
 * int param_5 = obj->getFront();
 * int param_6 = obj->getRear();
 * bool param_7 = obj->isEmpty();
 * bool param_8 = obj->isFull();
 */
```

## Complexity Analysis

```markdown
| Algorithm | Time Complexity | Space Complexity |
| --------- | --------------- | ---------------- |
| Circular Array Implementation  | O(1)           | O(k)             |
```

## Explanation

#### Intial Thoughts

To approach this problem, consider a circular buffer where elements can be added or removed from both ends. Think of it as a merry-go-round where you can get on or off at either end. Start by initializing the deque with a maximum size, and keep track of the front and rear pointers. Consider how to handle cases where the deque is full or empty. Think about how to update the front and rear pointers when elements are added or removed.


#### Intuitive Analysis

Intuitively, solving this problem involves understanding how a circular deque works. Imagine a ring where you can insert or delete elements at any point. To insert an element at the front, move the front pointer backwards and add the element. To insert at the rear, move the rear pointer forwards and add the element. When deleting, move the corresponding pointer in the opposite direction. Keep track of the size of the deque to handle full or empty cases. Visualize the process like a circular train where cars can be added or removed at either end, and the train can wrap around itself.


### 1. Intuition

- To implement a circular double-ended queue, we need to consider the properties of a deque and how to efficiently add and remove elements from both ends.
- We should use a circular array to store the elements, which allows us to reuse the space when an element is removed from the front or rear.
- The `front` and `rear` pointers are used to keep track of the current front and rear of the deque, and they are updated accordingly when elements are added or removed.
- The `size` variable keeps track of the current number of elements in the deque, which helps us to determine whether the deque is empty or full.
- The `capacity` variable stores the maximum size of the deque, which is used to check whether the deque is full before adding a new element.
- The circular nature of the deque allows us to use the modulo operator to wrap around the array when the `front` or `rear` pointer reaches the end of the array.
- This implementation provides an efficient way to add and remove elements from both ends of the deque, with an average time complexity of O(1).
- The use of a circular array and the `front` and `rear` pointers enables us to implement the deque operations in a concise and efficient manner.


### 2. Implementation

- The `MyCircularDeque` class is initialized with a maximum size `k`, and the `arr` vector is resized to `k` to store the elements.
- The `insertFront` method checks if the deque is full using the `isFull` method, and if not, it updates the `front` pointer and adds the new element to the front of the deque using `arr[front] = value`.
- The `insertLast` method checks if the deque is full, and if not, it adds the new element to the rear of the deque using `arr[rear] = value` and updates the `rear` pointer using `rear = (rear + 1) % capacity`.
- The `deleteFront` method checks if the deque is empty, and if not, it updates the `front` pointer using `front = (front + 1) % capacity` to remove the front element.
- The `deleteLast` method checks if the deque is empty, and if not, it updates the `rear` pointer using `rear = (rear - 1 + capacity) % capacity` to remove the rear element.
- The `getFront` and `getRear` methods return the front and rear elements of the deque, respectively, using `arr[front]` and `arr[(rear - 1 + capacity) % capacity]`.
- The `isEmpty` and `isFull` methods check whether the deque is empty or full, respectively, using the `size` variable.
- The implementation uses the modulo operator to handle the circular nature of the deque, ensuring that the `front` and `rear` pointers wrap around the array correctly.


<hr>

## Complexity Analysis

### Time Complexity: 
- All operations such as `insertFront`, `insertLast`, `deleteFront`, `deleteLast`, `getFront`, `getRear`, `isEmpty`, and `isFull` are performed in constant time, O(1), as they only involve updating indices and checking conditions without any loops or recursive calls. 
- The dominant operations are the updates of `front`, `rear`, and `size` variables, which are constant time operations as they involve simple arithmetic and assignment operations. 
- The justification of the Big O classification as O(1) stems from the fact that none of the operations depend on the size of the input, 'k', and all operations can be completed in a fixed amount of time regardless of the size of the input. 

### Space Complexity: 
- The algorithm uses a circular array of size 'k' to store the elements, resulting in a space complexity of O(k) as the memory usage grows linearly with the size of the input. 
- The data structure used, a vector `arr`, has a direct impact on the space complexity as it requires 'k' amount of space to store 'k' elements, hence the space complexity is O(k). 
- The justification of the space complexity as O(k) comes from the fact that the algorithm allocates a fixed amount of space at the beginning, which is proportional to the input size 'k', and does not change throughout the execution. 

<hr>

### Footnote

> This question is rated as **Medium** difficulty.

<hr>

### Similar Questions:

| Title | URL | Difficulty |
| ----- | --- | --- |
| Design Circular Queue | https://leetcode.com/problems/design-circular-queue |Medium|
| Design Front Middle Back Queue | https://leetcode.com/problems/design-front-middle-back-queue |Medium|
