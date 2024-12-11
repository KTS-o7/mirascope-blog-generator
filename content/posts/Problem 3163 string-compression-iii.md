+++
title = 'Problem 3163 String Compression III'
date = 2024-12-10T18:41:13+05:30
draft = false
series = 'leetcode'
tags = ['string']
toc = false
math = false
+++

# Problem Statement

**Link** - [Problem 3163](https://leetcode.com/problems/string-compression-iii/?envType=daily-question&envId=2024-11-04)

## Question

<p>Given a string <code>word</code>, compress it using the following algorithm:</p>

<ul>
	<li>Begin with an empty string <code>comp</code>. While <code>word</code> is <strong>not</strong> empty, use the following operation:

	<ul>
		<li>Remove a maximum length prefix of <code>word</code> made of a <em>single character</em> <code>c</code> repeating <strong>at most</strong> 9 times.</li>
		<li>Append the length of the prefix followed by <code>c</code> to <code>comp</code>.</li>
	</ul>
	</li>
</ul>

<p>Return the string <code>comp</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">word = &quot;abcde&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;1a1b1c1d1e&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>Initially, <code>comp = &quot;&quot;</code>. Apply the operation 5 times, choosing <code>&quot;a&quot;</code>, <code>&quot;b&quot;</code>, <code>&quot;c&quot;</code>, <code>&quot;d&quot;</code>, and <code>&quot;e&quot;</code> as the prefix in each operation.</p>

<p>For each prefix, append <code>&quot;1&quot;</code> followed by the character to <code>comp</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">word = &quot;aaaaaaaaaaaaaabb&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;9a5a2b&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>Initially, <code>comp = &quot;&quot;</code>. Apply the operation 3 times, choosing <code>&quot;aaaaaaaaa&quot;</code>, <code>&quot;aaaaa&quot;</code>, and <code>&quot;bb&quot;</code> as the prefix in each operation.</p>

<ul>
	<li>For prefix <code>&quot;aaaaaaaaa&quot;</code>, append <code>&quot;9&quot;</code> followed by <code>&quot;a&quot;</code> to <code>comp</code>.</li>
	<li>For prefix <code>&quot;aaaaa&quot;</code>, append <code>&quot;5&quot;</code> followed by <code>&quot;a&quot;</code> to <code>comp</code>.</li>
	<li>For prefix <code>&quot;bb&quot;</code>, append <code>&quot;2&quot;</code> followed by <code>&quot;b&quot;</code> to <code>comp</code>.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= word.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>word</code> consists only of lowercase English letters.</li>
</ul>


## Solution

```cpp
class Solution {
public:
    string compressedString(string word) {
        string comp = "";
        int size = word.size();
        comp.reserve(size*2);
        int ptr = 0;
        
        while (ptr < size) {
            int frq = 1;
            char ch = word[ptr];
            ptr++;
            
            while (ptr < size && word[ptr] == ch && frq < 9) {
                ptr++;
                frq++;
            }

            comp += (frq + '0');
            comp += ch;
        }
        
        return comp;
    }
};
```

## Complexity Analysis

```markdown
| Algorithm | Time Complexity | Space Complexity |
| --------- | --------------- | ---------------- |
| Run-length encoding  | O(n)           | O(n)             |
```

## Explanation

#### Intial Thoughts

To solve this problem, we should start by understanding the compression algorithm. It involves removing a prefix of the input string that consists of the same character repeated at most 9 times. We then append the length of this prefix and the character itself to the result string. This process repeats until the input string is empty. Key points to consider are: 
   1. Identify the repeated character prefixes in the string.
   2. Determine the length of each prefix, ensuring it doesn't exceed 9.
   3. Append the prefix length and character to the result string.
   4. Continue the process until the entire string is processed.
   5. Handle edge cases, such as an empty input string or single-character strings.


#### Intuitive Analysis

Intuitively, we can approach this problem by thinking of it as a process of scanning the input string from left to right, identifying blocks of consecutive identical characters, and representing each block with its length and the character. Important insights include: 
   1. Use a pointer to track the current position in the string.
   2. Compare characters to identify blocks of the same character.
   3. Keep a count of the length of each block.
   4. When a block ends, append its length and character to the result string.
   5. Repeat this process until the end of the string is reached, resulting in the compressed string.


### 1. Intuition

- The problem requires compressing a given string by replacing repeated characters with their count and character.
- To solve this, we can iterate through the string and keep track of the current character and its frequency.
- We should stop counting the frequency when we encounter a different character or when the frequency reaches 9.
- The key insight is to use a while loop to iterate through the string and another nested while loop to count the frequency of each character.
- This approach ensures that we process each character in the string exactly once, resulting in a time complexity of O(n).
- The space complexity is also O(n) because in the worst case, we might end up with a compressed string of the same length as the original string.
- The algorithmic choice of using a `while` loop and a `reserve` function for the result string is efficient and easy to implement.


### 2. Implementation

- We start by initializing an empty string `comp` to store the compressed result and a pointer `ptr` to keep track of the current position in the string.
- The line `comp.reserve(size*2)` is used to preallocate memory for the result string to avoid reallocations during the compression process.
- The outer `while` loop iterates through the string, and the inner `while` loop counts the frequency of each character using the condition `word[ptr] == ch && frq < 9`.
- The frequency is converted to a character using `frq + '0'` and appended to the result string `comp` along with the character `ch`.
- The use of `ptr++` ensures that we move to the next character in the string after processing the current one.
- Finally, the compressed string `comp` is returned as the result.
- The tradeoff here is between the time complexity of the algorithm and the space complexity of storing the result string.


<hr>

## Complexity Analysis

### Time Complexity: 
- The algorithm iterates over the string `word` once, using a while loop that increments `ptr` until it reaches the end of the string, resulting in a linear time complexity of O(n). 
- The dominant operation is the comparison `word[ptr] == ch`, which is performed within the nested while loop, but since this loop also increments `ptr` and only runs for a portion of the string, it does not increase the overall time complexity beyond O(n). 
- Mathematically, if we consider the string length as n, the number of operations (comparisons and concatenations) grows linearly with n, hence the time complexity is O(n), which encompasses the worst, average, and best cases. 

### Space Complexity: 
- The algorithm creates a new string `comp` to store the compressed version of `word`, with `comp.reserve(size*2)` ensuring enough space for the compressed string, which in the worst case could be larger than the original string if no characters are repeated. 
- The data structure impact comes from the strings `comp` and `word`, where the size of `comp` can grow up to twice the size of `word` in the worst-case scenario (when no compression is achieved), thus affecting the space complexity. 
- The space complexity is O(n) because the memory usage grows linearly with the size of the input string `word`, considering both the original string and the newly created `comp` string, which can be at most twice the size of `word`. 

<hr>

### Footnote

> This question is rated as **Medium** difficulty.

#### Hints

> Each time, just cut the same character in prefix up to at max 9 times. It’s always better to cut a bigger prefix.

<hr>

### Similar Questions:

| Title | URL | Difficulty |
| ----- | --- | --- |
| String Compression | https://leetcode.com/problems/string-compression |Medium|
| String Compression II | https://leetcode.com/problems/string-compression-ii |Hard|
