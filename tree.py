class TreeNode:
    def __init__(self,data,children=[]):
        self.data = data
        self.children = children
    
    def __str__(self, level=0):
        ret = "   "* level +str(self.data)+"\n"
        for child in self.children:
            ret+=child.__str__(level + 1 )
        return ret

    def addChild(self,TreeNode):
        self.children.append(TreeNode)


tree = TreeNode(data='Drinks',children=[])
cold = TreeNode(data = 'Cold',children=[])
hot = TreeNode(data="Hot",children=[])
tree.addChild(cold)
tree.addChild(hot)
cold.addChild(TreeNode("Alcoholic",[]))
cold.addChild(TreeNode("Non Alcoholic",[]))
print(tree.__str__())