import QueueLinkedList as queue
class BSTNode:
    def __init__(self,data):
        self.data = data 
        self.leftChild = None
        self.rightChild = None

def insert(rootNode,value):
    
    if rootNode.data == None:
        rootNode.data = value
        
    elif value <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(value)
        else:
            insert(rootNode.leftChild,value)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(value)
        else:
            insert(rootNode.rightChild,value)

def preOrderTraversel(rootNode):
    if rootNode is None:
        return 
    print(rootNode.data)
    preOrderTraversel(rootNode.leftChild)
    preOrderTraversel(rootNode.rightChild)

    
def search(rootNode,value):
    if rootNode.data is None:
        return None
    if rootNode.data == value:
        
        print("value is found") 

    elif rootNode.data > value:
        # print("the value is found")
        if rootNode.leftChild.data == value:
            print("the value is found")
        else:
            search(rootNode.leftChild,value)
    else:
        if rootNode.rightChild == value:
            print("the value is found")

        else:
            search(rootNode.rightChild,value)

    print("value is not found")


def searchNode(rootNode, nodeValue):
    
    if rootNode.data == nodeValue:
        print("The value is found")
    elif nodeValue < rootNode.data:
        if rootNode.leftChild.data == nodeValue:
            print("The value is found")
        else:
            searchNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild.data == nodeValue:
            print("The value is found")
        else:
            searchNode(rootNode.rightChild, nodeValue)



newBST = BSTNode(5)
insert(newBST,1)
insert(newBST,20)
insert(newBST,3)
insert(newBST,40)
searchNode(newBST,21)