class Node:

    def __init__(self,value= None,next=None):
        self.value = value
        self.next  = next 
    
    def __str__(self,value):
        string = str(self.value)
        if self.next:
            string+" -> "+str(self.next)
        return string
    

class Stack:

    def __init__(self):
        self.head = None
        self.minVal = None
    
    def push(self,value):
        
        if self.minVal and (self.minVal < value):
            self.minVal = Node(value=self.minVal.value,next=self.minVal)
        
        else:
            self.minVal = Node(value=value,next = self.minVal)
            
        self.top = Node(value=value,next=self.top)

    def pop(self):
        self.minVal = self.minVal.next
        self.top    = self.top.next
        


minval =value
minVal.next = Node()