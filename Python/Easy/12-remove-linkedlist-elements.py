# 203. Remove Linked List Elements
# https://leetcode.com/problems/remove-linked-list-elements/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return head
        currentNode = ListNode('-inf', head)
        while currentNode.next is not None:
            nextNode = currentNode.next
            if nextNode.val == val:
                poppedNode = nextNode
                if head == poppedNode:
                    head = poppedNode.next
                currentNode.next = poppedNode.next
                poppedNode.next = None
            else:
                currentNode = currentNode.next
        return head


        