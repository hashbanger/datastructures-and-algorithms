class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


if __name__ == "__main__":
    # created an empty list
    llist = LinkedList()

    firstNode = Node(1)
    secondNode = Node(2)
    thirdNode = Node(3)

    # assigning the head to first node
    llist.head = firstNode
    # connecting second to the first
    llist.head.next = secondNode
    # connecting third node to the second
    secondNode.next = thirdNode

    print(llist.head.data)
    print(llist.head.next.data)
    print(llist.head.next.next.data)
