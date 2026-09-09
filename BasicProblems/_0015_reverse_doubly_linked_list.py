from _helper_linked_list import DLinkedList

def reverse(ll):
    if not ll.head.next:
        return ll
    prev = None
    curr = ll.head
    front = curr.next
    while(curr!=None):
        curr.prev = front
        curr.next = prev
        prev = curr
        curr = front
        if(curr):
            front = curr.next
        else:
            break
    ll.head = prev
    return ll

A = DLinkedList()
A.append(1)
A.append(3)
A.append(5)
A.append(9)
A.append(102)
reverse(A)
print(A)
