class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self.recursive_insert(self.root, value)

    def recursive_insert(self, node, value):
        if value < node.value:
            if not node.left:
                node.left = Node(value)
            else:
                self.recursive_insert(node.left, value)
        else:
            if not node.right:
                node.right = Node(value)
            else:
                self.recursive_insert(node.right, value)

    def display_inorder(self):
        self.display_recursive_inorder(self.root)

    def display_recursive_inorder(self, node):
        if node:
            self.display_recursive_inorder(node.left)
            print(node.value, end=' ')
            self.display_recursive_inorder(node.right)

if __name__ == '__main__':
    cool_tree = BinarySearchTree()
    cool_tree.insert(5)
    cool_tree.insert(3)
    cool_tree.insert(7)
    cool_tree.insert(2)
    cool_tree.insert(4)
    cool_tree.display_inorder()