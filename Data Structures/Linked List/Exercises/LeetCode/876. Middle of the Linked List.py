"""
876. Middle of the Linked List
https://leetcode.com/problems/middle-of-the-linked-list/?envType=study-plan&id=level-1
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Initial attempt, with brute force.
        """
        count = 0
        search = head
        while search:
            count += 1
            search = search.next
        middle = count//2+1
        for i in range(middle-1):
            head = head.next
        return head

    def middleNode_Optimized(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Sourced this solution from the discussions section on leetcode. It is an optimized version. Time complexity is
        O(n).
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
