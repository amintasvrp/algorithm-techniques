# Dynamic Programming Questions Statements

## Codeforces Questions

### 416B - Art Union

A well-known art union called "Kalevich is Alive!" manufactures objects d'art (pictures). The union consists of n painters who decided to organize their work as follows.

Each painter uses only the color that was assigned to him. The colors are distinct for all painters. Let's assume that the first painter uses color 1, the second one uses color 2, and so on. Each picture will contain all these n colors. Adding the j-th color to the i-th picture takes the j-th painter tij units of time.

Order is important everywhere, so the painters' work is ordered by the following rules:

1. Each picture is first painted by the first painter, then by the second one, and so on. That is, after the j-th painter finishes working on the picture, it must go to the (j + 1)-th painter (if j < n);
2. Each painter works on the pictures in some order: first, he paints the first picture, then he paints the second picture and so on;
3. Each painter can simultaneously work on at most one picture. However, the painters don't need any time to have a rest;
4. As soon as the j-th painter finishes his part of working on the picture, the picture immediately becomes available to the next painter.

Given that the painters start working at time 0, find for each picture the time when it is ready for sale.

#### Input:

The first line of the input contains integers m and  n, where m is the number of pictures and n is the number of painters. Then follow the descriptions of the pictures, one per line. Each line contains n integers ti1, ti2, ..., tin, where tij is the time the j-th painter needs to work on the i-th picture.

#### Output:

Print the sequence of m integers r1, r2, ..., rm, where ri is the moment when the n-th painter stopped working on the i-th picture.

#### Solution:

[Click here](./art-union.py)

### 368B - Sereja and Suffixes

Sereja has an array a, consisting of n integers a1, a2,..., an. The boy cannot sit and do nothing, he decided to study an array. Sereja took a piece of paper and wrote out m integers l1, l2, ..., lm. For each number li he wants to know how many distinct numbers are staying on the positions li, li + 1, ..., n. Formally, he want to find the number of distinct numbers among ali, ali + 1, ..., an ?

Sereja wrote out the necessary array elements but the array was so large and the boy was so pressed for time. Help him, find the answer for the described question for each li.

#### Input

The first line contains two integers n and m (1 ≤ n, m ≤ 105). The second line contains n integers a1, a2, ..., an (1 ≤ ai ≤ 105) — the array elements.

Next m lines contain integers l1, l2, ..., lm. The i-th line contains integer li (1 ≤ li ≤ n).

#### Output

Print m lines — on the i-th line print the answer to the number li.

#### Solution

[Click here](./sereja-and-suffixes.py)

### 574B - Bear and Three Musketeers

Do you know a story about the three musketeers? Anyway, you will learn about its origins now. Richelimakieu is a cardinal in the city of Bearis. He is tired of dealing with crime by himself. He needs three brave warriors to help him to fight against bad guys.

There are n warriors. Richelimakieu wants to choose three of them to become musketeers but it's not that easy. The most important condition is that musketeers must know each other to cooperate efficiently. And they shouldn't be too well known because they could be betrayed by old friends. For each musketeer his recognition is the number of warriors he knows, excluding other two musketeers.

Help Richelimakieu! Find if it is possible to choose three musketeers knowing each other, and what is minimum possible sum of their recognitions.

#### Input

The first line contains two space-separated integers, n and m (3 ≤ n ≤ 4000, 0 ≤ m ≤ 4000) — respectively number of warriors and number of pairs of warriors knowing each other.

i-th of the following m lines contains two space-separated integers ai and bi (1 ≤ ai, bi ≤ n, ai ≠ bi). Warriors ai and bi know each other. Each pair of warriors will be listed at most once.

#### Output

If Richelimakieu can choose three musketeers, print the minimum possible sum of their recognitions. Otherwise, print "-1" (without the quotes).

#### Solution

[Click here](./bear-and-three-musketeers.py)

## ATAL Second Exercise List

### Number of Hops

Given a vector of integers, each representing the number of hops that can be given forward in the vector, implement a solution using Dynamic Programming that finds the minimum number of hops that can be made between vector[0] and vector[n], being the size of the vector.

#### Input:

A vector of integers, each representing the number of hops that can be given forward in the vector.

#### Output:

The minimum number of hops that can be taken.

#### Solution:

[Click here](./libraries.py)

### Pizza Delivery

Kelsier is a motoboy who works delivering pizzas to a pizzeria, however, recently the pizzeria has been receiving many complaints of some orders that take a long time to arrive.

So the pizzeria decided that Kelsier would deliver orders that took longer to deliver first. In other words, supposing the pizzeria says that Kelsier should deliver a maximum of 10 pizzas, among the orders that the pizzeria received, these being; 5 pizzas that take 15 min to be delivered; 4 pizzas that take 23 minutes to be delivered; 2 pizzas that take 21 min; 4 pizzas that take 16 min; 5 pizzas that take 19 min; and 2 pizzas that take 18 min to be delivered. Therefore, Kelsier must deliver the pizzas in a way that does not exceed the maximum quantity (10) stipulated by the pizzeria, maximizing the delivery time. Soon, Kelsier would deliver the 4 pizzas that take 23 min, the 2 pizzas that take 21 min and the 2 pizzas that take 18 min, totaling 8 pizzas delivered in 62 min.

Write a solution to help Kelsier know how long it will take to deliver the longest orders.

#### Input

A list of tuples where the first element represents how many pizzas are in the package, and the second element represents how long it will take to deliver.

#### Output

Time it will take to deliver the longest orders.

#### Solution

[Click here](./pizza-delivery.py)

### Sum of Subset

Given a set of nonnegative integers and a sum value, implement a solution using dynamic programming that determines whether there is a subset of the given set whose sum of values equals sum. If so, also determine the smallest possible subset.

#### Input

A set of nonnegative integers and a sum value.

#### Output

Print True if the subset exists, and show the smallest possible subset. Otherwise, print False.

#### Solution

[Click here](./sum-of-subset.py)
