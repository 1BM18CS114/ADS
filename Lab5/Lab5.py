'''Write a program to perform insertion and deletion operations on AVL trees.'''

class Node(): 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None
        self.height = 1
  
 
class AVLtree(): 
  
    def insert(self, root, key): 
          
        # Step 1 - Perform normal BST 
        if not root: 
            return Node(key) 
        elif key < root.val: 
            root.left = self.insert(root.left, key) 
        else: 
            root.right = self.insert(root.right, key) 
  
        # Step 2 - Update the height of the  
        # ancestor node 
        root.height = 1 + max(self.get_height(root.left), 
                          self.get_height(root.right)) 
  
        # Step 3 - Get the balance factor 
        balance = self.get_balance(root) 
  
        # Step 4 - If the node is unbalanced, 
        # then try out the 4 cases 
        # Left Left 
        if balance > 1 and key < root.left.val: 
            return self.right_rotate(root) 

        # Left Right 
        if balance > 1 and key > root.left.val: 
            root.left = self.left_rotate(root.left) 
            return self.right_rotate(root)

        # Right Right 
        if balance < -1 and key > root.right.val: 
            return self.left_rotate(root) 
  
        # Right Left 
        if balance < -1 and key < root.right.val: 
            root.right = self.right_rotate(root.right) 
            return self.left_rotate(root) 
  
        return root 
   
    def delete(self, root, key): 
  
        # Step 1 - Perform standard BST delete 
        if not root: 
            return root 
  
        elif key < root.val: 
            root.left = self.delete(root.left, key) 
  
        elif key > root.val: 
            root.right = self.delete(root.right, key) 
  
        else: 
            if root.left is None: 
                temp = root.right 
                root = None
                return temp 
  
            elif root.right is None: 
                temp = root.left 
                root = None
                return temp 
  
            temp = self.get_min_value_node(root.right) 
            root.val = temp.val 
            root.right = self.delete(root.right, 
                                      temp.val) 
  
        # If the tree has only one node, 
        # simply return it 
        if root is None: 
            return root 
  
        # Step 2 - Update the height of the  
        # ancestor node 
        root.height = 1 + max(self.get_height(root.left), 
                            self.get_height(root.right)) 
  
        # Step 3 - Get the balance factor 
        balance = self.get_balance(root) 
  
        # Step 4 - If the node is unbalanced,  
        # then try out the 4 cases 
        # Left Left 
        if balance > 1 and self.get_balance(root.left) >= 0: 
            return self.right_rotate(root) 

        # Left Right 
        if balance > 1 and self.get_balance(root.left) < 0: 
            root.left = self.left_rotate(root.left) 
            return self.right_rotate(root)
        
        # Right Right 
        if balance < -1 and self.get_balance(root.right) <= 0: 
            return self.left_rotate(root)  
  
        # Right Left 
        if balance < -1 and self.get_balance(root.right) > 0: 
            root.right = self.right_rotate(root.right) 
            return self.left_rotate(root) 
  
        return root 
  
    def left_rotate(self, z): 
  
        y = z.right 
        t2 = y.left 
  
        # Perform rotation 
        y.left = z 
        z.right = t2 
  
        # Update heights 
        z.height = 1 + max(self.get_height(z.left),  
                         self.get_height(z.right)) 
        y.height = 1 + max(self.get_height(y.left),  
                         self.get_height(y.right)) 
  
        # Return the new root 
        return y 
  
    def right_rotate(self, z): 
  
        y = z.left 
        t3 = y.right 
  
        # Perform rotation 
        y.right = z 
        z.left = t3
  
        # Update heights 
        z.height = 1 + max(self.get_height(z.left), 
                          self.get_height(z.right)) 
        y.height = 1 + max(self.get_height(y.left), 
                          self.get_height(y.right)) 
  
        # Return the new root 
        return y 
  
    def get_height(self, root): 
        if not root: 
            return 0
  
        return root.height 
  
    def get_balance(self, root): 
        if not root: 
            return 0
  
        return self.get_height(root.left) - self.get_height(root.right) 
  
    def get_min_value_node(self, root): 
        if root is None or root.left is None: 
            return root 
  
        return self.get_min_value_node(root.left) 
  
    def print_tree(self, root): 
  
        if not root: 
            return
  
        print(root.val, end=" ") 
        self.print_tree(root.left) 
        self.print_tree(root.right) 

tree = AVLtree() 
root = None
  
for val in [9, 5, 10, 0, 6, 11, -1, 1, 2]: 
    root = tree.insert(root, val)
    # tree.print_tree(root)
    # print()
    

 
print("Before deletion") 
tree.print_tree(root) 
print() 
  
root = tree.delete(root, 10) 
  
print("After deletion") 
tree.print_tree(root) 
print() 