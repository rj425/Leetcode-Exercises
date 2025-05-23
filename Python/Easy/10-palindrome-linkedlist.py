# 234. Palindrome Linked List
# https://leetcode.com/problems/palindrome-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Finding Middle node first
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # Reversing the linkedlist from slow.next
        prevNode = None
        while slow is not None:
            nextNode = slow.next
            slow.next = prevNode
            prevNode = slow
            slow = nextNode
        secondHead = prevNode
        # Comparing secondHead LL with head LL
        while secondHead is not None:
            if secondHead.val == head.val:
                secondHead = secondHead.next
                head = head.next
            else:
                return False
        return True