from _helper_linked_list import LinkedList

def length_of_loop(head):
    if(not head):
        return 0
    slow = head
    fast = head
    while True:
        if(not fast.next or not fast.next.next):
            return 0
        slow = slow.next
        fast = fast.next.next
        if(slow==fast):
            break
    count = 1
    slow = slow.next
    while(slow != fast):
        count += 1
        slow = slow.next
    return count

def test_case_1():
    A = LinkedList()
    A.append(1)
    A.append(2)
    A.append(3)
    A.append(4)
    A.append(5)
    A.add_loop(2)
    print(length_of_loop(A.head))

if __name__ == "__main__":
    test_case_1()
