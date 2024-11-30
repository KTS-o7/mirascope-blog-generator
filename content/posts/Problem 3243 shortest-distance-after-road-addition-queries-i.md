+++
title = 'Problem 3243 Shortest Distance After Road Addition Queries I'
date = 2024-11-30T11:09:07+05:30
draft = false
series = 'leetcode'
tags = ['array', 'breadth-first search', 'graph']
toc = false
math = false
+++

# Problem Statement

**Link** - [Problem 3243](https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/)

## Question

<p>You are given an integer <code>n</code> and a 2D integer array <code>queries</code>.</p>

<p>There are <code>n</code> cities numbered from <code>0</code> to <code>n - 1</code>. Initially, there is a <strong>unidirectional</strong> road from city <code>i</code> to city <code>i + 1</code> for all <code>0 &lt;= i &lt; n - 1</code>.</p>

<p><code>queries[i] = [u<sub>i</sub>, v<sub>i</sub>]</code> represents the addition of a new <strong>unidirectional</strong> road from city <code>u<sub>i</sub></code> to city <code>v<sub>i</sub></code>. After each query, you need to find the <strong>length</strong> of the <strong>shortest path</strong> from city <code>0</code> to city <code>n - 1</code>.</p>

<p>Return an array <code>answer</code> where for each <code>i</code> in the range <code>[0, queries.length - 1]</code>, <code>answer[i]</code> is the <em>length of the shortest path</em> from city <code>0</code> to city <code>n - 1</code> after processing the <strong>first </strong><code>i + 1</code> queries.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 5, queries = [[2,4],[0,2],[0,4]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[3,2,1]</span></p>

<p><strong>Explanation: </strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/06/28/image8.jpg" style="width: 350px; height: 60px;" /></p>

<p>After the addition of the road from 2 to 4, the length of the shortest path from 0 to 4 is 3.</p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/06/28/image9.jpg" style="width: 350px; height: 60px;" /></p>

<p>After the addition of the road from 0 to 2, the length of the shortest path from 0 to 4 is 2.</p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/06/28/image10.jpg" style="width: 350px; height: 96px;" /></p>

<p>After the addition of the road from 0 to 4, the length of the shortest path from 0 to 4 is 1.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 4, queries = [[0,3],[0,2]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[1,1]</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/06/28/image11.jpg" style="width: 300px; height: 70px;" /></p>

<p>After the addition of the road from 0 to 3, the length of the shortest path from 0 to 3 is 1.</p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/06/28/image12.jpg" style="width: 300px; height: 70px;" /></p>

<p>After the addition of the road from 0 to 2, the length of the shortest path remains 1.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= n &lt;= 500</code></li>
	<li><code>1 &lt;= queries.length &lt;= 500</code></li>
	<li><code>queries[i].length == 2</code></li>
	<li><code>0 &lt;= queries[i][0] &lt; queries[i][1] &lt; n</code></li>
	<li><code>1 &lt; queries[i][1] - queries[i][0]</code></li>
	<li>There are no repeated roads among the queries.</li>
</ul>

## Solution

```cpp
class Solution {
public:
    vector<vector<int>> graph;
    vector<int> distances;

    int computeShortestPath(int start_node, int total_nodes) {
        queue<int> bfs_queue;
        bfs_queue.push(start_node);

        while (!bfs_queue.empty()) {
            int curr_node = bfs_queue.front();
            bfs_queue.pop();

            for (const int& neighbor : graph[curr_node]) {
                if (distances[neighbor] > distances[curr_node] + 1) {
                    distances[neighbor] = distances[curr_node] + 1;
                    bfs_queue.push(neighbor);
                }
            }
        }

        return distances[total_nodes - 1];
    }

    vector<int> shortestDistanceAfterQueries(int total_nodes, vector<vector<int>>& queries) {
        graph.resize(total_nodes);
        for (int i = 0; i < total_nodes - 1; i++) {
            graph[i].push_back(i + 1);
        }

        distances.resize(total_nodes);
        iota(distances.begin(), distances.end(), 0);
        // iota is used to prevent loops like this
        // for (int i = 0; i < n; ++i) {
                //distances[i] = i;
            //}
        vector<int> result;
        result.reserve(queries.size());
        for (const auto& query : queries) {
            graph[query[0]].push_back(query[1]);
            result.push_back(computeShortestPath(query[0], total_nodes));
        }

        return result;
    }
};

```

## Complexity Analysis

```markdown
| Algorithm                                                | Time Complexity | Space Complexity |
| -------------------------------------------------------- | --------------- | ---------------- |
| Unweighted Directed Graph BFS with Dynamic Edge Addition | O(n + qE + qn)  | O(n)             |
```

## Explanation

#### Intial Thoughts

Consider the initial graph where cities are connected in a straight line. We can assume that the shortest path starts at city 0 and ends at city n-1,
and that initially there is no need to process queries because we know that it takes n-1 steps to reach the last city.
We also know that new roads can only reduce the length of the shortest path,
and that we only need to consider queries that reduce the length of the shortest path.
A query that reduces the length will be one where the destination is the same as the current shortest path.
We need a data structure to store the shortest path lengths and to process each query.

#### Intuitive Analysis

A good approach to solve this problem is by using Breadth-First Search (BFS) with each query as the starting point.
Before processing the queries, initialize a graph that represents the initial connections between the cities.
Initialize the distance from city 0 to itself as 0 and all other distances as infinity.
Then for each query, update the graph with the new connection, and run BFS from the source of the new connection.
During BFS, update the shortest distances for all cities that become reachable with fewer steps.
After processing each query, return the shortest distance to city n-1 as the answer.

### 1. Intuition

- The problem can be solved using a graph and a breadth-first search (BFS) algorithm.
- We can represent the cities as nodes in the graph and the roads as directed edges.
- The shortest path from city 0 to city n-1 can be found by performing a BFS from city 0.
- We can use a queue to keep track of the nodes to visit next.
- We can use a distances array to keep track of the shortest distance from city 0 to each city.
- We can update the distances array as we visit each node.
- We can return the shortest distance from city 0 to city n-1 after each query.

### 2. Implementation

- We initialize the graph with n nodes and add a directed edge from each node to the next node.
- We initialize the distances array with the initial distances from city 0 to each city.
- We use the `iota` function to initialize the distances array with the initial distances.
- We iterate over the queries and add a directed edge from the start node to the end node.
- We call the `computeShortestPath` function to update the distances array and return the shortest distance.
- We use a queue to perform the BFS and update the distances array.
- We use the `push_back` function to add nodes to the queue and the `pop` function to remove nodes from the queue.
- We use the `resize` function to resize the graph and distances array.

<hr>

## Complexity Analysis

### Time Complexity:

- The time complexity is dominant in three main parts: 1. Initialization of the adjacency list with O(n) operations, and 2. iterating querying the `queries` with O(q), and inside this loop, finding the shortest path via BFS, which results in an operation for every edge as the graph is traversed in O(E), with also an additional operation in O(n), leading to the time complexity of O(n + q*E + q*n).
- In this given sequence `graph[query[0]].push_back(query[1])` and the `computeShortestPath` loop, we see every operation between initializing nodes to the queries executed takes time O(n + q*E + q*n), as both operations do so. q iteration is due to queries pushed after initialization, leading to its addition to Big O. With many operations this sequence performs with n in each and E steps (BFS) for in a loop that is dependent on n from queries and the number of operations dependent as such total nodes (n), all results in the Big O.
- An optimization is applied using the `reserve` function on result, but overall the initialized data for each loop in given sequences pushes our complexity from above to our final Time Complexity which results as above O(n + q*E + q*n) when simplifying to our complexity with dropping constants

### Space Complexity:

- The space complexity is mainly influenced by the adjacency list `graph` with a size of O(n), as it will hold at most O(n) edges, while the distance array also has O(n) space complexity.
- With each node in a list initialized in `graph.resize(total_nodes);` the data for representing the given data doesn't scale any higher than O(n) because of initializing each data to all elements in total numbers to not miss any result in queries without having anything to do with E, thus not adding this Big O notation here.
- With BFS operations on every node in graph it's going to produce the needed `result` having the same assumption above resulting with O(n) Notation we write here on the complexity and the constant factor for additional variables and data types are dropped

<hr>

### Footnote

> This question is rated as **Medium** difficulty.

#### Hints

> Maintain the graph and use an efficient shortest path algorithm after each update.

> We use BFS/Dijkstra for each query.
