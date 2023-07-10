class BinaryTree:
    def __init__(self,size):
        self.customList = size*[None]
        self.lastusedIndex = 0
        self.maxsize = size


    def insertNode(self,value):
        if self.lastusedIndex+1==self.maxsize:
            return "Tree is full"
        self.customList[self.lastusedIndex+1] = value
        self.lastusedIndex+=1
        return "The value is successfully inserted"

    def search(self,value):
        for i in range(len(self.customList)):
            if self.customList[i]==value:
                return "Value is found"
            else:
                return "Value is found"
        
    def preOrderTraversel(self,index):
        if index > self.lastusedIndex:
            return 
        print(self.customList[index])
        self.preOrderTraversel(index*2)
        self.preOrderTraversel(index*2+1)
    def inOrderTraversel(self,index):
        if index > self.lastusedIndex:
            return 
        
        self.inOrderTraversel(index*2)
        print(self.customList[index])
        self.inOrderTraversel(index*2+1)
        

    def postOrderTraversel(self,index):
        if index > self.lastusedIndex:
            return 
        
        self.postOrderTraversel(index*2)
        self.postOrderTraversel(index*2+1)
        print(self.customList[index])
        

new_BT = BinaryTree(8)
print(new_BT.insertNode("Drinks"))
print(new_BT.insertNode("Hot"))
print(new_BT.insertNode("Cold"))
print(new_BT.insertNode("Tea"))
print(new_BT.insertNode("Coffee"))
# print(new_BT.search("Coldw"))
new_BT.postOrderTraversel(1)