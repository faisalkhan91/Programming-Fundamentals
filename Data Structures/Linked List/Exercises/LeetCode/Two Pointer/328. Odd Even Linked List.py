"""
328. Odd Even Linked List
https://leetcode.com/problems/odd-even-linked-list/description/?envType=study-plan-v2&envId=leetcode-75
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        In this solution, the two-pointer technique is used to traverse the linked list. There is a pointer for the odd
        nodes and a pointer with even nodes. As the even node will get disjointed during the process, a temporary
        pointer "placeholder" is used to track the start of the node and joined with the end of the odd nodes. The head
        of the new list is returned.
        :param head: Linked List
        :return: head: With odd and even nodes.

        Time Complexity: O(n). Space Complexity: O(1)
        """

        if not head: return head  # If the list is empty, return the head.
        odd = head  # Start of the odd node.
        even = placeholder = head.next  # Start of the even node along with a placeholder.

        while even and even.next:  # If there is a current and next even node, keep iterating.
            odd.next = odd.next.next  # Join the current odd node with the next odd node.
            even.next = even.next.next  # Join the current even node with the next even node.
            odd = odd.next  # Make the new odd node as the current odd node.
            even = even.next  # Make the next even node as the current even node.
        odd.next = placeholder  # Join the end of the odd nodes with the start of the even nodes.

        return head


head = ListNode()
head.__init__(4, ListNode(7, ListNode(1)))
execute = Solution()
print(execute.deleteMiddle(head))
