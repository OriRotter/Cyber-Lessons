class NodeTree:
    def __chackNode(self,node):
        if not isinstance(node, NodeTree) and node is not None:
            raise TypeError("Need to be a node")
    def __init__(self, _right=None, _left=None, _data=None):
        self.__chackNode(_right)
        self.__chackNode(_left)
        self.right = _right
        self.left = _left
        self.data = _data

    def getRight(self):
        return self.right

    def getLeft(self):
        return self.left

    def getData(self):
        return self.data

    def setRight(self, _right):
        self.__chackNode(_right)
        self.right = _right

    def setLeft(self, _left):
        self.__chackNode(_left)
        self.left = _left

    def setData(self, _data):
        self.data = _data
