# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list.
# The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

    dummy = ListNode()
    head = dummy  

    while list1 and list2: # while list1 and list2 have contents ( are not None )
            
         if list1.val <= list2.val: #case list1 <= list 2
            head.next = list1 # assign to head
            list1 = list1.next # update pointer from 'list1[0]' to 'list1[1]' in array terms
                
        else: # case list1 > list2
            head.next = list2 # assign to head
            list2 = list2.next # update pointer

        head = head.next # we want to update head to the last node in the merged list

    # if our while loop terminates and we still have elements in one of the lists (one is longer than the other)
    if list1: 
        head.next = list1 # append the rest of the remaining list
    elif list2:
        head.next = list2

    return dummy.next
        


# use a dummy node to start the output off head currently looks like 0 -> None

# while list1 and list2 both have nodes
    # check if the first nodes value in list1 is less than or equal to the value of first node in list2
        # if it is head.next = value
        # shift the pointer to list1 to the next val
    # if its not
        # we know list2 is less and that becomes head.next
        # shift the pointer to list2 to the next val

    # update the head, head = head.next

    
