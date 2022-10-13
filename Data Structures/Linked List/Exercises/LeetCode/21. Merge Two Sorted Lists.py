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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = ListNode()
        while list1 or list2:
            if list1.val >= list2.val:
                merged.next = list2
                merged = merged.next
                list2 = list2.next
            else:
                merged.next = list1
                merged = merged.next
                list1 = list1.next

        return merged