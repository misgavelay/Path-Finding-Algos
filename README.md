# Path-Finding-Algos
A platform that shows how diffrent path finding algorithems work in an interactive and visual way.
For now includes A* and Disjktra algorithems

## Main Menu
At the start of the program a menu opens that allows to choose between diffrent algorithems.
In Adition there is an instructions options that describes how to uses the platform

## Box
The box class is used to represent nodes.
For each box the boxes from each side are defined as its neighbors with out counting the diagnol ones.

## Disjktra 
https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#Algorithm
The implementation of the algorithem is a bit diffrent then the theoretical one.

Insted of using a tentative distance to keep track of the fastet rout we use the following logic:
each node has an atribute "prior" and an atribute "qeued" wich are initailly set to none and false respectevly.
during the algorithem for each current node we are examening, we check all of his neighboors. 
if his neighbor is not qeued, we add his neighbor to the qeue, change qeued to true, and update that neighboors prior to be are current box.

This logic allows as to make sure that the prior for each node is updated to the first node that saw him as his neihboor, and because we consider the step between each
two nodes the same, when we will hit are target, we could follow back all priors and get the shortest path.

## A*
https://en.wikipedia.org/wiki/A*_search_algorithm
To implement the A* algorithem en externael library is used PriortyQueue().
Priority Queue is an extension of the queue with the following properties:
-An element with high priority is dequeued before an element with low priority.
-If two elements have the same priority, they are served according to their order in the queue
In the A star allgorithim the f_count is our priority.
