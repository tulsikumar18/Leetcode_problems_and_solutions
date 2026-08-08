# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        p1 = headA
        p2 = headB


        # while both pointers are not equal  , traverse this..
        while p1 != p2:

            # when both pointers are not none..move to next.. and then any of the pointers becomes None
            # Shift it to the next head, so that each of them have fair chances to move and covers equal 
            # distance..
            if p1 is not None:
                p1 = p1.next
            else:
                p1 = headB

            if p2 is not None:
                p2 = p2.next 
            else:
                p2 = headA

        return p1