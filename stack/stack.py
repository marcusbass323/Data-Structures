from singly_linked_list import LinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []
        # self.storage = ?

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        if len(self.storage) == 0: 
            return None
        self.storage.pop()

class StackLL:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def push(self, value):
        self.storage.add_to_head(value)
    
    def pop(self):
        if len(self.storage) == 0:
            return None
        self.storage.remove_head()








class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None

class ListStack:
    def __init__(self):
        self.head = None
    
    def __len__(self):
        if self.head == None:
            return True
        else:
            return False
    
    def push(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            newnode = Node(value)
            newnode.next = self.head
            self.head = newnode
    
    def pop(self):
        if len(self) == 0:
            return None
        else:
            temp = self.head
            self.head = temp.next
            temp.next = None
            return temp.data

"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""


#An array can be troublesome due to the growing size of the array. If there isn't enough memory allocated to
#the array, we will have to start the process of re-allocating memory