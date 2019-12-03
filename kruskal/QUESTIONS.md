# Kruskal Questions Statements

## URI Questions

### 1152 - Dark Roads

Economic times these days are tough, even in Byteland. To reduce the operating costs, the government of Byteland has decided to optimize the road lighting. Till now every road was illuminated all night long, which costs 1 Bytelandian Dollar per meter and day. To save money, they decided to no longer illuminate every road, but to switch off the road lighting of some streets. To make sure that the inhabitants of Byteland still feelsafe, they want to optimize the lighting in such a way, that after darkening some streets at night, there will still be at least one illuminated path from every junction in Byteland to every other junction.

What is the maximum daily amount of money the government of Byteland can save, without making their inhabitants feel unsafe? 

#### Input

The input file contains several test cases. Each test case starts with two numbers m and n , that are the number of junctions in Byteland and the number of roads in Byteland, respectively. Follow n integer triples x, y, z, specifying that there will be a bidirectional road between x and y with length z meters. The input is terminated by m=n=0. The graph specified by each test case is connected.

#### Output

For each test case print one line containing the maximum daily amount the government can save.

#### Solution

[Click here - solution in Python](./dark-roads.py)

[Click here - solution in C++](./dark-roads.cpp)