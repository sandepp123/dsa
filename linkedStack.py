class Node:
    def __init__(self,value):
        self.value = value
        self.next  = None
    

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        currNode = self.head
        while currNode:
            yield currNode
            currNode = currNode.next


class Stack:
    '''implementation of stack using linkedlist'''
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        # print(values)
        return "\n".join(values)
    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        else:
            return False
    
    def push(self,value):
        next_element = self.LinkedList.head
        self.LinkedList.head = Node(value)
        self.LinkedList.head.next = next_element
    
    def pop(self):
        if self.isEmpty():
            return "The stack is empty"
        head = self.LinkedList.head
        self.LinkedList.head = self.LinkedList.head.next
        head.next = None
        return head.value

    def peek(self):
        if self.isEmpty():
            return "The stack is empty"
        else:
            return self.LinkedList.head.value

    def delete(self):
        self.LinkedList.head = None

customStack = Stack()
print(customStack.isEmpty())
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
customStack.push(5)
customStack.push(7)
print(customStack.isEmpty())
print(customStack.__str__(),"here")
customStack.pop()
print(customStack.__str__(),"here2")
print(customStack.peek())