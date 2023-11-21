"""
206. Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/?envType=study-plan-v2&envId=leetcode-75
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time complexity is O(n).
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed = None  # Set reversed to None
        while head:  # as long as there are nodes present.
            temp = head  # Store the current element in a temporary variable.
            head = head.next  # Make the head as the next node in the list
            temp.next = reversed  # Make the stored elements next point to the first element in the reversed variable.
            reversed = temp  # Make reversed as the new linked list with the temp variable added in reverse.
        return reversed
