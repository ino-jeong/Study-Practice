# binary search tree implementation practice

import queue_practice
import stack_practice


class Node(object):
    def __init__(self, parent, value):
        self.parent = parent
        self.left = None
        self.right = None
        self.value = value


class BST(object):

    def __init__(self):
        self.head = None

    def add(self, value):
        if self.head is None:
            self.head = Node(None, value)
            return

        current = self.head
        previous = None

        while current is not None:
            if current.value >= value:
                previous = current
                current = current.left
            else :
                previous = current
                current = current.right

        new_node = Node(previous, value)
        if previous.value >= value:
            previous.left = new_node
        else :
            previous.right = new_node

    def search(self, value, node):
        if node is None:
            print('no node with value %d' % value)
            return

        elif node.value == value:
            print('found %d' % value)
            return

        if node.value >= value:
            self.search(value, node.left)
        else:
            self.search(value, node.right)

    def minimum(self, node):
        if node.left is None:
            return node.value

        return self.minimum(node.left)

    def maximum(self, node):
        if node.right is None:
            return node.value

        return self.maximum(node.right)

    def pre_order(self, node):
        if node is None:
            return

        print(node.value)
        self.pre_order(node.left)
        self.pre_order(node.right)
        return

    def in_order(self, node):
        if node is None:
            return

        self.in_order(node.left)
        print(node.value)
        self.in_order(node.right)
        return

    def post_order(self, node):
        if node is None:
            return

        self.post_order(node.left)
        self.post_order(node.right)
        print(node.value)
        return

    def bfs(self):
        node_queue = queue_practice.Queue()
        node_queue.enqueue(self.head)

        while not node_queue.is_empty():
            current = node_queue.dequeue()
            print(current.value)
            if current.left is not None:
                node_queue.enqueue(current.left)
            if current.right is not None:
                node_queue.enqueue(current.right)

    def dfs(self):
        node_stack = stack_practice.Stack()
        node_stack.push(self.head)

        while not node_stack.is_empty():
            current = node_stack.pop()
            print(current.value)
            if current.left is not None:
                node_stack.push(current.left)
            if current.right is not None:
                node_stack.push(current.right)



# implementation test

bst = BST()
print(bst.head)

for x in [5,6,4,3,1,2]:
    bst.add(x)

print(bst.head.value)
print(bst.head.right.value)
print(bst.head.left.value)
print(bst.head.left.left.value)
print(bst.head.left.left.left.value)
print(bst.head.left.left.left.right.value)

bst.search(0, bst.head)

print(bst.minimum(bst.head))
bst.add(-9)
print(bst.minimum(bst.head))
print(bst.maximum(bst.head))
bst.add(28)
print(bst.maximum(bst.head), '\n\n')

bst.pre_order(bst.head)
print('\n')
bst.in_order(bst.head)
print('\n')
bst.post_order(bst.head)
print('\n')

print('bfs test')
bst.bfs()

print('\ndfs test')
bst.dfs()
