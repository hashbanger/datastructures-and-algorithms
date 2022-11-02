# constructing a binary tree from the given inorder and preorder traversal, with using hashing.
class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_tree_from_inorder_preorder(inorder, preorder, start, end):
    global current, index_map

    if start > end:
        return None

    # creating a tree node from the first element of the preorder
    tree = BinaryTree(preorder[current])
    current += 1

    # if there are no children then return the node
    if start == end:
        return tree

    # otherwise find it's position in the inorder sequence
    inorder_idx = index_map[tree.data]

    # build the left subtree recursively from all the elements to its left in inorder sequence
    tree.left = build_tree_from_inorder_preorder(
        inorder, preorder, start, inorder_idx - 1
    )

    # build the right subtree recursively from all the elements to its right in inorder sequence
    tree.right = build_tree_from_inorder_preorder(
        inorder, preorder, inorder_idx + 1, end
    )

    return tree


def build_tree(inorder, preorder, start, end):
    global index_map

    # creating the hashmap to find the indexes in preorder quicker
    for i in range(start, end + 1):
        index_map[inorder[i]] = i

    return build_tree_from_inorder_preorder(inorder, preorder, start, end)


def inorder_traversal(tree):
    if tree is None:
        return

    # recursively visit the left child until its None
    inorder_traversal(tree.left)

    # output the root value
    print(tree.data, end=" ")

    # recursively visit the right child until its None
    inorder_traversal(tree.right)


if __name__ == "__main__":
    inorder = [2, 4, 10, 12, 15, 18, 22, 24, 25, 31, 35, 44, 50, 66, 70, 90]
    preorder = [25, 15, 10, 4, 2, 12, 22, 18, 24, 50, 35, 31, 44, 70, 66, 90]

    current = 0
    index_map = {}
    btree = build_tree(inorder, preorder, 0, len(inorder) - 1)

    print("\nInorder Seq:\n", inorder)
    print("\nPreorder Seq:\n", preorder)
    print("\nInorder Traversal after recreating tree:")
    inorder_traversal(btree)

    inorder = [5, 6, 8, 9, 10, 11, 12]
    preorder = [10, 8, 5, 6, 9, 11, 12]

    current = 0
    index_map = {}
    btree = build_tree(inorder, preorder, 0, len(inorder) - 1)

    print("\n\nInorder Seq:\n", inorder)
    print("\nPreorder Seq:\n", preorder)
    print("\nInorder Traversal after recreating tree:")
    inorder_traversal(btree)
