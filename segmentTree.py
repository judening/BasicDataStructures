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

        mid = self.getMid(ss,se)
        print 'the set of mid,ss,se,si,left,right index are: ', mid,ss,se,si,si*2+1, si*2+2
        if ss == se:
            st[si] = arr[ss]
            return arr[ss]

        #Parent node is the minimum of given range
        st[si] = min(self.constructST(arr,ss,mid,st,si*2+1), self.constructST(arr,mid+1,se,st,si*2+2))

        return st[si]

    def RMQreturn(self,st,ss,se,qs,qe,index):
        if qs<=ss and qe>=se:
            return st[index]
        else:
            return min(self.RMQreturn(st,ss,mid,qs,qe,2*index+1),self.RMQreturn(st,mid+1,se,qs,qe,2*index+2))


#Testing

arr = [2,5,1,4,9,3]
arrSegTree = SegmentTree(arr)
print arrSegTree.st
