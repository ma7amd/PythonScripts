'''
How to implement LinkedList in Python
'''

class ListNode:
    def __init__(self, value, pointer):
        self.value = value
        self.pointer = pointer

# here is how to insert Nodes manaualy
node4 = ListNode(31, None)
node3 = ListNode(37, node4)
node2 = ListNode(62, node3)
node1 = ListNode(19, node2)



# Here how to print a linked list
print(node1.value)
print(node2.value)
print(node3.value)
print(node4.value)



# Printing Nodes with a loop
def PrintNodesWithLoop():
    global HeadNode
    current = HeadNode
    countNodes = 0

    if (current != None):
        while (current.pointer != None):
            print(current.value)
            current = current.pointer
            countNodes += 1
        print(current.value)
        print("Count:", countNodes)
    else:
        print("Empty List")



# Craete empty lLinkedList
def createEmptyList():
    global HeadNode
    HeadNode = None



# Delete a LinkedList
def deletelinkedList():
    global HeadNode
    HeadNode = None



# How to check if the LinkedList is empty
def listIsEmpty():
    global HeadNode
    return HeadNode == None



# How to find a Node in a linkedList
def findANode(n):
    global HeadNode
    current = HeadNode

    while ((current.pointer != None) and (current.value != n)):
        current = current.pointer

        if (current.pointer == None):
            print(n, "not in the list")
        else:
            print("Found value:", current.value)




# How to insert a node in LinkedList
def insertNode(pos, n):
    global HeadNode
    current = HeadNode
    nodeX = ListNode(n, None)
    positionCounter = 1
    countNodes = 0

    if pos == 0:
        HeadNode = nodeX
        nodeX.pointer = current
    else:
        while (pos > positionCounter):
            current = current.pointer
            positionCounter = positionCounter + 1
        nodeX.pointer = current.pointer
        current.pointer = nodeX
