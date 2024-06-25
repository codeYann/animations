class Node:
    def __init__(self, key: str) -> None:
        self.left = None
        self.right = None
        self.key = key


class Tree:
    def __init__(self) -> None:
        self.root = None

    def _insert(self, current_node: Node, key: str) -> None:
        if int(key) < int(current_node.key):
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert(current_node.left, key)
        elif int(key) > int(current_node.key):
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert(current_node.right, key)

    def _process(self, root: Node, cb) -> None:
        cb(root)

    def insert(self, key: str) -> None:
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def inorder_traversal(self, root: Node, cb, fn) -> None:

        if not root:
            return
        fn(root)
        self.inorder_traversal(root.left, cb, fn)
        self._process(root, cb)
        self.inorder_traversal(root.right, cb, fn)
