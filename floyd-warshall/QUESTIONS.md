# Floyd-Warshall Questions Statements

## Codeforces Questions

### 295B - Greg and Graph

Greg has a weighed directed graph, consisting of n vertices. In this graph any pair of distinct vertices has an edge between them in both directions. Greg loves playing with the graph and now he has invented a new game:

1. The game consists of n steps.
2. On the i-th step Greg removes vertex number xi from the graph. As Greg removes a vertex, he also removes all the edges that go in and out of this vertex.
3. Before executing each step, Greg wants to know the sum of lengths of the shortest paths between all pairs of the remaining vertices. The shortest path can go through any remaining vertex. In other words, if we assume that d(i, v, u) is the shortest path between vertices v and u in the graph that formed before deleting vertex xi, then Greg wants to know the value of the sum of all shortest paths between each pair of vertices. 

#### Input

The first line contains integer n — the number of vertices in the graph. Next n lines contain n integers each — the graph adjacency matrix: the j-th number in the i-th line aij represents the weight of the edge that goes from vertex i to vertex j. The next line contains n distinct integers: x1, x2, ..., xn — the vertices that Greg deletes.

#### Output

Print n integers — the i-th number equals the required sum before the i-th step.

#### Solution

[Click here](./greg-and-graph.py)