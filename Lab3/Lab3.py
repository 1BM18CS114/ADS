
'''Write a program to perform insertion, deletion and searching operations on a skip list.
consider the maximum number of levels to be log n where 'n' is the number of nodes in the list.'''
from math import log2
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.down = None

class linked_list:
    def __init__(self):
        self.first = None
        
    def insert(self, data):
        node = Node(data)
        # first node
        if self.first == None:
            
            self.first = node
            #print('Got here to if')
            
        
        # Less than existing first node
        elif self.first.data > data:
            #print('Got here to elif')
            

            node.next = self.first
            self.first = node
        
            

        else:   
            #print('Got here to else')
            current = self.first
            prev = None
            while current != None and current.data < data:
                prev = current
                current = current.next
            
            prev.next = node
            node.next = current
        return node
           
    def delete(self, data):
        if self.first.data == data:
            self.first = self.first.next
        
        else:
            current = self.first
            prev = None
            while current.next != None and current.data < data:
                prev = current
                current = current.next
            if current.data == data:
                prev.next = current.next
        
    def search(self, data, first):
        current = first
        c = 1
        while current.next != None and current.next.data <= data:
            current = current.next
            c += 1
        return current, c
    
    def print(self):
        arr = []
        current = self.first
        while current != None:
            
            arr.append(current.data)
            current = current.next
        print(arr)
        

class Skip_list():
    def __init__(self):
        self.lvls = []
        self.N = 0
    
    def insert(self, data):
        self.N += 1
        temp = None
        for i in range(int(log2(self.N))+1):
            if self.N % 2**i == 0:
                if i+1 > len(self.lvls):
                    lvli  = linked_list()
                    self.lvls.append(lvli)

                current = self.lvls[i].insert(data)
                current.down = temp
                temp = current
                
    def delete(self, data):
        for lvl in self.lvls:
            lvl.delete(data)

    def search(self, data):
        current = self.lvls[0].first
        current, c_whole = self.lvls[0].search(data, current)
        print('Number of nodes to travel to search for given number', c_whole)
        
        i = 1
        c = 0
        current = self.lvls[-1].first
        while i <= len(self.lvls):
            print('lvl ', i)
            current, c_step = self.lvls[-i].search(data, current)
            c += c_step
            if current.data == data:
                break
            current = current.down
            i += 1
        print('Number of nodes to travel using skip list for given number', c)

    def print(self):
        for lvl in self.lvls[::-1]:
            lvl.print()




lst = Skip_list()
lst.insert(9)
lst.insert(19)
lst.insert(8)
lst.insert(27)
lst.insert(25)
lst.insert(6)
lst.insert(12)
lst.insert(3)
lst.insert(10)
lst.insert(11)
lst.print()
lst.insert(50)
print('---------------------------------------')
lst.print()









        

