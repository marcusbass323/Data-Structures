class Node: 
    def __init__(self, value, next=None):
        self.value = value
        self.next = next 

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_to_tail(self, value):
        #Check if there is a tail
        #If there is a tail 
        if not self.tail:
            # - create a new node with value
            # - set current tail.next to new node
            new_tail = Node(value, None)
            # - set new tail node to a value of none
            self.head = new_tail
            self.tail = new_tail
        #If there's no tail
        else:
            # - Create a new node with value
            new_tail = Node(value, None)
            old_tail = self.tail
            old_tail.next = new_tail
            # - Set self.head and self.tail to the new node
            self.tail = new_tail
        self.length += 1

    def remove_head(self):
        #check if there is a head
            #if no head 
            # return None
        if not self.head:
            return None
            # - set self.head to current_head.next
        if self.head == self.tail:
            current_head = self.head
            self.head = None
        #set self.tail to None
            self.tail = None
            self.length -= 1
            return current_head.value
        else:
            current_head = self.head
            self.head = current_head.next
            self.length -= 1
            return current_head.value
           
        
        pass

    def remove_tail(self):
        #check if there is a tail
        if not self.tail:
            return None
        #If only one element
        if self.head == self.tail:
            current_tail = self.tail
            self.tail = None
            self.head = None
            self.length = self.length - 1
            return current_tail.value
        else:
            current_node = self.head
            while current_node.next != self.tail:
                current_node = current_node.next
            current_tail = self.tail
            self.tail = None
            current_node.next = None
            self.length = self.length - 1
            return current_tail.value
        #start at head and iterate to the next-to-last node

    def add_to_head(self, value):
        #check if there is a head
        if self.head is None:
        #if no head / empty list:
            #create the new node with next = None
            new_node = Node(value, None)
            #set self.head = new node
            self.head = new_node
            #set self.tail = new node
            self.tail = new_node
            #increment self.length
            self.length += 1
        #if head;
        else:
            #create the new node
            new_node = Node(value, self.head)
            #new node.next = self.head
            #set self.head = new_node
            self.head = new_node
            #increment self.length
            self.length += 1
    
    def remove_from_index(self, index):
        #check that length > i - if not return None
        if index >= self.length:
            return None
        #iterate through the loop i times:
            #prev_node = self.head
            #for i times
        for i in range(index - 1):
            prev_node = prev_node.next

            target = prev_node.next
            prev_node.next = target.next
            target.next = None
            self.length = self.length - 1

            return target.value