from typing import Optional
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = dummy = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
        return dummy.next

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