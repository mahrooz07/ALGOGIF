class Node:
    """A class representing a node in a binary tree."""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    """Binary Tree implementation."""
    def __init__(self):
        self.root = None

    def insert(self, data):
        """Insert a node into the binary tree."""
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, current, data):
        """Recursive helper to insert data into the tree."""
        if data < current.data:
            if current.left is None:
                current.left = Node(data)
            else:
                self._insert_recursive(current.left, data)
        else:
            if current.right is None:
                current.right = Node(data)
            else:
                self._insert_recursive(current.right, data)

    def delete(self, data):
        """Delete a node from the binary tree."""
        self.root, deleted = self._delete_recursive(self.root, data)
        return deleted

    def _delete_recursive(self, node, data):
        """Recursive helper to delete a node."""
        if node is None:
            return node, False

        if data < node.data:
            node.left, deleted = self._delete_recursive(node.left, data)
        elif data > node.data:
            node.right, deleted = self._delete_recursive(node.right, data)
        else:  # Node to be deleted found
            if node.left is None:
                return node.right, True
            elif node.right is None:
                return node.left, True

            # Node with two children
            min_larger_node = self._find_min(node.right)
            node.data = min_larger_node.data
            node.right, _ = self._delete_recursive(node.right, min_larger_node.data)
            return node, True

        return node, deleted

    def _find_min(self, node):
        """Find the smallest value in the subtree."""
        while node.left:
            node = node.left
        return node

    def inorder_traversal(self):
        """Perform an in-order traversal of the tree."""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        """Recursive helper for in-order traversal."""
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.data)
            self._inorder_recursive(node.right, result)
