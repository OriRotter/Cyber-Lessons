from Homework.Data.ex4.NodeTree import NodeTree

lastR = NodeTree(_data=1)
lastRL = NodeTree(_data=4)
secR = NodeTree(_data =2, _right= lastR, _left=lastRL)

lastLR = NodeTree(_data=6)
firstR = NodeTree(_data=8, _left=lastLR)

root = NodeTree(_data=5, _left=secR, _right=firstR)

def printTree(root):
    if root is None:
        return
    print(root.getData())
    print("R ", end="")
    printTree(root.getRight())
    print("L ", end="")
    printTree(root.getLeft())



# אם צריך לעשות את המשימה ביעילות כי יודעים שהעץ מסודר תגיד לי אני אגיש שוב
def countAppears(root,value):
    if root is None:
        return 0
    if root.getData() == value:
        return 1+countAppears(root.getLeft(),value)+countAppears(root.getRight(),value)
    return countAppears(root.getLeft(), value) + countAppears(root.getRight(), value)


def numberContain(root,num):
    numList = list(str(num))
    for i in numList:
        if countAppears(root,int(i)) == 0:
            print("not all the numbers are in the tree.")
            return False
    print("all the numbers are in the tree.")
    return True

printTree(root)
num = countAppears(root,4)
print(num)
numberContain(root,586)
