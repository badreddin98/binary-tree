# Binary Tree Traversal Implementation

This is my solution for BE Module 12 Lesson 7 Assignment focusing on Binary Tree Traversal algorithms.

## Problem Statement

Implement and understand different tree traversal algorithms using a binary tree data structure.

The binary tree structure used in this implementation:

```
                  50
           ┌─────┴─────┐
          30           70
     ┌────┴────┐    ┌────┴────┐
    40       20   60         80
```

## Tasks Completed

1. Implemented in-order traversal algorithm (left -> root -> right)
2. Implemented pre-order traversal algorithm (root -> left -> right)
3. Implemented post-order traversal algorithm (left -> right -> root)
4. Created test cases to demonstrate all traversal methods

## Expected Outputs

- In-order traversal: 40 30 20 50 60 70 80
- Pre-order traversal: 50 30 40 20 70 60 80
- Post-order traversal: 40 20 30 60 80 70 50

## How to Run

Simply run the Python file:
```bash
python binary_tree.py
```
