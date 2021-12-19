class ListNode:
    def __init__(self, val: int = 0, next = None) -> None:
        self.val = val
        self.next = next


class Solution: 
    def __init__(self) -> None:
        self.head = None

    def get_head(self) -> ListNode:
        return self.head

    def append(self, val: int) -> None:
        if self.head == None:
            self.head = ListNode(val)
            return

        if self.head.next == None:
            self.head.next = ListNode(val)
            return

        current_node = self.head

        while current_node.next != None:
            current_node = current_node.next

        current_node.next = ListNode(val)

    def printlist(self, head: ListNode) -> None:
        if head == None:
            print("The List is empty")
            return

        current_node = head

        while current_node != None:
            print(current_node.val)
            current_node = current_node.next

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA == None or headB == None:
            return None

        pointerA: ListNode = headA
        pointerB: ListNode = headB

        while pointerA != pointerB:
            if pointerA == None:
                pointerA = headB

            elif pointerA != None:
                pointerA = pointerA.next

            if pointerB == None:
                pointerB = headA

            elif pointerB != None:
                pointerB = pointerB.next

        return pointerA


listA = Solution()
listB = Solution()

listA.append(4)
listA.append(1)
listA.append(8)
listA.append(4)
listA.append(5)

listB.append(5)
listB.append(6)
listB.append(1)
listB.append(8)
listB.append(4)
listB.append(5)

headA = listA.get_head()
headB = listB.get_head()

intersecting_node = listA.getIntersectionNode(headA, headB)

listA.printlist(intersecting_node)