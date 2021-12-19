from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next = None) -> None:
        self.val: int = val
        self.next: ListNode = next

    
class Solution:
    def __init__(self) -> None:
        self.head: ListNode = None

    def get_head(self) -> ListNode:
        return self.head

    def append(self, value: int) -> None:
        if self.head == None:
            self.head = ListNode(value)
            return

        if self.head.next == None:
            self.head.next = ListNode(value)
            return

        current_node: ListNode = self.head

        while current_node.next != None:
            current_node = current_node.next

        current_node.next = ListNode(value)

    def printlist(self, node: ListNode) -> None:
        if node == None:
            print("The List is empty")
            return

        current_node: ListNode = node

        while current_node != None:
            print(current_node.val)
            current_node = current_node.next


    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return None

        current_node: ListNode = head
        prev_node: ListNode = None
        next_node: ListNode = None

        while current_node != None:
            next_node = current_node.next
            current_node.next = prev_node

            prev_node = current_node
            current_node = next_node

        head = prev_node
        return head



solution = Solution()
solution.append(1)
solution.append(2)
solution.append(3)
solution.append(4)
solution.append(5)
initialHead = solution.get_head()

reversedHead = solution.reverseList(initialHead)
solution.printlist(reversedHead)

        