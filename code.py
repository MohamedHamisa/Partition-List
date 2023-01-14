class Solution:
    def partition(self, head: ListNode, x: int):
        h1 = l1 = ListNode(0)
        h2 = l2 = ListNode(0)
        while head:
            if head.val < x:
                l1.next = head
                l1 = l1.next
            else:
                l2.next = head
                l2 = l2.next
            head = head.next
        l2.next = None
        l1.next = h2.next
        return h1.next

#We basically need to keep track of first and last node of each partioned sub lists, so that we can connect them later.

   # We initialize two linked lists, one for each node for which 
                        #     node.val is less than k and another for each node for which 
                        #     node.val is not less than k. We traverse the given linked list, 
                        #     and append each node to its appropriate  more or less list.
                        #     In our example,   less: 1-> 2-> 2       more: 3->5
                        #
                        #   • We attach more to less. In our example, less = 1-> 2-> 2->  3-> 5
                        #  
                        #   • We return to head and update the nodes ordering using the list of 
                        #     nodes. 


