class Node:
    def __init__(self, data):
        self.left_child = None
        self.right_child = None
        self.data = data
        self.depth = 0

    def insert(self,data):
        if self.data > data:
            if self.left_child is None:
                self.left_child = Node(data)
                self.left_child.depth = self.depth+1
            else:
                self.left_child.insert(data)
        else:
            if self.right_child is None:
                self.right_child = Node(data)
                self.right_child.depth = self.depth+1
            else:
                self.right_child.insert(data)

    #Parent is default as None if it's not given
    def search(self,data,parent=None):
        if (self.data > data):
            if self.left_child is not None:
                return self.left_child.search(data,self)
            return None,None
        elif (self.data < data):
            if self.right_child is not None:
                return self.right_child.search(data,self)
            return None,None
        else:
            return self,parent

    #The one to replace/swap is always the left child or the smallest of right sub tree
    def find_smallest(self,parent):
        if self.left_child:
            return self.left_child.find_smallest(self)
        else:
            return self,parent

    #The default value of direction is None
    #The whole point of setting direction is to know which child to delete.
    #During the process of searching, we will lose track of going left / right if we don't make a flag
    #Instead of searching thru in the delete method, why don't you do that in the search method?
    #Not only does it reduce the duplicate, but looks more elegant
    def delete(self,data):

        node,parent = self.search(data)

        if node is None:
            return False

        if(node.left_child is None and node.right_child is None):
            if parent:
                if parent.left_child is node:
                    parent.left_child = None
                else:
                    parent.right_child = None
            del node
            return True

        elif (node.left_child is not None and node.right_child is not None):
            to_replace, to_replace_parent = self.right_child.find_smallest(node)
            flag = 0
            if to_replace is to_replace_parent.right_child:
                flag = 1
                #I gotta give the tuple unpacking some credits, so damn easy
            node.data, to_replace.data = to_replace.data, node.data
            if flag==0 :
                to_replace_parent.left_child = None
            else:
                to_replace_parent.right_child = None
            return True
        elif (node.left_child is None and node.right_child is not None):
            to_replace, to_replace_parent = node.right_child, parent
            flag = 0
            if to_replace is to_replace_parent.right_child:
                flag = 1
            node.data, to_replace.data = to_replace.data, node.data
            if flag==0 :
                to_replace_parent.left_child = None
            else:
                to_replace_parent.right_child = None
            return True
        else:
            to_replace, to_replace_parent = node.left_child, parent
            flag = 0
            if to_replace is to_replace_parent.right_child:
                flag = 1
            node.data, to_replace.data = to_replace.data, node.data
            if flag==0 :
                to_replace_parent.left_child = None
            else:
                to_replace_parent.right_child = None
            return True


    def inorderTraversal(self,queue):
        if self is not None:
            if self.left_child is not None:
                self.left_child.inorderTraversal(queue)
            queue.append(self.data)
            if self.right_child is not None:
                self.right_child.inorderTraversal(queue)

    def preorderTraversal(self,queue):
        if self is not None:
            queue.append(self.data)
            if self.left_child is not None:
                self.left_child.preorderTraversal(queue)
            if self.right_child is not None:
                self.right_child.preorderTraversal(queue)

    def postorderTraversal(self,queue):
        if self is not None:
            if self.left_child is not None:
                self.left_child.postorderTraversal(queue)
            if self.right_child is not None:
                self.right_child.postorderTraversal(queue)
            queue.append(self.data)

    #There really isn't many meanings to do bfs using recursion
    def bfsTraversal(self,queue):
        if self is not None:
            if self.left_child is not None:
                queue.append(self.left_child)
            if self.right_child is not None:
                queue.append(self.right_child)
            if len(queue) >1:
                queue[0].bfsTraversal(queue[1:])

def bfs_queue(root):
    queue = []
    dic = {}
    bfs_print(root,queue,dic)
    print(dic)

# can use an iterator (yield) instead
def bfs_print(root):
    queue = []
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

bst = Node(10)
bst.insert(9)
bst.insert(11)
bst.insert(7.5)
bst.insert(9.5)
bst.insert(9.25)
bst.insert(9.75)
bst.insert(10.5)
bst.insert(11.5)
queueOne = []
bst.inorderTraversal(queueOne)
print queueOne
bst.delete(10)
queue = []
anotherQueue = []
bst.inorderTraversal(queue)
#bst.bfsTraversal(anotherQueue)
print queue
#for node in anotherQueue:
#    print node.data
