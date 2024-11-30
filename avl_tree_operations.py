class Node:
    def __init__(self, key):
        """Create a node with a given key."""
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # Initially, the height of the node is 1

class AVLTree:
    def __init__(self):
        """Initialize an empty AVL Tree."""
        self.root = None

    def get_height(self, node):
        """Get the height of a node."""
        if not node:
            return 0
        return node.height

    def get_balance_factor(self, node):
        """Get the balance factor of a node."""
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, y):
        """Perform a right rotation on the given node."""
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1

        return x  # Return new root

    def left_rotate(self, x):
        """Perform a left rotation on the given node."""
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1

        return y  # Return new root

    def insert(self, node, key):
        """Insert a new key into the AVL tree and balance it."""
        # Perform the normal BST insert
        if not node:
            return Node(key)

        if key < node.key:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)

        # Update height of this ancestor node
        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1

        # Get the balance factor of this ancestor node to check whether it became unbalanced
        balance = self.get_balance_factor(node)

        # Left Left Case
        if balance > 1 and key < node.left.key:
            return self.right_rotate(node)

        # Right Right Case
        if balance < -1 and key > node.right.key:
            return self.left_rotate(node)

        # Left Right Case
        if balance > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Right Left Case
        if balance < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        # Return the (unchanged) node pointer
        return node

    def inorder(self, root):
        """Inorder traversal of the AVL tree."""
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    def delete(self, node, key):
        """Delete a key from the AVL tree and balance it."""
        # Step 1: Perform the normal BST delete
        if not node:
            return node

        if key < node.key:
            node.left = self.delete(node.left, key)
        elif key > node.key:
            node.right = self.delete(node.right, key)
        else:
            # Node to be deleted is found
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            # Node with two children, get the inorder successor (smallest in the right subtree)
            temp = self.get_min_value_node(node.right)
            node.key = temp.key
            node.right = self.delete(node.right, temp.key)

        # Step 2: Update height of the current node
        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1

        # Step 3: Get the balance factor of the current node and balance the tree
        balance = self.get_balance_factor(node)

        # Left Left Case
        if balance > 1 and self.get_balance_factor(node.left) >= 0:
            return self.right_rotate(node)

        # Right Right Case
        if balance < -1 and self.get_balance_factor(node.right) <= 0:
            return self.left_rotate(node)

        # Left Right Case
        if balance > 1 and self.get_balance_factor(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Right Left Case
        if balance < -1 and self.get_balance_factor(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def get_min_value_node(self, node):
        """Get the node with the minimum value (leftmost node)."""
        current = node
        while current.left:
            current = current.left
        return current

# Example usage
if __name__ == "__main__":
    avl_tree = AVLTree()

    # Insert nodes into the AVL tree
    root = None
    values = [20, 4, 15, 70, 50, 100, 10, 8, 30]
    for value in values:
        root = avl_tree.insert(root, value)

    print("Inorder Traversal after insertions:")
    avl_tree.inorder(root)  # Output should be in sorted order
    print()

    # Delete a node
    root = avl_tree.delete(root, 70)
    print("Inorder Traversal after deletion of 70:")
    avl_tree.inorder(root)
    print()

    # Delete another node
    root = avl_tree.delete(root, 20)
    print("Inorder Traversal after deletion of 20:")
    avl_tree.inorder(root)
    print()
