# Binary Tree

A tree whose elements have at most 2 children is called a binary tree. Since each element in a binary tree can have only 2 children, we typically name them the left and right child.

## Properties of binary tree

- Max no. of nodes at level l (if root level is 0) = $2^l$ (l-level)
- Max no. of nodes in a binary tree of height h = $2^h - 1 = 2^{h+1} - 1$ (if root level is 0)
- Binary tree with N nodes, min possible height or the min levels is = $Log_2(N+1)$
- Binary tree with h leaves has levels at least = $|Log_2L|+1$
- In a binary tree where every nodes has 0 or 2 children, no. of leaf nodes is always one more than nodes with 2 children.
- In a non-empty binary tree, if n is the total no. of nodes and e is the edges then $e = n-1$

## Types of Binary Trees

- Full Binary Tree - Each node has either two or no children.
- Complete Binary Tree - All the levels are completely filled except the last level and all the keys in the last level are as left as possible. A complete binary tree doesn't have to be a full binary tree.
- Perfect Binary Tree - All the internal nodes have two children and all the leaf nodes are at the same level. $(Leaf Nodes = Internal Nodes + 1)$
- Balanced Binary Tree - A binary tree is balanced if the height of the tree is $O(Log n)$, where n is the number of nodes.
- Degenerate Tree - Every internal node has one child. Such trees are performance-wise same as linked list. A degenerate or pathological tree is the tree having a single child either left or right.
- Skewed Binary Tree - A pathological/degenerate tree dominated by the left nodes or the right nodes. Thus, there are two types of skewed binary tree:
  - Left-Skewed Binary Tree
  - Right-Skewed Binary Tree.
