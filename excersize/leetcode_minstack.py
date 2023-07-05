class Node():
    def __init__(self, value=None, next = None):
        self.value = value
        self.next = next
    
    def __str__(self):
        string = str(self.value)
        if self.next:
            string += ',' + str(self.next)
        return string

class MinStack():
    def __init__(self):
        self.head = None
        self.minNode = None
    
    def min(self):
        if not self.minNode:
            return None
        return self.minNode.value
    
    def push(self, item):
        if self.minNode and (self.minNode.value < item):
            self.minNode = Node(value = self.minNode.value, next=self.minNode)
        else:
            self.minNode = Node(value = item, next=self.minNode)
        self.head = Node(value=item, next=self.head)
    
    def pop(self):
        if not self.head:
            return None
        self.minNode = self.minNode.next
        item = self.head.value
        self.head = self.head.next
        return item

    def top(self):
        return self.head.value
    
    def getMin(self):
        return self.minNode.value



min_stack = MinStack()

# Test Case 1
min_stack.push(5)
min_stack.push(2)
min_stack.push(7)
min_stack.push(1)
# Expected: 1
print(min_stack.getMin())

min_stack.pop()
min_stack.pop()
# Expected: 2
print(min_stack.getMin())

# Expected: 7
print(min_stack.top())

# Test Case 2
min_stack.push(3)
min_stack.push(8)
min_stack.push(4)
min_stack.push(10)
# Expected: 3
print(min_stack.getMin())

min_stack.pop()
min_stack.pop()
# Expected: 3
print(min_stack.getMin())

# Expected: 4
print(min_stack.top())

# Test Case 3
min_stack.push(6)
min_stack.push(2)
min_stack.push(9)
min_stack.push(5)
# Expected: 2
print(min_stack.getMin())

min_stack.pop()
min_stack.pop()
# Expected: 3
print(min_stack.getMin())

# Expected: 5
print(min_stack.top())

# Test Case 4
min_stack.push(1)
min_stack.push(4)
min_stack.push(7)
min_stack.push(2)
# Expected: 1
print(min_stack.getMin())

min_stack.pop()
min_stack.pop()
# Expected: 3
print(min_stack.getMin())

# Expected: 7
print(min_stack.top())

# Test Case 5
min_stack.push(6)
min_stack.push(3)
min_stack.push(5)
min_stack.push(9)
# Expected: 1
print(min_stack.getMin())

min_stack.pop()
min_stack.pop()
# Expected: 3
print(min_stack.getMin())

# Expected: 5
print(min_stack.top())
