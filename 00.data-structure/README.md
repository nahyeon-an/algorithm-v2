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

