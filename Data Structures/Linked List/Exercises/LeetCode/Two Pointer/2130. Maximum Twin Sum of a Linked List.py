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
        """
        This solution primarily uses stack to solve the problem. The linked list is iterated over, and all the values
        are added to the stack. Then we iterate over the stack and pop the elements from the end of the stack and add it
        to the front twin pair in the stack. Then the max value in the stack is returned.

        Time Complexity: O(n). Space Complexity: O(n).
        :param head: Given Linked List
        :return: Maximum sum of a twin pair.
        """

        list_stack = []  # Declare stack.

        while head:
            list_stack.append(head.val)  # Iterate over the list and add values to the stack.
            head = head.next

        for i in range(len(list_stack) // 2):  # Iterate only until the mid of the stack.
            tail_twin = list_stack.pop()  # Remove elements from the end and add it to the twin pair in the stack.
            list_stack[i] += tail_twin

        return max(list_stack)

    def pairSum_two_pointer(self, head: Optional[ListNode]) -> int:
        """
        In this solution, two pointers technique is utilized and more specifically the slow and fast pointer technique.
        The slow pointer iterates at 1x the speed while the fast pointer is operated at 2x the speed. Thus, a slow
        pointer reaches the middle of the linked list when the fast pointer has iterated over the whole linked list.
        The elements in the slow pointer are stored in a list and reversed once mid is reached. Then the rest of the
        remaining linked list is iterated with the slow pointer, and each new element is added with the twin pair in the
        list.

        Time Complexity: O(n). Space Complexity: O(1).

        :param head: Given Linked List
        :return: Maximum sum of a twin pair.
        """
        slow = head
        fast = head
        twin_sum = []

        while fast and fast.next:  # Iterate until the middle of the list.
            twin_sum.append(slow.val) # Insert the values form the linked list into the stack.
            slow = slow.next
            fast = fast.next.next

        twin_sum.reverse()  # Reverse the stack.
        i = 0

        while slow:  # Iterate the remaining values in the list and add it to the twin pair in the stack.
            twin_sum[i] += slow.val
            slow = slow.next
            i += 1

        return max(twin_sum)


head = ListNode()
head.__init__(4, ListNode(7, ListNode(1)))
execute = Solution()
print(execute.pairSum_two_pointer(head))
