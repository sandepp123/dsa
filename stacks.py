class Stack:
    '''stack without length limit'''
    def __init__(self):
        self.list = []
    
    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.list ==[]:
            return True
        else:
            False
    
    def push(self,value):
        self.list.append(value)
        return """The element has been successfully inserted"""
    
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.list.pop()

    def peek(self):
        if self.isEmpty():
            return "There is not any element in stack"
        return self.list[-1]

    def delete(self):
        self.list = None
    

customStack = Stack()
print(customStack.isEmpty())
customStack.push(1)
customStack.push(2)
customStack.push(3)
# print(customStack.isEmpty())
# print(customStack.__str__())
# print(customStack.pop())
# print("E#EEEEEEE")
# print(customStack.__str__())
print(customStack.peek())