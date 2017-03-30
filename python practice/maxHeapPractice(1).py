# max heap implementation practice
import math

class MaxHeap ():

    def __init__(self):
        self.data=[]

    def getsize(self):
        return len(self.data)

    # for array A, compare ith element with its children, within range of 0~(length-1)th elements
    def compareAndSwap(self,i,A,length):

        # compute index of last leaf's parent (=last parent)
        lastParentIdx = int(length/2)-1

        # in case of i is larger than last parent index
        if (i > lastParentIdx):
            return None

        # compute left/right child index of ith element
        left = (i+1)*2-1
        right = (i+1)*2

        # index of larger child between left/right
        largerchild = -1

        # if ith element is last parent and tree's length is even, last leaf must be left child
        if (i == lastParentIdx and length%2 == 0):
            largerchild = left
        elif (A[left] > A[right]):
            largerchild = left
        else:
            largerchild = right

        # if value of larger child is larger than its parent, swap and return swapped location
        if (A[largerchild] > A[i]):
            (A[largerchild], A[i]) = (A[i], A[largerchild])
            return largerchild

        return None


    # do heapify (Max-heapify)
    def heapify(self,length):
        i=0 # start from root

        # compare ith element with its child and swap if larger child is also larger than parent.
        # and compare/swap again along swapped location, until reach its end continuously...
        while(i != None):
            i=self.compareAndSwap(i,self.data,length)


    # add value, attach data at last and then make heap from its parent to root
    def add(self,x):
        self.data.append(x)
        i = int(len(self.data) / 2) - 1  # parent index of last leaf

        for j in range(i, -1, -1):
            self.compareAndSwap(j,self.data,len(self.data))


    # remove (pop) max value (root) of heap
    def pop(self):
        last=len(self.data)

        # if heap is empty, return None
        if(last <= 0):
            print('no elements in heap')
            return None

        # if heap has only root, return root
        if(last == 1):
            return self.data[0]

        # swap root and last element, and Max-heapify execept swapped last one
        (self.data[0], self.data[last-1]) = (self.data[last-1], self.data[0])
        self.heapify(last-1)

        # return and remove last element (max value)
        return self.data.pop(last-1)


    # return sorted array (heat sort), swallow copy
    def sortedArray(self):
        if(len(self.data)<=0):
            print('no elements in heap')
            return

        output = self.data[:] # swallow copy to retain heat tree

        # for each loop, swap root and last element.
        # and then heapify swallow copied one, except swapped last element
        # do it continuously until sorted array completed
        for last in range(len(self.data)-1,-1,-1):
            (output[0],output[last])=(output[last],output[0])
            i=0
            while(i != None):
                i=self.compareAndSwap(i,output,(last))

        return output


    # print heap data as array
    def showArray(self):
         print(self.data)


    # print heap tree
    def showTree(self):
        if(len(self.data)<=0):
            print('no elements in heap')
            return

        length = len(self.data)
        totalRow = int(math.log2(length)) # total number of row(level) of tree. starting from 0


        for row in range(totalRow+1): # for each row (level)
            for i in range((2**row-1), 2**(row+1)-1): # deal each item in certain row(level)

                # if tree is not full binary tree, loop shall be stopped at last element
                if(i == (length)):
                    break

                reversedRow = totalRow-row # counting row number reversely.
                firstSpace = 2**reversedRow-1 # number of space characters at left end
                restSpace = 2**(reversedRow+1)-1 # number of space characters rest

                for fS in range(firstSpace):
                    print(' ',end='')

                print(self.data[i],end="")

                for rS in range(restSpace):
                    print(' ',end='')

            print('') # changing row


    # modify ith element of array as x, if user wants to change specific element in specific case
    def modifyArray(self,i,x):
        if(len(self.data)<=0):
            print('no elements in heap')
            return
        elif(i<0 or i>=len(self.data)):
            print('out of index range')
            return

        self.data[i]=x




# Max heap implementation test

print('create empty max heap instance : mh=MaxHeap()\n')
mh = MaxHeap()
print('trying sorting empty heap : mh.sortedArray()')
print(mh.sortedArray(),'\n')

print('add some elements : 5,3,6,1,2,4,0,4,9')
for i in [5,3,6,1,2,4,0,4,9]:
    mh.add(i)
mh.showArray()
mh.showTree()
print('number of total elements : ',mh.getsize())

print('\ntesting heap sort : mh.sortedArray()')
print(mh.sortedArray(),'\n')

print('testing heapify : change root as -9')
mh.showArray()
print('to')
mh.modifyArray(0,-9)
mh.showArray()
mh.showTree()

print('\nnow hepify : mh.heapify()')
mh.heapify(mh.getsize())
mh.showArray()
mh.showTree()

print('\nadd more elements : 89,0,-1,27,44')
for i in [89,0,-1,27,44]:
    mh.add(i)
mh.showArray()
mh.showTree()

print('\ntesting heap sort : mh.sortedArray()')
print(mh.sortedArray(),'\n')

mh.showArray()
print('pop max (root) test : mh.pop()')
print('popped value is : ',mh.pop())
print('after pop(), now heap is as below :')
mh.showArray()
mh.showTree()
