class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


if __name__ == "__main__":
    # creating a sample tree below
    #          1
    #        /  \
    #       2    3
    #      /
    #     4

    btree = Node(1)

    btree.left = Node(2)
    btree.right = Node(3)

    btree.left.left = Node(4)

# * Properties of binary tree
# 1. Max no. of nodes at level l (if root level is 0) = 2^l (l-level)
# 2. Max no. of nodes in a binary tree of height h = 2^h - 1 = 2^(h+1) - 1 (if root level is 0)
# 3. Binary tree with N nodes, min possible height or the min levels is = Log_2(N+1)
# 4. Binary tree with h leaves has levels at least = |Log_2L|+1
# 5. In a binary tree where every nodes has 0 or 2 children, no. of leaf nodes is always one more than nodes with 2 children.
# 6. In a non-empty binary tree, if n is the total no. of nodes and e is the edges then e = n-1
