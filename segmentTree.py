import math

class SegmentTree:
    def __init__(self,arr):
        height = math.ceil(math.log(len(arr),2))
        self.max_size = int(2*pow(2,height)-1)
        self.st = [None for i in range(self.max_size)]
        self.constructST(arr,0,len(arr)-1,self.st,0)
#        for a in reversed(self.st):
#            if a is None:
#                self.st.remove(a)
#
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
        print 'the set of ss,se,qs,qe and index are: ', ss, se,qs,qe,index
        if qs<=ss and qe>=se:
            return st[index]
        elif se < qs or ss >qe:
            infinity = float("inf")
            return infinity
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

arr = [1,3,2,7,9,11]
arrSegTree = SegmentTree(arr)
print arrSegTree.st
print arrSegTree.RMQreturn(6,1,5)
