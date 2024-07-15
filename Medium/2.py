from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]):
        r = 0
        curr1 = l1
        curr2 = l2
        i = 0
        nodelist = []
        while curr1 is not None or curr2 is not None:
            solution = ListNode()
            if curr1 is not None and curr2 is not None:
                summ = curr1.val + curr2.val + r
                if summ >= 10:
                    solution.val = summ - 10
                    r = summ // 10
                else:
                    solution.val = summ
                    r = 0
                curr1 = curr1.next
                curr2 = curr2.next
            elif curr1 is None and curr2 is not None:
                summ = curr2.val + r
                if summ >= 10:
                    solution.val = summ - 10
                    r = summ // 10
                else:
                    solution.val = summ
                    r = 0
                curr2 = curr2.next
            elif curr1 is not None and curr2 is None:
                summ = curr1.val + r
                if summ >= 10:
                    solution.val = summ - 10
                    r = summ // 10
                else:
                    solution.val = summ
                    r = 0
                curr1 = curr1.next
            nodelist.append(solution)
        if r > 0:
            nodelist.append(ListNode(val=r, next=None))
        for i in range(-1, -len(nodelist), -1):
            node = nodelist[i - 1]
            node.next = nodelist[i]
            nodelist[i - 1] = node
        return nodelist[0]


if __name__ == "__main__":
    l1 = ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3, next=None)))
    l2 = ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4, next=None)))
    sol = Solution()
    result = sol.addTwoNumbers(l1, l2)
    # Print the result linked list
    while result is not None:
        print(result.val, end=' ')
        result = result.next
