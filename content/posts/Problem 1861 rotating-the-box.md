+++
title = 'Problem 1861 Rotating the Box'
date = 2024-11-23T19:49:39+05:30
draft = false
series = 'leetcode'
tags = ['array', 'two pointers', 'matrix']
toc = false
math = false
+++

# Problem Statement

**Link** - [Problem 1861](https://leetcode.com/problems/rotating-the-box/)

## Question

<p>You are given an <code>m x n</code> matrix of characters <code>box</code> representing a side-view of a box. Each cell of the box is one of the following:</p>

<ul>
	<li>A stone <code>&#39;#&#39;</code></li>
	<li>A stationary obstacle <code>&#39;*&#39;</code></li>
	<li>Empty <code>&#39;.&#39;</code></li>
</ul>

<p>The box is rotated <strong>90 degrees clockwise</strong>, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity <strong>does not</strong> affect the obstacles&#39; positions, and the inertia from the box&#39;s rotation <strong>does not </strong>affect the stones&#39; horizontal positions.</p>

<p>It is <strong>guaranteed</strong> that each stone in <code>box</code> rests on an obstacle, another stone, or the bottom of the box.</p>

<p>Return <em>an </em><code>n x m</code><em> matrix representing the box after the rotation described above</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/04/08/rotatingtheboxleetcodewithstones.png" style="width: 300px; height: 150px;" /></p>

<pre>
<strong>Input:</strong> box = [[&quot;#&quot;,&quot;.&quot;,&quot;#&quot;]]
<strong>Output:</strong> [[&quot;.&quot;],
&nbsp;        [&quot;#&quot;],
&nbsp;        [&quot;#&quot;]]
</pre>

<p><strong class="example">Example 2:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/04/08/rotatingtheboxleetcode2withstones.png" style="width: 375px; height: 195px;" /></p>

<pre>
<strong>Input:</strong> box = [[&quot;#&quot;,&quot;.&quot;,&quot;*&quot;,&quot;.&quot;],
&nbsp;             [&quot;#&quot;,&quot;#&quot;,&quot;*&quot;,&quot;.&quot;]]
<strong>Output:</strong> [[&quot;#&quot;,&quot;.&quot;],
&nbsp;        [&quot;#&quot;,&quot;#&quot;],
&nbsp;        [&quot;*&quot;,&quot;*&quot;],
&nbsp;        [&quot;.&quot;,&quot;.&quot;]]
</pre>

<p><strong class="example">Example 3:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/04/08/rotatingtheboxleetcode3withstone.png" style="width: 400px; height: 218px;" /></p>

<pre>
<strong>Input:</strong> box = [[&quot;#&quot;,&quot;#&quot;,&quot;*&quot;,&quot;.&quot;,&quot;*&quot;,&quot;.&quot;],
&nbsp;             [&quot;#&quot;,&quot;#&quot;,&quot;#&quot;,&quot;*&quot;,&quot;.&quot;,&quot;.&quot;],
&nbsp;             [&quot;#&quot;,&quot;#&quot;,&quot;#&quot;,&quot;.&quot;,&quot;#&quot;,&quot;.&quot;]]
<strong>Output:</strong> [[&quot;.&quot;,&quot;#&quot;,&quot;#&quot;],
&nbsp;        [&quot;.&quot;,&quot;#&quot;,&quot;#&quot;],
&nbsp;        [&quot;#&quot;,&quot;#&quot;,&quot;*&quot;],
&nbsp;        [&quot;#&quot;,&quot;*&quot;,&quot;.&quot;],
&nbsp;        [&quot;#&quot;,&quot;.&quot;,&quot;*&quot;],
&nbsp;        [&quot;#&quot;,&quot;.&quot;,&quot;.&quot;]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == box.length</code></li>
	<li><code>n == box[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 500</code></li>
	<li><code>box[i][j]</code> is either <code>&#39;#&#39;</code>, <code>&#39;*&#39;</code>, or <code>&#39;.&#39;</code>.</li>
</ul>

## Solution

```cpp
class Solution {
public:
    vector<vector<char>> rotateTheBox(vector<vector<char>>& box) {
        int m =box.size(),n=box[0].size();
        for(auto &row:box){
            int obstacle = row.size();
            for(int i = row.size()-1; i>=0; i--){
                if(row[i]=='#'){
                    char temp = row[i];
                    row[i]='.';
                    row[obstacle-1]=temp;
                    obstacle--;
                }

                if(row[i]=='*')
                    obstacle =i;
            }
        }

        vector<vector<char>>result(n,vector<char>(m,'.'));

        for(int i = 0; i<m; i++)
            for(int j = 0; j<n; j++)
                result[j][m-1-i] = box[i][j];
        
        return result;
    }
};
```

## Complexity Analysis

```markdown
| Algorithm | Time Complexity | Space Complexity |
| --------- | --------------- | ---------------- |
| TwoPass  | O(mn)           | O(mn)             |
```

## Explanation

### 1. Intuition

```markdown
- The problem requires us to simulate the rotation of a box 90 degrees clockwise and let the stones fall due to gravity.
- We can solve this problem in two steps: first, we simulate the falling of stones in each row, and then we rotate the box 90 degrees clockwise.
- To simulate the falling of stones, we iterate over each row from right to left and move the stones to the rightmost available position.
- If we encounter an obstacle, we move the obstacle to its original position and continue the process.
- After simulating the falling of stones, we rotate the box 90 degrees clockwise by swapping the rows and columns.
```

### 2. Implementation

- We start by iterating over each row in the box and simulating the falling of stones.
- We use a variable `obstacle` to keep track of the rightmost available position in the row.
- We iterate over each character in the row from right to left and check if it is a stone.
- If it is a stone, we move it to the rightmost available position by swapping it with the character at the `obstacle` index.
- We then decrement the `obstacle` index to keep track of the new rightmost available position.
- If we encounter an obstacle, we move it to its original position and reset the `obstacle` index.
- After simulating the falling of stones, we create a new matrix `result` to store the rotated box.
- We iterate over each character in the original box and assign it to the corresponding position in the `result` matrix.
- We use the formula `result[j][m-1-i] = box[i][j]` to rotate the box 90 degrees clockwise.
- Finally, we return the `result` matrix.


<hr>

## Complexity Analysis

### Time Complexity: 
- The outer loop in the solution iterates through each row of the input box, resulting in a time complexity of O(m). 
- Inside the outer loop, each element in the row is traversed, resulting in a time complexity of O(n). 
- So, the overall time complexity of the solution is O(mn). 
- Additionally, the algorithm includes a second loop that populates the result, which also results in a time complexity of O(mn). 

### Space Complexity: 
- The algorithm includes additional space to store the transformed box, resulting in a space complexity of O(mn). 
- This space is needed to accommodate the output of size mxn, where m is the number of rows in the input and n is the number of columns. 
