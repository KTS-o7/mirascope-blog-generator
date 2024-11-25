+++
title = 'Problem 3254 Find the Power of K-Size Subarrays I'
date = 2024-11-25T15:17:30+05:30
draft = false
series = 'leetcode'
tags = ['array', 'sliding window']
toc = false
math = false
+++

# Problem Statement

**Link** - [Problem 3254](https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/)

## Question

<p>You are given an array of integers <code>nums</code> of length <code>n</code> and a <em>positive</em> integer <code>k</code>.</p>

<p>The <strong>power</strong> of an array is defined as:</p>

<ul>
	<li>Its <strong>maximum</strong> element if <em>all</em> of its elements are <strong>consecutive</strong> and <strong>sorted</strong> in <strong>ascending</strong> order.</li>
	<li>-1 otherwise.</li>
</ul>

<p>You need to find the <strong>power</strong> of all <span data-keyword="subarray-nonempty">subarrays</span> of <code>nums</code> of size <code>k</code>.</p>

<p>Return an integer array <code>results</code> of size <code>n - k + 1</code>, where <code>results[i]</code> is the <em>power</em> of <code>nums[i..(i + k - 1)]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3,4,3,2,5], k = 3</span></p>

<p><strong>Output:</strong> [3,4,-1,-1,-1]</p>

<p><strong>Explanation:</strong></p>

<p>There are 5 subarrays of <code>nums</code> of size 3:</p>

<ul>
	<li><code>[1, 2, 3]</code> with the maximum element 3.</li>
	<li><code>[2, 3, 4]</code> with the maximum element 4.</li>
	<li><code>[3, 4, 3]</code> whose elements are <strong>not</strong> consecutive.</li>
	<li><code>[4, 3, 2]</code> whose elements are <strong>not</strong> sorted.</li>
	<li><code>[3, 2, 5]</code> whose elements are <strong>not</strong> consecutive.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,2,2,2,2], k = 4</span></p>

<p><strong>Output:</strong> <span class="example-io">[-1,-1]</span></p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,2,3,2,3,2], k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">[-1,3,-1,3,-1]</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == nums.length &lt;= 500</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= k &lt;= n</code></li>
</ul>

## Solution

```cpp
class Solution {
public:
    vector<int> resultsArray(vector<int>& nums, int k) {
        if(k==1)
            return nums;

        int size = nums.size();
        vector<int>result(size-k+1,-1);
        int count = 1;
        for(int i=0;i<size-1;i++){

            if(nums[i]+1 == nums[i+1])
                count++;
            else
                count =1;

            if(count >= k)
                result[i+2-k] = nums[i+1];
        }
        return result;

    }
};
```

## Complexity Analysis

```markdown
| Algorithm                                  | Time Complexity | Space Complexity |
| ------------------------------------------ | --------------- | ---------------- |
| Single-pass traversal with auxiliary array | O(n)            | O(n)             |
```

## Explanation

### 1. Intuition

- The problem requires finding the power of all subarrays of size k in the given array nums.
- The power of an array is defined as its maximum element if all elements are consecutive and sorted in ascending order, otherwise -1.
- To solve this problem, we need to check each subarray of size k and determine if its elements are consecutive and sorted.
- We can use a sliding window approach to efficiently check all subarrays of size k.
- We need to keep track of the count of consecutive elements in the current window.
- If the count is greater than or equal to k, we can update the result array with the maximum element of the current window.
- We need to handle the edge case where k is 1, in which case the result is simply the input array.

### 2. Implementation

- The function resultsArray takes a vector of integers nums and an integer k as input and returns a vector of integers.
- If k is 1, the function returns the input array nums.
- The function initializes a result vector of size n-k+1 with all elements set to -1.
- The function uses a for loop to iterate over the input array, keeping track of the count of consecutive elements.
- Inside the loop, the function checks if the current element is consecutive to the previous element by comparing nums[i] and nums[i+1].
- If the elements are consecutive, the function increments the count; otherwise, it resets the count to 1.
- If the count is greater than or equal to k, the function updates the result array with the maximum element of the current window.

<hr>

## Complexity Analysis

### Time Complexity:

- The solution iterates over the input array `nums` once, with a single loop running from `i=0` to `size-2`
- The dominant operation is the conditional increment of the count variable, which occurs once per iteration, resulting in O(n) time complexity
- The time complexity remains the same in the best, average, and worst cases as the input size `n` directly dictates the number of iterations

### Space Complexity:

- The solution creates an auxiliary array `result` of size `n-k+1`, where `n` is the size of the input array
- The space complexity is dominated by the storage required for the `result` array, leading to O(n) space complexity
- The space complexity remains the same in all cases as the size of the auxiliary array directly depends on the input size, which must be stored in memory

<hr>

### Footnote

> This question is rated as **Medium** difficulty.

#### Hints

> Can we use a brute force solution with nested loops and HashSet?

<hr>

### Similar Questions:

| Title                                           | URL                                                                           | Difficulty |
| ----------------------------------------------- | ----------------------------------------------------------------------------- | ---------- |
| Maximum Sum of Distinct Subarrays With Length K | https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k | Medium     |
