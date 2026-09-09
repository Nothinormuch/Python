class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
    def __str__(self):
        if not self.val:
            return None
        return "{val: "+str(self.val)+", next: "+self.next.__str__()+"}"

class LinkedList:
    def __init__(self):
        self.head = None
        self.len = 0
    def __len__(self):
        return self.len
    def __str__(self):
        return str(self.head)
    
    def append(self,val):
        new_node = Node(val)
        if(not self.head):
            self.head = new_node
            self.len += 1
            return
        curr = self.head
        while(curr.next!=None):
            curr = curr.next
        curr.next = new_node
        self.len += 1
    
    def add_loop(self,index):
        curr = self.head
        for i in range(index):
            if(curr != self.head and not curr.next):
                raise ValueError("invalid linked list index!")
            curr = curr.next
        to_node = curr
        while(curr.next != None):
            curr = curr.next
        curr.next = to_node


class DNode:
    def __init__(self,val):
        self.prev = None
        self.val = val
        self.next = None
    def __str__(self):
        if not self.val:
            return None
        return "{val: "+str(self.val)+", next: "+self.next.__str__()+"}"

class DLinkedList:
    def __init__(self):
        self.head = None
        self.len = 0
    def __len__(self):
        return self.len
    def __str__(self):
        return str(self.head)
    
    def append(self,val):
        new_node = DNode(val)
        if(not self.head):
            self.head = new_node
            self.len += 1
            return
        curr = self.head
        while(curr.next!=None):
            prev = curr
            curr = curr.next
            curr.prev = prev
        curr.next = new_node
        new_node.prev = curr
        self.len += 1
