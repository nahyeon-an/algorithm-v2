# Data Structure  

## What is a Data Structure?  
A data structure is a way of organizing data  
so that it can be used effectively.  

## Why Data Structure?  
1. essential ingredients in creating efficient algorithms  
2. manage and organize data  
3. code will be cleaner and easier to understand  

## Abastract Data Type vs. Data Structure  

### Abstract Data Type (ADT)  
An abstract data type is an abstraction of a data structure  
which provides only the interface to which a data structure must adhere to.  

- the interface does not give any specific details  
- about how something should be implemented or 
- in what programming language

Examples (Abstraction : Implementation)  
- List : Dynamic Array, Linked List
- Queue : Linked List, Array, Stack
- Map : Hash Table/Map, Tree  

## Big-O Notation  
Big-O notation gives an upper bound of the complexity in the worst case,  
helping to quantify performance  
as the input size becomes arbitrarily large.  

- Constant Time : O(1)
- Logarithmic Time : O(log n)
- Linear Time : O(n)
- Linearithmic Time : O(n log n)
- Quadratic Time : O(n^2)
- Cubic Time : O(n^3)
- Exponential Time : O(2^n)  
- Factorial Time : O(n!)  

## What is a static Array?
A static array is a fixed length container  
containing n elements indexable from the range [0, n-1]  

What is being 'indexable'?
- each slot/index can be referenced with a number  

When and Where is a static Array used?
- storing and accessing sequential data
- buffers used by IO routines

## What is a dynamic Array?
A dynamic array can grow and shrink in size  

## What is a Linked List?  
A linked list is a sequential list of nodes  
that hold data which point to other nodes containing data.  

Where are linked lists used?  
- List, Queue and Stack implementation  
- circular lists
- Hashtable implementation  

Terminology
- Head : The first node in a linked list  
- Tail : The last node in a linked list  
- Pointer : Reference to another node  
- Node : An object containing data and pointer  

Singly Linked Lists  
- hold a reference to the next node  

Doubly Linked Lists  
- hold a reference to the next node and previous node  
- pros : can be traversed backwards  

## What is a Stack?  
A stack is a one-ended linear data structure  
which models a real world stack  
by having 2 primary operations, push and pop.  
(LIFO)

When and where is a stack used?  
- undo mechanism  
- compiler syntax checking  
- DFS  
- tower of hanoi  

## What is a Queue?  
A queue is a linear data structure  
which models a real world queue  
by having 2 primary operations, enqueue and dequeue.  

When and where is a queue used?  
- recently added elements  
- serve request management  
- BFS  

## What is a Priority Queue?  
A priority queue is an Abstract Data Type  
that operates similar to a queue  
except that each element has a certain priority.  
The priority determines the order in which elements are removed from the Priority Queue.  
Priority queues only support comparable data.  

## What is a Heap?  
A heap is a tree based data structure  
that satisfies the heap invariant (heap property)  
- max / min heap  

When and where is a priority queue used?  
- dijkstra's shortest path algorithm  
- A* BFS  
- MST algorithms  

Binary Heap  
- construction : O(n)  

### Turning Min PA into Max PQ  
comparator, comparator with negation   

### Adding Elements to Binary Heap  

### How to Implement a Priority Queue  
Priority queues are usually implemented with heaps  
- the best possible time complexity  
- heaps are not the only way to implement PQ  

Many types of heaps  
- binary, fibonacci, binomial, pairing heap  

A binary heap is a binary tree that supports the heap invariant.  
- every node has exactly two children  

A complete binary tree is a tree  
in which at every level except the last is completely filled   
and all the nodes are as far left as possible.  

### Removing Elements From Binary Heap in O(log(n))  
The inefficiency comes from performing a linear search   
to find out where an element is indexed at.  
=> What if using a Hashtable to find out where a node is indexed at?  

Multiple value problem : one value to multiple positions  
- Use a Set or Tree Set of indexes for which a value maps to  