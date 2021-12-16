from math import ceil

class ListNode:
    def  __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        self.head = None

    def getHead(self) -> ListNode:
        return self.head

    def append(self, val):
        new_node = ListNode(val)
        if(self.head == None):
            self.head = new_node
            return

        if(self.head.next == None):
            self.head.next = new_node
            return

        current_node = self.head

        while(current_node.next != None):
            current_node = current_node.next

        current_node.next = new_node

    def printList(self, head: ListNode):
        if(head == None):
            print("No Data Found")
            return

        current_node = head

        while(current_node != None):
            print(current_node.val)
            current_node = current_node.next

    def getNumberOFNodes(self, head: ListNode) -> int:
        currentNode = head
        totalNumOfNodes: int = 0

        while(currentNode != None):
            totalNumOfNodes += 1
            currentNode = currentNode.next

        return totalNumOfNodes

    def middleNode(self, head: ListNode) -> ListNode:
        if head == None:
            return None

        currentNumberOfNode = self.getNumberOFNodes(head)
        middlePoint = None

        if (currentNumberOfNode % 2 != 0):
            middlePoint = ceil(currentNumberOfNode / 2)
        else:
            middlePoint = (currentNumberOfNode // 2) + 1

        currentPoint = 1
        currentNode = head

        while currentPoint < middlePoint:
            currentNode = currentNode.next
            currentPoint += 1

        return currentNode


LinkedList = Solution()
LinkedList.append(1)
LinkedList.append(2)
LinkedList.append(3)
LinkedList.append(4)
LinkedList.append(5)
LinkedList.append(6)
currentHead = LinkedList.getHead()
midNode = LinkedList.middleNode(currentHead)
LinkedList.printList(midNode)
