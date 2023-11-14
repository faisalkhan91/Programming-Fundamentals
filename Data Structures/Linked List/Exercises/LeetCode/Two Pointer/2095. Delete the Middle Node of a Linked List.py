"""
2095. Delete the Middle Node of a Linked List
https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/?envType=study-plan-v2&envId=leetcode-75
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head):
        """
        This is an iterative solution. Initially, the length of the Linked List is traversed and the length is
        determined. The middle of the Linked List is then calculated as middle = length / 2. Again the list is traversed
        until the middle and the list pointer is manipulated by pointing the node before next to the node after next,
        i.e., deleting the middle element by removing the pointer. Then the function returns the head with the
        deleted node.
        :param head: Start of the Linked List.
        :return: head: List with the deleted middle node.
        """

        current_node = head  # Set the current node as the root node.
        length = 0
        while current_node:
            length += 1  # Calculate the length of the Linked List.
            current_node = current_node.next

        if length <= 1:  # If the list has no or one node, then return None as there is no middle node.
            return None

        middle = length // 2  # Calculate the middle node.
        current_node = head  # Set he current node to root node.

        for i in range(middle - 1):  # Traverse until the node before middle node.
            current_node = current_node.next
        # Point the node before middle nodes pointer to the node after middle node.
        current_node.next = current_node.next.next

        return head

    def deleteMiddle_two_pointer(self, head):
        """
        This solution uses the two-pointer approach. In this solution, there are two pointers, slow and fast, that are
        used to traverse the Linked List. The slow pointer iterates at the speed of 1, while the fast pointer iterates
        over the list at the speed of two nodes. The fast pointer is used an index to find the middle node as when the
        fast pointer reaches the end of the list, the slow pointer will be at the middle of the list due to 2x speed
        difference. The slow pointer can then be pointed to the node after middle node, and the head of the list with
        deleted node is returned.
        :param head: Start of the Linked List.
        :return: List with the deleted middle node.
        """

        if not head.next: return None  # If the list has one or less node return None

        slow = head  # Slow pointer starting at the root node.
        fast = head.next.next  # Fast pointer starting 2 nodes down.
        while fast and fast.next:  # Iterate until the end of the list at 2x speed.
            slow = slow.next  # This will be the middle once fast has reached the end of the list.
            fast = fast.next.next
        slow.next = slow.next.next  # Delete the middle node

        return head


head = ListNode()
head.__init__(4, ListNode(7, ListNode(1)))
execute = Solution()
print(execute.deleteMiddle(head))
