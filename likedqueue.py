class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        currNode = self.head
        while currNode:
            yield currNode
            currNode.next = None

class Queue:
    def __init__(self):
        self.LinkedList = LinkedList()


    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        # print(values)
        return "\n".join(values)


    def enque(self,value):
        newNode = Node(value)
        if self.LinkedList.head = None:
            self.LinkedList.head = newNode
            self.LinkedList.tail = newNode
        
        else:
            self.LinkedList.tail.next = newNode
            self.LinkedList.tail = newNode

    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        else:
            return False


    def deque(self):
        if self.LinkedList.isEmpty():
            return "Queue is empty"
        else:
            currNode = self.LinkedList.head
            while currNode.next.next is not None:
                currNode = currNode.next
            old_tail = currNode.next
            self.LinkedList.tail = currNode
            currNode.next = None
            
