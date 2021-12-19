class ListNode: 
    def __init__(self, val: int = 0) -> None:
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def get_head(self) -> ListNode:
        return self.head

    def append(self, val: int) -> None:
        new_node = ListNode(val)
        if self.head == None:
            self.head = new_node
            return

        if self.head.next == None:
            self.head.next = new_node
            return

        current_node = self.head

        while current_node.next != None:
            current_node = current_node.next

        current_node.next = new_node

    def printlist(self, head: ListNode) -> None:
        if head == None:
            print("First provide us with some data and then try to print it OUT!!!")
            return

        current_node = head

        while current_node != None:
            print(current_node.val)
            current_node = current_node.next

    def get_node(self, val: int) -> ListNode:
        if self.head == None:
            print("First provide us with some data and then try to print it OUT!!!")
            return

        current_node = self.head

        while current_node.val != val:
            if current_node == None:
                print("Data not found")

            current_node = current_node.next

        return current_node

    def deleteNode(self, node: ListNode) -> None:
        node.val = node.next.val
        node.next = node.next.next


lList = LinkedList()
lList.append(24)
lList.append(67)
lList.append(51)
lList.append(100)

deletingNode = lList.get_node(51)
headNode = lList.get_head()

lList.deleteNode(deletingNode)
lList.printlist(headNode)