# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # Walk the slow pointer to the start of the second half of the list
        slow, fast = head, head
        while(fast):
            slow = slow.next
            if (fast.next):
                fast = fast.next.next
            else:
                fast = fast.next
        
        # Reverse the second half of the list
        left, right = head, self.reverse_linked_list(slow)
        
        # Merge the two lists together
        walkL, walkR = head, right
        while(walkR):
            walkL, walkR = left.next, right.next
            
            left.next = right
            right.next = walkL

            left, right = walkL, walkR
        walkL.next = None
    
    def reverse_linked_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev
        
        
        