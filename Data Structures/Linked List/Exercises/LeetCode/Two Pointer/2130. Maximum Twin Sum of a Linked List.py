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
        This solution primarily uses stack to solve the problem. The linked list is iterated over and all the values
        are added to the stack. Then we iterate over the stack and pop the elements from the end of the stack and add it
        to the front twin pair in the stack. Then the max value in the stack is returned.
        :param head:
        :return:
        """

        list_stack = []

        while head:
            list_stack.append(head.val)
            head = head.next

        for i in range(len(list_stack) // 2):
            tail_twin = list_stack.pop()
            list_stack[i] += tail_twin

        return max(list_stack)

    def pairSum_two_pointer(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        twin_sum = []

        while fast and fast.next:
            twin_sum.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        twin_sum.reverse()
        i = 0

        while slow:
            twin_sum[i] += slow.val
            slow = slow.next
            i += 1

        return max(twin_sum)


head = ListNode()
head.__init__(4, ListNode(7, ListNode(1)))
execute = Solution()
print(execute.pairSum_two_pointer(head))
