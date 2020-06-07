class Node:

    def __init__(self, key):
        self.key=key
        self.left_kind=None
        self.right_kind=None
        self.parent=None
        self.height=0

    def add(self, ins):
        if ins == self.key:
            return False
        elif(ins < self.key):
            if self.left_kind == None:
                self.left_kind = Node(ins)
            else:
                self.left_kind.add(ins)
        else:
            if self.right_kind == None:
                self.right_kind = Node(ins)
            else:
                self.right_kind.add(ins)

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

class AVL_Baum:

    def __init__(self):
        self.root=None

root = Node(6)
root.add(5)
root.add(4)
root.add(7)
root.add(8)
root.add(10)
root.inOrder()