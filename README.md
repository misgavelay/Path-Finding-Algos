# Path-Finding-Algos
A platform that shows how diffrent path finding algorithems work in an interactive and visual way.
For now includes A* and Disjktra algorithems

## Main Menu
At the start of the program a menu opens that allows to choose between diffrent algorithems.
In Adition there is an instructions options that describes how to uses the platform

## Box
The box class is used to represent nodes.
For each box the boxes from each side are defined as its neighbors with out counting the diagnol ones.

## BFS 
[https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#Algorithm](https://en.wikipedia.org/wiki/Breadth-first_search)
Implemented with a qeue

## A*
https://en.wikipedia.org/wiki/A*_search_algorithm
To implement the A* algorithem en externael library is used PriortyQueue().
Priority Queue is an extension of the queue with the following properties:
-An element with high priority is dequeued before an element with low priority.
-If two elements have the same priority, they are served according to their order in the queue
In the A star allgorithim the f_count is our priority.