+++
title = 'Problem 3152 Special Array II'
date = 2024-12-10T18:36:18+05:30
draft = false
series = 'leetcode'
tags = ['array', 'binary search', 'prefix sum']
toc = false
math = false
+++

# Problem Statement

**Link** - [Problem 3152](https://leetcode.com/problems/special-array-ii/?envType=daily-question&envId=2024-12-09)

## Question

<p>An array is considered <strong>special</strong> if every pair of its adjacent elements contains two numbers with different parity.</p>

<p>You are given an array of integer <code>nums</code> and a 2D integer matrix <code>queries</code>, where for <code>queries[i] = [from<sub>i</sub>, to<sub>i</sub>]</code> your task is to check that <span data-keyword="subarray">subarray</span> <code>nums[from<sub>i</sub>..to<sub>i</sub>]</code> is <strong>special</strong> or not.</p>

<p>Return an array of booleans <code>answer</code> such that <code>answer[i]</code> is <code>true</code> if <code>nums[from<sub>i</sub>..to<sub>i</sub>]</code> is special.<!-- notionvc: e5d6f4e2-d20a-4fbd-9c7f-22fbe52ef730 --></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,4,1,2,6], queries = [[0,4]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[false]</span></p>

<p><strong>Explanation:</strong></p>

<p>The subarray is <code>[3,4,1,2,6]</code>. 2 and 6 are both even.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [4,3,1,6], queries = [[0,2],[2,3]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[false,true]</span></p>

<p><strong>Explanation:</strong></p>

<ol>
	<li>The subarray is <code>[4,3,1]</code>. 3 and 1 are both odd. So the answer to this query is <code>false</code>.</li>
	<li>The subarray is <code>[1,6]</code>. There is only one pair: <code>(1,6)</code> and it contains numbers with different parity. So the answer to this query is <code>true</code>.</li>
</ol>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= queries.length &lt;= 10<sup>5</sup></code></li>
	<li><code>queries[i].length == 2</code></li>
	<li><code>0 &lt;= queries[i][0] &lt;= queries[i][1] &lt;= nums.length - 1</code></li>
</ul>

## Solution

```cpp
class Solution {
public:
    vector<bool> isArraySpecial(vector<int>& nums, vector<vector<int>>& queries) {
        vector<bool> ans(queries.size(), false);
        vector<int> prefix(nums.size(), 0);
        prefix[0] = 0;

        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] % 2 == nums[i - 1] % 2) {
                prefix[i] = prefix[i - 1] + 1;
            }
            else {
                prefix[i] = prefix[i - 1];
            }
        }

        for (int i = 0; i < queries.size(); i++) {
            vector<int> query = queries[i];
            int start = query[0];
            int end = query[1];

            ans[i] = prefix[end] - prefix[start] == 0;
        }

        return ans;
    }
};
```

## Complexity Analysis

```markdown
| Algorithm                         | Time Complexity | Space Complexity |
| --------------------------------- | --------------- | ---------------- |
| Prefix Sum Array with Linear Scan | O(n + m)        | O(n + m)         |
```

## Explanation

#### Intial Thoughts

To approach this problem, we need to think about how to efficiently check if every pair of adjacent elements in a given subarray has different parity. One possible approach could be to iterate over each subarray and check the parity of each pair of adjacent elements. Another approach could be to use some kind of prefix sum or cumulative sum to keep track of the number of pairs with the same parity. We also need to think about how to efficiently handle multiple queries on the same array.

#### Intuitive Analysis

Intuitively, we can solve this problem by creating a prefix array that keeps track of the number of pairs of adjacent elements with the same parity. We can then use this prefix array to quickly answer each query by checking the difference in the prefix array values between the start and end of the subarray. If this difference is zero, then the subarray is special. We can also think of this problem in terms of finding the 'bad' pairs of adjacent elements and counting them. The subarray is special if there are no such 'bad' pairs. We can also consider using a similar approach to the one used in the solution, where we create a prefix array and then use it to answer each query.

### 1. Intuition

- The problem requires checking if every pair of adjacent elements in a subarray has different parity.
- To solve this efficiently, we can use a prefix array to keep track of the number of pairs with the same parity.
- The prefix array will help us to calculate the number of pairs with the same parity in any subarray in constant time.
- We need to iterate over the array and update the prefix array based on the parity of the current and previous elements.
- If the parity of the current and previous elements is the same, we increment the prefix array value.
- The key insight is that a subarray is special if the difference between the prefix array values at the end and start of the subarray is 0.
- This approach allows us to solve the problem in linear time complexity.

### 2. Implementation

- We initialize a `prefix` array with the same length as the input `nums` array and set `prefix[0]` to 0.
- We iterate over the `nums` array and update the `prefix` array using the condition `if (nums[i] % 2 == nums[i - 1] % 2)` to check if the current and previous elements have the same parity.
- If the condition is true, we increment the `prefix` array value at the current index `i` by setting `prefix[i] = prefix[i - 1] + 1`.
- Otherwise, we set `prefix[i] = prefix[i - 1]` to keep the same value as the previous index.
- We then iterate over the `queries` array and for each query, we calculate the difference between the `prefix` array values at the end and start of the subarray using `prefix[end] - prefix[start]`.
- If the difference is 0, we set the corresponding value in the `ans` array to `true`, indicating that the subarray is special.
- Finally, we return the `ans` array containing the results for all queries.

<hr>

## Complexity Analysis

### Time Complexity:

- The algorithm has two main loops: the first loop iterates over the `nums` array to calculate the `prefix` array, resulting in a time complexity of O(n), where n is the size of the `nums` array.
- The second loop iterates over the `queries` array, and for each query, it performs a constant amount of work, resulting in a time complexity of O(m), where m is the size of the `queries` array. Since these loops are executed sequentially, the overall time complexity is O(n + m).
- The mathematical reasoning behind this time complexity is based on the fact that the algorithm performs a linear scan over the input arrays, and the number of operations grows linearly with the size of the input. This justifies the Big O classification of O(n + m), as it represents the worst-case, average-case, and best-case time complexities.

### Space Complexity:

- The algorithm uses two additional arrays: `prefix` and `ans`, which have sizes of n and m, respectively, where n is the size of the `nums` array and m is the size of the `queries` array.
- The `prefix` array is used to store the prefix sum, and its size is directly proportional to the size of the `nums` array. The `ans` array is used to store the results of the queries, and its size is directly proportional to the size of the `queries` array.
- The space complexity is therefore O(n + m), as the algorithm uses a total of n + m extra space to store the `prefix` and `ans` arrays, in addition to the input arrays `nums` and `queries`.

<hr>

### Footnote

> This question is rated as **Medium** difficulty.

#### Hints

> Try to split the array into some non-intersected continuous special subarrays.

> For each query check that the first and the last elements of that query are in the same subarray or not.
