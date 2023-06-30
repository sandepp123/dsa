class Stack:
    def __init__(self,maxSize):
        self.maxSize = maxSize
        self.list     = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    def isEmpty(self):
        if self.list ==[]:
            return True
        else:
            False

    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False
    
    def push(self,value):
        if self.isFull():
            print("stack is full")
            return "Stack is full"
        else:
            self.list.append(value)
            return "The element has been successfully inserted"
    
    def peek(self):
        if self.isEmpty():
            return "There is not any element in stack"
        return self.list[-1]
    def delete(self):
        self.list = None


customStack = Stack(4)
print(customStack.isEmpty())
print(customStack.isFull())
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(13)
customStack.push(123)
print(customStack.__str__())