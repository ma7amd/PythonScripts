
class Node(object):

    # Construtor to create a node in our linkedlist
    def __init__(self, data):
        self.data = data
        self.nextNode = None

    # Function for removing a node and update or linkedlist references
    def remove(self, data, previousNode):
        if self.data == data:
            previousNode.nextNode = self.nextNode
            del self.data
            del self.nextNode
        else:
            if self.nextNode is not None:
                self.nextNode.remove(data, self)
    
    