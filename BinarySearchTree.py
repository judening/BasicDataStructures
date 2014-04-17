class Node:
    def __init__(self, val):
        self.left_child = None
        self.right_child = None
        self.data = val
        
    def insert(root,node):
        if root is None:
            root = node
        else:
            if root.data > node.data:
                if root.left_child == None:
                    root.left_child = node
                else:
                    insert(root.left_child, node)
            else:
                if root.right_child == None:
                    root.right_child = node
                else:
                    insert(root.right_child, node)
                    
    
