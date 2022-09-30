class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def insert_at_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" - ")
            current = current.next

    # recusive merge
    def merge(self, left, right):
        result = None

        if left is None:
            return right
        if right is None:
            return left

        if left.data <= right.data:
            result = left
            result.next = self.merge(left.next, right)
        else:
            result = right
            result.next = self.merge(left, right.next)

        return result

    def merge_sort(self, head):
        if head is None or head.next is None:
            return head

        # getting the middle element
        middle = self.get_middle(head)

        # creating second part
        next_to_middle = middle.next

        # disconnecting second part
        middle.next = None

        # applying merge sort to the left and right part
        left = self.merge_sort(head)
        right = self.merge_sort(next_to_middle)

        # merging the left and right
        sorted_list = self.merge(left, right)
        return sorted_list

    # get the middle element of the linked list
    def get_middle(self, head):
        if head is None:
            return head

        slow = head
        fast = head

        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next

        return slow


if __name__ == "__main__":
    llist = LinkedList()
    llist.insert_at_front(15)
    llist.insert_at_front(10)
    llist.insert_at_front(29)
    llist.insert_at_front(20)
    llist.insert_at_front(3)
    llist.insert_at_front(2)
    print("Before Sorting: ")
    llist.print_list()
    llist.head = llist.merge_sort(llist.head)
    print("\nAfter Sorting: ")
    llist.print_list()
