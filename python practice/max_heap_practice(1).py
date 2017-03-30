# max heap implementation practice
import math


class MaxHeap(object):

    def __init__(self):
        self.data = []

    def get_size(self):
        return len(self.data)

    # find parent index of last leaf (parent of last leaf = last parent)
    # compute by length of array (length)
    @staticmethod
    def get_last_parent(length):
        return int(length / 2) - 1

    # for array A, compare i'th (idx'th) element with its children, within range of 0~(length-1)th elements
    @staticmethod
    def compare_and_swap(idx, arr, length):

        # compute index of last leaf's parent (=last parent)
        last_parent_idx = MaxHeap.get_last_parent(length)

        # in case of idx is larger than last parent index
        if idx > last_parent_idx:
            return None

        # compute left/right child index of ith element
        left = (idx+1)*2-1
        right = (idx+1)*2

        # if idx'th element is last parent and tree's length is even, last leaf must be left child
        if idx == last_parent_idx and (length % 2) == 0:
            larger_child = left
        elif arr[left] > arr[right]:
            larger_child = left
        else:
            larger_child = right

        # if value of larger child is larger than its parent, swap and return swapped location
        if arr[larger_child] > arr[idx]:
            arr[larger_child], arr[idx] = arr[idx], arr[larger_child]
            return larger_child

        # in case any statement does not executed
        return None

    # heapify(max-heapify)
    def heapify(self,length):
        idx = 0  # start from root

        # compare ith element with its child and swap if larger child is also larger than parent.
        # and compare/swap again along swapped location, until reach its end continuously...
        while idx is not None:
            idx = MaxHeap.compare_and_swap(idx, self.data, length)

    # add value, attach data at last and then do heapify from its parent to root
    def add(self,value):
        self.data.append(value)
        length = self.get_size()
        parent_idx = MaxHeap.get_last_parent(length)

        for j in range(parent_idx, -1, -1):
            MaxHeap.compare_and_swap(j, self.data, len(self.data))

    # remove max value of heap (popping root)
    def pop(self):
        last = self.get_size()

        # if heap is empty, return None
        if last <= 0:
            print('no elements in heap')
            return None

        # if heap has only root, return root
        if last == 1:
            return self.data[0]

        # swap root and last element, and max-heapify except swapped last one
        self.data[0], self.data[last-1] = self.data[last-1], self.data[0]
        self.heapify(last-1)

        # return and remove last element (max value)
        return self.data.pop(last-1)

    # heat sort (return sorted array, swallow copied one)
    def sorted_array(self):
        length = self.get_size()
        if length <= 0:
            print('no elements in heap')
            return

        output = self.data[:]  # swallow copy to retain heat tree

        # for each loop, swap root and last element.
        # and then heapify swallow copied one, except swapped last element
        # do it continuously until sorted array completed
        for last in range(length-1, -1, -1):
            output[0], output[last] = output[last], output[0]
            idx = 0
            while idx is not None:
                idx = MaxHeap.compare_and_swap(idx, output, last)

        return output

    # print heap data as an array
    def show_array(self):
        print(self.data)

    # print heap tree
    def show_tree(self):
        if len(self.data) <= 0:
            print('no elements in heap')
            return

        length = len(self.data)
        total_row = int(math.log2(length))  # total number of row(level) of tree. starting from 0

        for row in range(total_row + 1):  # for each row (level)
            for i in range((2**row-1), 2**(row+1)-1):  # deal each item in certain row(level)

                # if tree is not full binary tree, loop shall be stopped at last element
                if i == length:
                    break

                reversed_row = total_row - row  # counting row number reversely.
                first_space = 2**reversed_row - 1  # number of space characters at left end
                rest_space = 2**(reversed_row+1) - 1  # number of space characters rest

                for fs in range(first_space):
                    print(' ', end='')

                print(self.data[i], end='')

                for rs in range(rest_space):
                    print(' ', end='')

            print('')  # changing row

    # modify idx'th element of array as x, if user wants to change specific element in specific case
    def modify_array(self, idx, x):
        length = self.get_size()

        if length <= 0:
            print('no elements in heap')
            return
        elif idx < 0 or idx >= length:
            print('out of index range')
            return

        self.data[idx] = x


# Max heap implementation test
# uncomment each line to test
#
# print('create empty max heap instance : mh=MaxHeap()\n')
# mh = MaxHeap()
# print('trying sorting empty heap : mh.sorted_array()')
# print(mh.sorted_array(), '\n')
#
# print('add some elements : 5,3,6,1,2,4,0,4,9')
# for idx in [5, 3, 6, 1, 2, 4, 0, 4, 9]:
#     mh.add(idx)
# mh.show_array()
# mh.show_tree()
# print('number of total elements : ', mh.get_size())
#
# print('\ntesting heap sort : mh.sorted_array()')
# print(mh.sorted_array(), '\n')
#
# print('testing heapify : change root as -9')
# mh.show_array()
# print('to')
# mh.modify_array(0, -9)
# mh.show_array()
# mh.show_tree()
#
# print('\nnow heapify : mh.heapify()')
# mh.heapify(mh.get_size())
# mh.show_array()
# mh.show_tree()
#
# print('\nadd more elements : 89,0,-1,27,44')
# for idx in [89, 0, -1, 27, 44]:
#     mh.add(idx)
# mh.show_array()
# mh.show_tree()
#
# print('\ntesting heap sort : mh.sorted_array()')
# print(mh.sorted_array(), '\n')
#
# mh.show_array()
# print('pop max (root) test : mh.pop()')
# print('popped value is : ', mh.pop())
# print('\nafter pop(), now heap is as below :')
# mh.show_array()
# mh.show_tree()
