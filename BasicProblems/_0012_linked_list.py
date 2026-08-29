class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self,val):
        new_node = Node(val)
        if(self.head == None):
            self.head = new_node
        else:
            current = self.head
            while(current.next!=None):
                current = current.next
            current.next = new_node
    def insert(self,index,val):
        new_node = Node(val)
        if(self.head == None):
            self.head = new_node
        elif(index == 0):
            new_node.next = self.head
            self.head = new_node
        else:
            count = 0
            current = self.head
            for i in range(0,index-1):
                current = current.next
            temp = current.next
            current.next = new_node
            new_node.next = temp

    def __str__(self):
        res = ""
        if(self.head):
            current = self.head
            while(current!=None):
                res += str(current.val) + " "
                current = current.next
        return res

l = LinkedList()
l.append(10)
l.append(2)
l.insert(1,101)
print(l)
