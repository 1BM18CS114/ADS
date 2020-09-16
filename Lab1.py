'''Program-1:
Given a linked list of size N, write a program to reverse every k nodes (where k is an input to the function) in the linked list.
Sample Input 1:
Linked List: 1->2->2->4->5->6->7->8
K = 4
Output: 4 2 2 1 8 7 6 5

Sample Input 2:
Linked List: 1->2->3->4->5
K = 3
Output: 3 2 1 5 4'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.first = None
        self.last = None
    


    def create_ll(self, sample):
        arr = [int(x) for x in sample.split('->')]
        
        for i, x in enumerate(arr[::-1]):
            node = Node(x)
            node.next = self.first
            self.first = node

            #add self.last to last node
            if i == 0:
                self.last = node

    def print_list(self):
        temp = self.first
        while temp != None:
            print(temp.data)
            temp = temp.next
    
    
    
    def reverse_k(self, k):
        forward = None
        current = self.first
        prev = temp = None

        s = 0
        d = 1
        while current != None:
            if s % k == 0:
                tempb = temp
                temp = current
            
            if d == k:
                self.first = current
            
            if (d-k) % k == 0 and (d-k) != 0:
                tempb.next = current
            
            s += 1
            d += 1

            forward = current.next
            current.next = prev
            prev = current
            current = forward
        
        if s % k != 0:
            tempb.next = prev
        temp.next = None
        self.print_list()

l = Linked_list()
l.create_ll('1->2->2->4->5->6->7->8')
l.reverse_k(5)


