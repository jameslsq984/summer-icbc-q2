#!/usr/bin/env python
# coding: utf-8

# In[3]:


#To identify different situation when which list is None
#By using while loop to keep pushing elements in list to complete computation

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
       
        add = 0
        result = []
        
        while l1 != None and l2 != None:
            a = l1.val
            b = l2.val
            x = a + b + add
            save = x%10
            add = x//10
            result.append(save)
            l1 = l1.next            
            l2 = l2.next
            
        while l2 == None and l1 != None:
            a = l1.val
            x = a+ add
            save = x%10
            add = x//10
            result.append(save)
            l1 = l1.next
            
        while l1 == None and l2 != None:
            b = l2.val
            x = b+ add
            save = x%10
            add = x//10
            result.append(save)
            l2 = l2.next
        if l1 == None and l2 == None:
                if add == 1:
                    result.append(add)   
            
            
        return result
                
            
        
        
        
        
        
        
        
   #

