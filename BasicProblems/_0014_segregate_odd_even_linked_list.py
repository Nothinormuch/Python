from _helper_linked_list import LinkedList

def oddEvenList(head):
        if(not head or not head.next):
            return head
        even_head = head.next

        even_prev = even_head
        odd_prev = head
        even_curr = even_head
        odd_curr = head
        
        while(True):
            if(odd_curr.next and odd_curr.next.next):
                odd_prev = odd_curr
                odd_curr = odd_curr.next.next
                odd_prev.next = odd_curr
            if(even_curr.next and even_curr.next.next):
                even_prev = even_curr
                even_curr = even_curr.next.next
                even_prev.next = even_curr
            else:
                even_curr.next = None
                break
        odd_curr.next = even_head
        return head

def test_case_1():
    A = LinkedList()
    A.append("odd1")
    A.append("Even1")
    A.append("odd2")
    print(oddEvenList(A.head))

def test_case_2():
    A = LinkedList()
    A.append("odd1")
    A.append("Even1")
    A.append("odd2")
    A.append("Even2")
    print(oddEvenList(A.head))

if __name__ == "__main__":
    test_case_1()
    test_case_2()
