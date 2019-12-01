# Breadth-First Search Questions Statements

## Codeforces Questions

### 217A - Ice Skating

Bajtek is learning to skate on ice. He's a beginner, so his only mode of transportation is pushing off from a snow drift to the north, east, south or west and sliding until he lands in another snow drift. He has noticed that in this way it's impossible to get from some snow drifts to some other by any sequence of moves. He now wants to heap up some additional snow drifts, so that he can get from any snow drift to any other one. He asked you to find the minimal number of snow drifts that need to be created.

We assume that Bajtek can only heap up snow drifts at integer coordinates.

#### Input:

The first line of input contains a single integer n (1 ≤ n ≤ 100) — the number of snow drifts. Each of the following n lines contains two integers xi and yi (1 ≤ xi, yi ≤ 1000) — the coordinates of the i-th snow drift.

_Note that the north direction coinсides with the direction of Oy axis, so the east direction coinсides with the direction of the Ox axis. All snow drift's locations are distinct._

#### Output:

The minimal number of snow drifts that need to be created in order for Bajtek to be able to reach any snow drift from any other one.

#### Solution:

[Click here](./ice-skating.py)

## ATAL Second Exercise List

### Importing Libraries

Vin is a programmer and needs to import some libraries into her code. After some research, she finds that some libraries depend onfrom other libraries, which in turn require other libraries and so on. 

Vin has come up with a final list of all the libraries you'll need. With this list in hand, she suspects it has loops. For example, if a library A depends on another library B, which in turn depends on library A would make the task endless.

#### Input:

Given the list of dependencies between libraries. As input you will get an n, which is the number of libraries, enumerated from 1 to n, and an array symbolizing dependencies.

#### Output:

Determines whether or not Vin will be able to import all libraries. Your solution should say YES if Vin can import all libraries and NO otherwise.

#### Solution:

[Click here](./importing-libraries.py)