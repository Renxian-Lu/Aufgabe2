class Node:

    def __init__(self, key):
        self.key=key
        self.left_kind=None
        self.right_kind=None
        self.parent=None
        self.height=0


class AVL_Baum:

    def __init__(self, key):
        self.root= Node(key)


    def heigh(self, node):
        if(node is None):
            return
        else:
            return (1 + max(node.left_kind, node.right_kind))

    def add(self, p, root, ins):

       if(root == None):
           self.root = Node(ins)
       elif(ins < root.key):
            root.left_kind = self.add(root, root.left_kind, ins)
       elif(ins > root.key):
           root.right_kind = self.add(root, root.right_kind, ins)
       else:
           return False
        h = self.heigh(root)



    def balance(self, key):
        pass

    def L_Rotation(self, x):
        y = x.right_kind
        x.right_kind = y.left_kind
        if(y.left_kind != None):
            y.left_kind.parent = x
        y.parent = x.parent
        if(x.parent == None):
            self.root = y
        elif(x == x.parent.left_kind):
            x.parent.left_kind = y
        elif(x == x.parent.right_kind):
            x.parent.right_kind = y
        y.left_kind = x
        x.parent = y

    def R_Rotation(self, x):
        y = x.left_kind
        x.left_kind = y.right_kind
        if (y.right_kind != None):
            y.right_kind.parent = x
        y.parent = x.parent
        if (x.parent == None):
            self.root = y
        elif (x == x.parent.right_kind):
            x.parent.lright_kind = y
        elif (x == x.parent.left_kind):
            x.parent.left_kind = y
        y.right_kind = x
        x.parent = y

    def inOrder(self):
        if self.left_kind:
            self.left_kind.inOrder()
        print(self.key)
        if self.right_kind:
            self.right_kind.inOrder()

root = Node(6)
