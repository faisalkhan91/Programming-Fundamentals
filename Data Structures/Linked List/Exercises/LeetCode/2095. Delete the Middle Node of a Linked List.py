"""
2095. Delete the Middle Node of a Linked List
https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/?envType=study-plan-v2&envId=leetcode-75
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head):

        current_node = head
        length = 0
        while current_node:
            length += 1
            current_node = current_node.next

        middle = length // 2
        current_node = head
        if length <= 1: return None

        for i in range(middle - 1):
            current_node = current_node.next
        current_node.next = current_node.next.next

        return head


head = [1,3,4,7,1,2,6]  # This will not work since it is not a linked list object.
execute = Solution()
print(execute.deleteMiddle(head))
