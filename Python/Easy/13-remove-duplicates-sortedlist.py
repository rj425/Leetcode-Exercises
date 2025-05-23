# 83. Remove Duplicates from Sorted List
# http://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodeSet = set()
        currentNode = head
        if head is None:
            return head
        while currentNode.next is not None:
            nodeSet.add(currentNode.val)
            nextNode = currentNode.next
            if nextNode.val in nodeSet:
                currentNode.next = nextNode.next
                nextNode.next = None
            else:
                currentNode = nextNode
        return head