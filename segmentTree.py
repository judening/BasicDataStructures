import math

class SegmentTree:
    def __init__(self,arr):
        height = math.ceil(math.log(len(arr),2))
        self.max_size = int(2*pow(2,height)-1)
        self.st = [None for i in range(self.max_size)]
        self.constructST(arr,0,len(arr)-1,self.st,0)

    def getMid(self,s,e):
        return s+(e-s)/2

    def constructST(self,arr,ss,se,st,si):
        if ss == se:
            st[si] = arr[ss]
            return arr[ss]
        mid = self.getMid(ss,se)
        #Parent node is the minimum of given range
        st[si] = min(self.constructST(arr,ss,mid,st,si*2+1), self.constructST(arr,mid+1,se,st,si*2+2))
        return st[si]

    def RMQreturnUtil(self,st,ss,se,qs,qe,index):
        #This might be a bit hard to understand, but ss and se represents the staring index and ending
        #index of a node given. It has nothing to do with the length of st, which confused me at first.
        #If condition is met, it means that the ss-se interval is within the inquired range qs-qe.
        #Thus, this node must have been the smallest node given the way we construct them
        if qs<=ss and qe>=se:
            return st[index]
        elif se < qs or ss >qe:
            infinity = float("inf")
            return infinity
        #If parts of it overlaps, keep shrinking the intervals
        else:
            mid = self.getMid(ss,se)
            return min(self.RMQreturnUtil(st,ss,mid,qs,qe,2*index+1),self.RMQreturnUtil(st,mid+1,se,qs,qe,2*index+2))

    def RMQreturn(self,n,qs,qe):
        if qs <0 or qe > n-1 or qs>qe:
            print "invalid input"
            return -1
        else:
            return self.RMQreturnUtil(self.st,0,n-1,qs,qe,0)

#Testing

arr = [2,5,1,4,9,3]
arrSegTree = SegmentTree(arr)
print "The array representation of the segment tree is",arrSegTree.st
print
print "The minimum value between index 1 to 5 of", arr, "is",arrSegTree.RMQreturn(6,1,5)
