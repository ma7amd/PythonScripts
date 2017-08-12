# Declaring a LinkedList
class Node(object):
    def __init__(self, item):
        self.val = item
        self.next = None


# Add Node
    def add(self, item):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(item)


# Print list
    def printList(self):
        cur = self.head
        while cur is not None:
            print(cur.val)
            cur = cur.next


# Removing Node
    def remove(self, item):
        if self.head.val == item:
            self.head = self.head.next
        else:
            cur = self.head
            while cur.next is not None:
                if cur.val == item:
                    self.removeItem(item)
                    return
                cur = cur.next
            print("item doesn't exist in Linked list")

    def removeItem(self, item):
        cur = self.head
        while cur.next is not None:
            if cur.next.val == item:
                nextnode = cur.next.next
                cur.next = nextnode
                break


# Reverse Items in LinkedList
    def reverse(self):
        prev = None
        cur = self.head
        while cur is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.head = prev