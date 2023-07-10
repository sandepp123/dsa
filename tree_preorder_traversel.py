import QueueLinkedList as queue
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        









def preOrderTraversel(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversel(rootNode.leftChild)
    preOrderTraversel(rootNode.rightChild)
# preOrderTraversel(newBT)
print("dddddddddddddd")
def inOrderTraversel(rootNode):
    if not rootNode:
        print("dd")
        return "dd"
    # print(rootNode.data)
    inOrderTraversel(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversel(rootNode.rightChild)
# inOrderTraversel(newBT)

print("ddddddddddddd2")
def inOrderTraversel(rootNode):
    if not rootNode:
        print("dd")
        return "dd"
    # print(rootNode.data)
    postOrderTraversel(rootNode.leftChild)
    
    postOrderTraversel(rootNode.rightChild)
    print(rootNode.data)
# inOrderTraversel(newBT)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return 
    else:
        customQ = queue.Queue()
        customQ.enqueue(rootNode)

        while not(customQ.isEmpty()):
            root = customQ.dequeue()
            print(root.value.data)

            if root.value.leftChild is not None:
                customQ.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQ.enqueue(root.value.rightChild)

def levelOrderSearch(rootNode,query):
    if not rootNode:
        return 
    else:
        customQ = queue.Queue()
        customQ.enqueue(rootNode)

        while not(customQ.isEmpty()):
            root = customQ.dequeue()
            # print(root.value.data)
            if root.value.data == query:
                # print("here,root")
                return root
            
            if root.value.leftChild is not None:
                customQ.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQ.enqueue(root.value.rightChild)
        return "Elelment not found"

def levelOrderInsert(rootNode,newNode):
    if not rootNode:
        return 
    else:
        customQ = queue.Queue()
        customQ.enqueue(rootNode)

        while not(customQ.isEmpty()):
            root = customQ.dequeue()
            # print(root.value.data)

            if root.value.leftChild is not None:
                customQ.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                return "Successfully inserted in left"

            if root.value.rightChild is not None:
                customQ.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                return "Successfully inserted"
                
newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
leftChild.leftChild = tea
leftChild.rightChild = coffee
rightChild = TreeNode("Cold")
newBT.leftChild = leftChild
newBT.rightChild = rightChild
# print(levelOrderTraversal(newBT))
print(levelOrderInsert(newBT, TreeNode("vahiyat")))
levelOrderTraversal(newBT)
# print(levelOrderTraversal(newBT),"dkdk")