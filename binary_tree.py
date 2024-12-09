class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def inorder_traversal(self, node):
        """Task 1: Implement in-order traversal (left -> root -> right)"""
        if node:
            # Traverse left subtree
            self.inorder_traversal(node.left)
            # Visit the root
            print(node.value, end=' ')
            # Traverse right subtree
            self.inorder_traversal(node.right)

    def preorder_traversal(self, node):
        """Task 2: Implement pre-order traversal (root -> left -> right)"""
        if node:
            # Visit the root
            print(node.value, end=' ')
            # Traverse left subtree
            self.preorder_traversal(node.left)
            # Traverse right subtree
            self.preorder_traversal(node.right)

    def postorder_traversal(self, node):
        """Task 3: Implement post-order traversal (left -> right -> root)"""
        if node:
            # Traverse left subtree
            self.postorder_traversal(node.left)
            # Traverse right subtree
            self.postorder_traversal(node.right)
            # Visit the root
            print(node.value, end=' ')

# Task 4: Test the traversal algorithms
def main():
    # Create binary tree
    tree = BinaryTree()
    tree.root = Node(50)
    tree.root.left = Node(30)
    tree.root.right = Node(70)
    tree.root.left.left = Node(40)
    tree.root.left.right = Node(20)
    tree.root.right.left = Node(60)
    tree.root.right.right = Node(80)

    # Test all traversal methods
    print("\nIn-order traversal:")
    tree.inorder_traversal(tree.root)  # Expected: 40 30 20 50 60 70 80

    print("\nPre-order traversal:")
    tree.preorder_traversal(tree.root)  # Expected: 50 30 40 20 70 60 80

    print("\nPost-order traversal:")
    tree.postorder_traversal(tree.root)  # Expected: 40 20 30 60 80 70 50
    print()

if __name__ == "__main__":
    main()
