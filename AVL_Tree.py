class Node:

    def __init__(self, key):
        self.key=key
        self.left_kind=None
        self.right_kind=None
        self.parent=None
        self.height=0


class AVL_Baum:

    def __init__(self):
        self.root=None

    def heigh(self):
        pass

    def _add(self, ins):
        if not self.root:
            self.root = Node(ins)
        else:
            self.root = self.add(ins, self.root)

    def add(self, ins, node):

       if (ins < node.key):
            node.left_kind = self.add(ins, node.left_kind)

       elif(ins > node.key):
           node.right_kind = self.add(ins, node.left_kind)

        return node

    def balance(self, key):
        pass

    def L_Rotation(self):
        pass

    def R_Rotation(self):
        pass

    def inOrder(self):
        if self.left_kind:
            self.left_kind.inOrder()
        print(self.key)
        if self.right_kind:
            self.right_kind.inOrder()

root = Node(6)
root.add(5)
root.add(4)
root.add(7)
root.add(8)
root.add(10)
root.inOrder()