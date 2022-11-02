# constructing a binary tree from the given inorder traversal
class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def _get_index(array, start, end, data):
    for idx in range(start, end + 1):
        if array[idx] == data:
            return idx


def build_tree_from_inorder_preorder(inorder, preorder, start, end):
    global current

    if start > end:
        return None

    tree = BinaryTree(preorder[current])
    current += 1

    if start == end:
        return tree

    inorder_idx = _get_index(inorder, start, end, tree.data)

    tree.left = build_tree_from_inorder_preorder(
        inorder, preorder, start, inorder_idx - 1
    )
    tree.right = build_tree_from_inorder_preorder(
        inorder, preorder, inorder_idx + 1, end
    )

    return tree


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
    btree = build_tree_from_inorder_preorder(inorder, preorder, 0, len(inorder) - 1)

    print("\nInorder Seq:\n", inorder)
    print("\nPreorder Seq:\n", preorder)
    print("\nInorder Traversal after recreating tree:")
    inorder_traversal(btree)

    inorder = [5, 6, 8, 9, 10, 11, 12]
    preorder = [10, 8, 5, 6, 9, 11, 12]

    current = 0
    btree = build_tree_from_inorder_preorder(inorder, preorder, 0, len(inorder) - 1)

    print("\n\nInorder Seq:\n", inorder)
    print("\nPreorder Seq:\n", preorder)
    print("\nInorder Traversal after recreating tree:")
    inorder_traversal(btree)
