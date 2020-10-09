'''
Given a boolean 2D matrix, find the number of islands. 
A group of connected 1's forms an island. 
For example, the below matrix contains 5 islands
{1, 1, 0, 0, 0}, 
{0, 1, 0, 0, 1}, 
{1, 0, 0, 1, 1}, 
{0, 0, 0, 0, 0}, 
{1, 0, 1, 0, 1}.
A cell in the 2D matrix can be connected to 8 neighbours. 
Use disjoint sets to implement the above scenario.
'''

# Corners connected, 1st and last col connected, 1st and last row connected


class globe:
    def __init__(self, arr):
        
        self.l_row = len(arr)
        self.l_col = len(arr[0])
        self.arr = arr

        

        self.sets = [[i*self.l_col + j for j in range(self.l_col)] for i in range(self.l_row)]
        self.weights = [[0 for j in range(self.l_col)] for i in range(self.l_row)]
    
    
    def root(self, p):
        pr, pc = p
        while self.sets[pr][pc] != pr*self.l_col + pc:
            val = self.sets[pr][pc]
            pc =  val % self.l_col
            pr = (val - pc) // self.l_row
        
        return pr, pc
            
    
    
    def union(self, p, q):
        if self.root(p) != self.root(q):
            pr, pc = self.root(p)
            qr, qc = self.root(q)
            if self.weights[pr][pc] > self.weights[qr][qc]:
                self.sets[qr][qc] = self.sets[pr][pc]
                self.weights[pr][pc] += self.weights[qr][qc]
            else:
                self.sets[pr][pc] = self.sets[qr][qc]
                self.weights[qr][qc] = self.weights[pr][pc]


    def get_dir_moves(self, row, col):
        directions = [] 

        # Up 
        if row - 1 != -1:
            directions.append([row - 1, col])

            # Top Left
            if col - 1 != -1:
                directions.append([row - 1, col - 1])
            
            # Top Right
            if col + 1 != len(self.arr[0]):
                directions.append([row - 1, col + 1])


            


        # Down 
        if row + 1 != len(self.arr):
            directions.append([row + 1, col])

            # Bottom Left
            if col - 1 != -1:
                directions.append([row + 1, col - 1])
            
            # Bottom Right
            if col + 1 != len(self.arr[0]):
                directions.append([row + 1, col + 1])

        # Left 
        if col - 1 != -1:
            directions.append([row, col - 1])

        # Right 
        if col + 1 != len(self.arr[0]):
            directions.append([row, col + 1])

        return directions
    

    def find_number_of_islands(self):
        for i in range(self.l_row):
            for j in range(self.l_col):
                if self.arr[i][j] == 1:
                    di = self.get_dir_moves(i, j)
                    for d in di:
                        if self.arr[d[0]][d[1]] == 1:
                            self.union(d, [i, j])
        return len(set(self.root([i, j]) for j in range(self.l_col) for i in range(self.l_row))) - str(self.arr).count('0')
        

arr1 = [[1, 1, 0, 0, 0], 
       [0, 1, 0, 0, 1], 
       [1, 0, 0, 1, 1], 
       [0, 0, 0, 0, 0], 
       [1, 0, 1, 0, 1]]

g = globe(arr1)
print(g.find_number_of_islands())



arr2 = [[1, 1, 0, 1, 0], 
        [0, 1, 0, 0, 1], 
        [1, 0, 0, 1, 1], 
        [0, 1, 0, 0, 0], 
        [1, 0, 1, 1, 1]]

g = globe(arr2)
print(g.find_number_of_islands())




