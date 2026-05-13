"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        nodeMap = {}
        curr = head
        while (curr):
            nodeMap[curr] = Node(curr.val, None, None)
            curr = curr.next
        
        currOld, currNew = head, nodeMap.get(head, None)
        while (currOld):
            nodeMap[currOld].next   = nodeMap.get(currOld.next, None)
            nodeMap[currOld].random = nodeMap.get(currOld.random, None)

            currOld = currOld.next

        return nodeMap.get(head, None)



        