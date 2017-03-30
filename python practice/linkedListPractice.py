# linked list implementation practice
class Node(object):
    def __init__(self,x):
        self.value=x
        self.next=None

class LinkedList(object):
    def __init__(self):
        self.head=None
        self.size=0

    def add(self,x):
        if (self.head == None):
            self.head=Node(x)
        else :
            current=self.head
            while (current.next != None):
                current=current.next
            current.next=Node(x)
        self.size=self.size+1

    def remove(self,x):
        # print('*** remove input(target) value check : ',x)
        # if linked list is empty list
        if (self.head == None):
            print('no nodes exist, no item was deleted')

        #if target node is first (head) node
        elif (self.head.value == x):
            temp=self.head
            self.head=self.head.next
            del temp

        else:
            current = self.head

            #list traversal
            while (current.next != None):
                # if next node is target node
                if(current.next.value == x):
                    temp=current.next
                    current.next = current.next.next
                    del temp
                    return
                current = current.next

    def print(self):
        if (self.head == None):
            print('no nodes exist')
        else :
            current=self.head
            while (current.next!= None):
                print(current.value,end="->")
                current=current.next
            print(current.value)


# linked list implementation test
link = LinkedList()

print('just create linked list object :')
link.print()
print('')

print('try remove item from empty linked list :')
link.remove(4)
print('')

print('add first node with value 9')
link.add(9)
link.print()
print('')

print('add next node with value 12')
link.add(12)
link.print()
print('')

print('add more node with value 5,6,12,0,-8')
for i in [5,6,12,0,-8]:
    link.add(i)
link.print()
print('')

print('remove first node')
link.remove(9)
link.print()
print('')

print('remove middle node (value 6)')
link.remove(6)
link.print()
print('')

print('remove last node')
link.remove(-8)
link.print()
print('')

print('remove last node again')
link.remove(0)
link.print()
print('')

print('add several nodes again : 8,23,5,-105')
for i in [8,23,5,-105]:
    link.add(i)
link.print()
print('')

print('remove middle node (value 5)')
link.remove(5)
link.print()
print('')
