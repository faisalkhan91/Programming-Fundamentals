"""
21. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/?envType=study-plan&id=level-1
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time complexity is O(m+n)
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Merged is the pointer moving to the next node after each node is added. Head is the pointer to the start as we
        # need to return the starting node.
        merged = head = ListNode()  # Create a starting node.
        while list1 and list2:  # As long as there are nodes present in both the linked list keep iterating.
            if list1.val < list2.val:
                merged.next = list1
                list1 = list1.next
            else:
                merged.next = list2
                list2 = list2.next
            merged = merged.next  # Move the cursor.
        merged.next = list1 or list2  # If any node(s) left, add it to the merged list.
        return head.next  # Return from next node as the first node was created by us.
