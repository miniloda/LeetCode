from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return head
        def calcGCD(a,b):
            while(b!=0):
                r = a%b
                a = b
                b = r
            return a
        prev = dummy = head
        curr = head.next
        while curr is not None:
            gcd = calcGCD(prev.val, curr.val)
            gcd_node = ListNode(gcd)
            gcd_node.next = curr
            prev.next = gcd_node
            prev = curr
            curr = curr.next
        return dummy

# Create the linked list
head = ListNode(18)
node2 = ListNode(6)
node3 = ListNode(10)
node4 = ListNode(3)

head.next = node2
node2.next = node3
node3.next = node4

# Initialize the solution class
solution = Solution()

# Run the test case
result = solution.insertGreatestCommonDivisor(head)

# Print the result
current = result
while current is not None:
    print(current.val, end=" -> ")
    current = current.next