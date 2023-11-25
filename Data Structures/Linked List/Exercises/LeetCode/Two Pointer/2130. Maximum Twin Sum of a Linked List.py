"""
2130. Maximum Twin Sum of a Linked List
https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/?envType=study-plan-v2&envId=leetcode-75
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        list_stack = []

        while head:
            list_stack.append(head.val)
            head = head.next

        for i in range(len(list_stack) // 2):
            tail_twin = list_stack.pop()
            list_stack[i] += tail_twin

        return max(list_stack)
