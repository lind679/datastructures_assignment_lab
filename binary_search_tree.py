class Node:
    def __init__(self, key):
        """Create a node with a given key."""
        self.left = None
        self.right = None
        self.value = key

class BinarySearchTree:
    def __init__(self):
        """Initialize an empty BST."""
        self.root = None

    def insert(self, root, key):
        """Insert a new node with the given key into the BST."""
        if root is None:
            return Node(key)
        else:
            if key < root.value:
                root.left = self.insert(root.left, key)  # Insert in left subtree
            else:
                root.right = self.insert(root.right, key)  # Insert in right subtree
        return root

    def search(self, root, key):
        """Search for a node with the given key in the BST."""
        if root is None or root.value == key:
            return root
        if key < root.value:
            return self.search(root.left, key)  # Search in left subtree
        return self.search(root.right, key)  # Search in right subtree

    def find_min(self, root):
        """Find the node with the minimum key."""
        current = root
        while current.left is not None:
            current = current.left
        return current

    def find_max(self, root):
        """Find the node with the maximum key."""
        current = root
        while current.right is not None:
            current = current.right
        return current

    def delete(self, root, key):
        """Delete a node with the given key from the BST."""
        if root is None:
            return root
        if key < root.value:
            root.left = self.delete(root.left, key)  # Delete from left subtree
        elif key > root.value:
            root.right = self.delete(root.right, key)  # Delete from right subtree
        else:
            # Node to be deleted is found
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node has two children: Get the inorder successor (smallest in the right subtree)
            min_node = self.find_min(root.right)
            root.value = min_node.value  # Replace the value with the inorder successor
            root.right = self.delete(root.right, min_node.value)  # Delete the inorder successor

        return root

    def inorder(self, root):
        """Inorder traversal of the BST."""
        if root:
            self.inorder(root.left)
            print(root.value, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        """Preorder traversal of the BST."""
        if root:
            print(root.value, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        """Postorder traversal of the BST."""
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.value, end=" ")

# Example usage
if __name__ == "__main__":
    bst = BinarySearchTree()
    root = None

    # Insert elements into the BST
    values = [20, 8, 22, 4, 12, 10, 14]
    for value in values:
        root = bst.insert(root, value)

    print("Inorder Traversal:")
    bst.inorder(root)  # Output: 4 8 10 12 14 20 22
    print()

    print("Preorder Traversal:")
    bst.preorder(root)  # Output: 20 8 4 12 10 14 22
    print()

    print("Postorder Traversal:")
    bst.postorder(root)  # Output: 4 10 14 12 8 22 20
    print()

    # Search for a node
    key = 10
    result = bst.search(root, key)
    if result:
        print(f"Node with value {key} found!")
    else:
        print(f"Node with value {key} not found.")

    # Find the minimum and maximum nodes
    min_node = bst.find_min(root)
    max_node = bst.find_max(root)
    print(f"Minimum value in the BST: {min_node.value}")
    print(f"Maximum value in the BST: {max_node.value}")

    # Delete a node
    key_to_delete = 12
    root = bst.delete(root, key_to_delete)
    print(f"Deleted node {key_to_delete}. Inorder Traversal after deletion:")
    bst.inorder(root)  # Output: 4 8 10 14 20 22
    print()
