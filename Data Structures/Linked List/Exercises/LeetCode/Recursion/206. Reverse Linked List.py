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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        An Iterative approach is used in this solution. The current node is stored in a temporary variable and the head
        is made as the next node. Then the stored current node is reversed by pointing to the current reversed list and
        making it as the new reversed list.

        Time Complexity: O(n), Space Complexity: O(1).

        :param head: List that is to be reversed.
        :return: reversed: It's a reversed linked list.
        """
        reversed = None  # Set reversed to None
        while head:  # as long as there are nodes present.
            temp = head  # Store the current element in a temporary variable.
            head = head.next  # Make the head as the next node in the list
            temp.next = reversed  # Make the stored elements next point to the first element in the reversed variable.
            reversed = temp  # Make reversed as the new linked list with the temp variable added in reverse.
        return reversed

    def reverseList_recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reference: https://www.youtube.com/watch?v=G0_I-ZF0S38

        In this solution, recursion is used to reverse the Linked Lists. The base case is set such as that when the end
        of the list is reached or there are no nodes in the list, it will return None, else if there is a next node it
        will call the function recursively with the next node. Once the recursive stack is popped, the node after head
        is reversed by pointing to the current head and the current head is pointed to None.

        Time Complexity: O(n), Space Complexity: O(n)

        :param head: List that is to be reversed.
        :return: new_head: It's a reversed linked list.
        """

        if not head:  # Base case, if there is no head, return None.
            return None

        new_head = head  # Set the new head as the current head.
        if head.next:  # If there is a next node.
            new_head = self.reverseList(head.next)  # Call the function with next node recursively.
            head.next.next = head  # Reverse the list by pointing the next node to the current node.
        head.next = None  # Point the current node to None.

        return new_head

    def reverseList_recursive_clean(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Same as above, reformatted to look cleaner.
        """

        if not head or not head.next:
            return head
        new_head = head
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head
