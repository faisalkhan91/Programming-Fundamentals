"""
142. Linked List Cycle II
https://leetcode.com/problems/linked-list-cycle-ii/?envType=study-plan&id=level-1
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """ This problem is solved using Floyd cycle detection algorithm. """
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head  # Set a slow pointer
        fast = head  # Set a fast pointer
        while fast and fast.next:
            slow = slow.next  # Move slow pointer at 1x the speed.
            fast = fast.next.next  # Move fast pointer at 2x the speed.
            if slow == fast:  # When the pointers meet that means there is a cycle.
                slow = head  # Reset the slow pointer to the head. Leave fast pointer as is.
                while slow != fast:  # To find the index where tail was looping to, keep moving slow and fast at 1x.
                    slow = slow.next
                    fast = fast.next
                return slow  # Once the slow and fast pointer meet again return any slow or fast to give the index.


# Initial Attempt, does not work on all edge cases, example: [-1,-7,7,-4,19,6,-9,-5,-2,-5], 6, since the method used
# initially was based on assumption that all the values are unique.
# class Solution:
#     def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         node_map = {}
#         if not head:
#             return
#         if head.next is None:
#             return
#         while head:
#             if head.val not in node_map and head.next is not None:
#                 node_map[head.val] = head.next.val
#                 head = head.next
#             elif head.next is None:
#                 print(node_map)
#                 return
#             else:
#                 print(node_map)
#                 return head
