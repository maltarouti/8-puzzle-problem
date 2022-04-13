# 8-Puzzle-Problem

![image](https://user-images.githubusercontent.com/63660298/162525325-370d69dd-591b-4a6d-971d-a91db7a50694.png)

# Introduction
The 8 Puzzle, often known as the sliding puzzle, is a classic puzzle that consists of 9 tiles with three rows and three columns. The puzzle consists of 8 tiles with numbers ranging from 1 to 8 and one empty tile. The solution is to move the tiles around into different spots to have the numbers displayed same as you goal state. In this project, we will attempt to solve this puzzle using search algorithms and show a basic comparison between breadth-first search and A star algorithms.

# Algorithms
1. Breadth-first search (BFS)

Breadth-first search is a uniformed algorithm for traversing, searching in a tree or a graph. BFS starts from the tree root and explores all the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level. This search algorithm uses a queue data structure to explore the undiscovered nodes in order.

2. A*

A* is an informed algorithm that avoids expanding the expensive paths before the cheap ones. This algorithm is often used in many fields of computer science due to its completeness, optimality, and efficiency.

# Sample run and differences between BFS and A*
This section contains a sample test for the BFS and A* techniques, as well as the differences between them in terms of time and speed. To ensure a good and fair comparison, the same sample test was evaluated on both algorithms.

* The sample run
```
Intial State:
2 8 1
- 4 3
7 6 5

Goal State:
1 2 3
8 - 4
7 6 5
```
* Result

After running this sample run on both alogrithms, I found that A* is much faster than BFS algorithm. A* has solved the problem in 0.003 with only 44 expanded nodes, unlike BFS which took 0.02 seconds to reach the goal state with 359 expanded nodes. 

# Files
 ```
 .
├── input_sample1.txt
├── input_sample2.txt
├── input_sample3.txt
├── output_sample1.txt
├── output_sample2.txt
├── output_sample3.txt
├── PriorityQueue.py
├── puzzle.py ** The main file **
├── Queue.py
└── tree.py
```
* Note that I did a little demo inside the puzzle file utilizing the 3 sample inputs

# Conclusion
In the conclusion A* search is much faster than the breadth-first search because A* is an informed strategy where it follows the lowest path in cost. Breadth-first search is an uninformed strategy that takes a lot of time, because it expands all the nodes searching for the goal.

**This project code is not the best so feel free to fork this repository and improve it to better.**
