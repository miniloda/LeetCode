from typing import Optional
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        prev = None
        curr1, curr2 = list1, list2
        while curr1 is not None and curr2 is not None:
            if curr1.val <= curr2.val:
                if prev is None:
                    prev = curr1
                else:
                    prev.next = curr1
                prev = curr1
                curr1 = curr1.next
            else:
                if prev is None:
                    prev = curr2
                else:
                    prev.next = curr2
                prev = curr2
                curr2 = curr2.next
        while curr1 is not None and curr2 is None:
            prev.next = curr1
            prev = curr1
            curr1 = curr1.next
        while curr2 is not None and curr1 is None:
            prev.next = curr2
            prev = curr2
            curr2 = curr2.next

        return prev

if __name__ == "__main__":
    # Create linked list 1
    linked_list1 = ListNode(1)
    linked_list1.next = ListNode(3)
    linked_list1.next.next = ListNode(4)

    # Create linked list 2
    linked_list2 = ListNode(1)
    linked_list2.next = ListNode(2)
    linked_list2.next.next = ListNode(4)

    # Create an instance of the Solution class
    solution = Solution()

    # Merge the two linked lists
    merged_list = solution.mergeTwoLists(linked_list1, linked_list2)

    # Print the merged linked list
    result = []
    while merged_list is not None:
        result.append(merged_list.val)
        merged_list = merged_list.next

    print(result)  # Output: [1, 1, 2, 3, 4,]