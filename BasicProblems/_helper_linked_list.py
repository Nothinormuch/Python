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
