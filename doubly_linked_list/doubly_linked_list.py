"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # create a new node
        new_node = ListNode(value)
        # if empty list:
        if self.head is None:
        # set self.head = new_node
            self.head = new_node
        # set self.tail = new_node
            self.tail = new_node
        # else:
        else:
        # set self.head.prev = new_node  
            self.head.prev = new_node
        # set self.head = new_node
            self.head = new_node
        # set new_node.next to self.head
            new_node.next = self.head
        # new_node.previous = None
            new_node.previous = None
        # increment
        self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        pass
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
         # create a new node
        new_node = ListNode(value)
        # if empty list:
        if self.head is None:
        # set self.head = new_node
            self.head = new_node
        # set self.tail = new_node
            self.tail = new_node
        # else:
        else:
        # set self.head.prev = new_node  
            self.tail.prev = new_node
        # set self.head = new_node
            self.tail = new_node
        # set new_node.next to self.head
            new_node.next = self.tail
        # new_node.previous = None
            new_node.previous = None
        # increment
        self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        pass
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        pass
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        #Check for empty pointers (remove left and right pointers that surround the node)
        #Get previous node = node.prev
        #Set prev_node.next to node.next
        #Next_node = node.next
        #Set next_node.previous = prevous_node
        #decrement length 
        #Set node.prev = None
        #Set node.next = None
        #Return node.value
        pass

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        #if length == 0 return None
        if self.length == 0:
            return None
        #if length == 1 return self.head.value
        if self.length == 1:
            return self.head.value
        #Current_max variable
        current_max = self.head.value
        #Iterate through the list
        current_node = self.head
        #stop when current_node is not None:
        while current_node is not None:
        #Compare current_max to each value and update current_max if value > current_max
            if current_max < current_node.value:
                current_max = current_node.value
        #Move current_node forward
            current_node = current_node.next
        #Return current_max
        return current_max


