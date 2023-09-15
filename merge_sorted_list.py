# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        
        return dummy.next

"""
How to go about solving this problem is pretty simple but we have to understand the 
nature of the data structure used. That is a linked list, a linked list is a sequential linear 
data structure in which every element is seperate object called a node, which has two parts
-data
-reference. 

In the example above the we can create a node from the ListNode class, the class an object of that 
class has two attributes, 'val' and 'next'. The 'next' attribute keeps the reference of the subsequent element

step1. Initialize a dummy node.
The dummy node will be the new list that will be created from merging.
'current' is the reference to the dummy node. Note the current will be used 
as a joiner between two elements.

- we first use the while loop and compare if the two lists have any elemts and execute the while condition.
- compare the value of the first element to that of the second element. NB. looping two lists at the same time
- if true, 'current' will reference to the first element and remember current is also a reference of the dummy node
  in other terms we have initialized our new linkedlist.
- since we have appended 'list1' to current.next then we have to move to the next element and we do so by 'list1 = list1.next' 
  because the 'list1.next' is the reference to the next element.
- In the else block we will use the above logic.
- Remember 'current = current.next', this line moves the current to point to the last node.
- The last block of if code checks if there's anymore elements left in either of the lists above and append it 'current.next'
- The return block will return the new linked list

"""