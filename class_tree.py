class Node:
    def __init__(self, x):
        self.left = None
        self.right = None
        self.id = x


class Tree:
    def __init__(self, x=None):
        self.root = Node(x)

#    TODO: fix tree representation
    def printTree(self):
        """function represents the whole tree with data in left and tight nodes"""

        if self.root is not None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node is not None:
            self._printTree(node.left)
            print(str(node.id) + ' ')
            self._printTree(node.right)


    def insert(self, x):
        """public method to insert a value into the tree"""

        if self.root is None:
            self.root = Node(x)
        else:
            self._insert(x, self.root)

    def _insert(self, x, root):
        """privet method that compare data in nodes and choose following direction"""

        if x < root.id:
            if root.left is None:
                root.left = Node(x)
            else:
                self._insert(x, root.left)
        else:
            if root.right is None:
                root.right = Node(x)
            else:
                self._insert(x, root.right)

    def find(self, x):
        if self.root is not None:
            return self._find(x, self.root)
        else:
            return None

#    TODO: "fix stuff with returning object"
    def _find(self, x, node):
        if x == node.id:
            return node
        elif x < node.id and node.left is not None:
            self._find(x, node.left)
        elif node.right is not None:
            self._find(x, node.right)
        else:
            return print('not in tree')



if __name__ == '__main__':
    t = Tree(3)
    t.insert(4)
    t.insert(0)
    t.insert(8)
    a = t.find(0)