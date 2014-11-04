class SegmentTree:
    def __init__(self,arr):
        max_size = 2*len(arr)-1
        self.st = [None for i in range(max_size)]
        self.constructST(arr,0,len(arr),self.st,0)

    def getMid(self,s,e):
        return s+(e-s)/2

    def constructST(self,arr,ss,se,st,si):
        if ss == se:
            st[si] = arr[ss]
            return arr[ss]

        mid = getMid(ss,se)
        #Parent node is the minimum of given range
        st[si] = min(self.constructST(arr,ss,mid,st,si*2+1), self.constructST(arr,mid+1,se,st,si*2+2))

        return st[si]

    def RMQreturn(self,st,ss,se,qs,qe,index):
        if qs<=ss and qe>=se:
            return st[index]


