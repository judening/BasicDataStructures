class Node:
    def __init__(self, val):
        self.left_child = None
        self.right_child = None
        self.data = val
        self.depth = 0
        
def insert(root,node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.left_child is None:
                root.left_child = node
                root.left_child.depth = root.depth+1
            else:
                insert(root.left_child, node)
        else:
            if root.right_child is None:
                root.right_child = node
                root.right_child.depth = root.depth+1
            else:
                insert(root.right_child, node)
    
#Python has class problem
def delete(root,node,parent,direction):
    if root is None:
        return False
    else:
        if root.data > node.data:
            if root.left_child is None:
                return False
            else:
                delete(root.left_child, node, root, 0)
        elif root.data < node.data:
            if root.right_child is None:
                return False
            else:
                delete(root.right_child, node, root, 1)
        else:
            if(root.left_child is None and root.right_child is None):
                if direction == 0:
                    parent.left_child = None
                elif direction == 1:
                    parent.right_child = None
                else:
                    root = None
                return True
            elif (root.left_child is None and root.right_child is not None):
                to_replace, to_replace_parent = find_smallest(root.right_child), root
                i = 0
                if to_replace.data == to_replace_parent.right_child.data:
                    i = 1
                #I gotta give the tuple unpacking some credits, so damn easy
                root.data, to_replace.data = to_replace.data, root.data
                if i==0 :
                    to_replace_parent.left_child = None
                else:
                    to_replace_parent.right_child = None
                return root
            else:
                to_replace, to_replace_parent = find_smallest(root.left_child), root
                i = 0
                if to_replace.data == to_replace_parent.right_child.data:
                    i = 1
                #I gotta give the tuple unpacking some credits, so damn easy
                root.data, to_replace.data = to_replace.data, root.data
                if i==0 :
                    to_replace_parent.left_child = None
                else:
                    to_replace_parent.right_child = None
                return root
                    
#The one to replace/swap is always the left child or the smallest of right sub tree            
def find_smallest(root):
    if root is None:
        return None
    else:
        if root.left_child is not None:
            return find_smallest(root.left_child)
        else:
            return root

def search(root,node):
    if root is None:
        return None
    else:
        if (root.data > node.data):
            return search(root.left_child, node)
        elif (root.data < node.data):
            return search(root.right_child,node)
        else:
            return root

def bfs_queue(root):
    queue = []
    dic = {}
    bfs_print(root,queue,dic)
    print(dic)
    
# can use an iterator (yield) instead
def bfs_print(root, queue, dic):
    if root is None:
        return
    else:
        queue.append(root)
        if dic.get(root.depth) is None:
            dic[root.depth] = [root.data]
        else:
            dic[root.depth].append(root.data)
        if root.left_child is not None:
            queue[-1] = root.left_child
        if root.right_child is not None:
            queue[-1] = root.right_child
        bfs_print(root.left_child,queue,dic)
        bfs_print(root.right_child,queue,dic)
    
