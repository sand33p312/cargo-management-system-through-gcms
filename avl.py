from node import Node

def comp_1(node_1, node_2):
    pass

class AVLTree:
    def __init__(self, compare_function=comp_1):
        self.root = None
        self.size = 0
        self.comparator = compare_function
        
    def get_height(self, root1):
        if root1 is None:
            return -1
        return root1.height
        
    def balFac(self, root1):
        if root1 is None:
            return 0
        return self.get_height(root1.left) - self.get_height(root1.right)
    
    def lowValue(self, root1):
        if root1 is None:
            return None
        curr = root1
        while curr.left is not None:
            curr = curr.left
        return curr

    def maxValue(self, root1):
        if root1 is None:
            return None
        curr = root1
        while curr.right is not None:
            curr = curr.right
        return curr

    def inOrder_obj(self, root, l=None):
        if l is None:
            l = [] 
        if root is None:
            return l 
        self.inOrder_obj(root.left, l)
        l.append(root.key)
        self.inOrder_obj(root.right, l)
        return l 

    def rightRotate(self, node):
        temp = node
        temp1 = node.left
        if temp1 is None:
            return  
        temp.left = temp1.right
        if temp1.right is not None:
            temp1.right.parent = temp

        temp1.parent = temp.parent
        if temp.parent is None:  
            self.root = temp1
        elif temp == temp.parent.right:
            temp.parent.right = temp1
        else:
            temp.parent.left = temp1

        temp1.right = temp
        temp.parent = temp1

        # Update heights after rotation
        temp.height = 1 + max(self.get_height(temp.left), self.get_height(temp.right))
        temp1.height = 1 + max(self.get_height(temp1.left), self.get_height(temp1.right))

    def leftRotate(self, node):
        temp = node
        temp1 = node.right
        if temp1 is None:
            return  
        
        temp.right = temp1.left
        if temp1.left is not None:
            temp1.left.parent = temp

        temp1.parent = temp.parent
        if temp.parent is None:  
            self.root = temp1
        elif temp == temp.parent.left:
            temp.parent.left = temp1
        else:
            temp.parent.right = temp1

        temp1.left = temp
        temp.parent = temp1

        # Update heights after rotation
        temp.height = 1 + max(self.get_height(temp.left), self.get_height(temp.right))
        temp1.height = 1 + max(self.get_height(temp1.left), self.get_height(temp1.right))

    def search_id(self, key):
        curr = self.root
        while curr:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                break
        return curr

    def add(self, key, value):
        new_node = Node(key, value)
        self.insert(new_node)

    def insert(self, node):
        if self.root is None:
            self.root = node
            return self.root

        curr = self.root
        while curr:
            node.parent = curr
            if node.key < curr.key:
                if curr.left is None:
                    curr.left = node
                    break
                curr = curr.left
            elif node.key > curr.key:
                if curr.right is None:
                    curr.right = node
                    break
                curr = curr.right
            else:
                comparison = curr.value.id - node.value.id
                if comparison > 0:
                    if curr.left is None:
                        curr.left = node
                        break
                    curr = curr.left
                else:
                    if curr.right is None:
                        curr.right = node
                        break
                    curr = curr.right

        # Rebalance the tree
        self.rebalance_after_deletion(curr)

    def delete(self, key, val):
        curr = self.root
        # Locate the node to delete based on key and val
        while curr:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                
                if curr.value.is_bin == 1:
                    if val == curr.value.id:
                        break
                    elif val < curr.value.id:
                        curr = curr.left
                    else:
                        curr = curr.right
                # Object deletion logic
                else:
                    if val == curr.value.size:
                        break
                    elif val < curr.value.size:
                        curr = curr.left
                    else:
                        curr = curr.right

        if curr is None:
            return  # Node to delete was not found

        # Case 1: Node with no children (leaf node)
        if curr.left is None and curr.right is None:
            if curr.parent is None:  # Deleting the root node
                self.root = None
            elif curr == curr.parent.left:
                curr.parent.left = None
            else:
                curr.parent.right = None

        # Case 2: Node with only right child
        elif curr.left is None:
            if curr.parent is None:  # Deleting the root node
                self.root = curr.right
                self.root.parent = None
            elif curr == curr.parent.left:
                curr.parent.left = curr.right
            else:
                curr.parent.right = curr.right
            curr.right.parent = curr.parent

        # Case 3: Node with only left child
        elif curr.right is None:
            if curr.parent is None:  # Deleting the root node
                self.root = curr.left
                self.root.parent = None
            elif curr == curr.parent.left:
                curr.parent.left = curr.left
            else:
                curr.parent.right = curr.left
            curr.left.parent = curr.parent

        # Case 4: Node with two children
        else:
            successor = self.lowValue(curr.right)  # Find the in-order successor (smallest node in right subtree)

            # Manually move successor to replace curr
            if successor.parent.left == successor:
                    successor.parent.left = successor.right
            else:
                successor.parent.right = successor.right
            if successor.right is not None:
                    successor.right.parent = successor.parent


            # Replace curr with successor
            successor.left = curr.left
            successor.right = curr.right
            if curr.left is not None:
                curr.left.parent = successor
            if curr.right is not None:
                curr.right.parent = successor

            if curr.parent is None:  # Replace root
                self.root = successor
                self.root.parent = None
            else:
                successor.parent = curr.parent
                if curr == curr.parent.left:
                    curr.parent.left = successor
                else:
                    curr.parent.right = successor
            
            self.rebalance_after_deletion(successor)
            
        self.rebalance_after_deletion(curr.parent)

    def rebalance_after_deletion(self, node):
        while node is not None:
            # Update the height of the node
            node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

            # Get the balance factor
            balance = self.balFac(node)

            # Left-heavy
            if balance > 1:
                if self.balFac(node.left) >= 0:
                    self.rightRotate(node)
                else:
                    self.leftRotate(node.left)
                    self.rightRotate(node)

            # Right-heavy
            elif balance < -1:
                if self.balFac(node.right) <= 0:
                    self.leftRotate(node)
                else:
                    self.rightRotate(node.right)
                    self.leftRotate(node)

            # Move up to the parent to continue rebalancing
            node = node.parent

    def update(self, node, val):
        curr = self.root
        while curr:
            if node.key < curr.key:
                curr = curr.left
            elif node.key > curr.key:
                curr = curr.right
            else:
                break
        curr.value.rem_capacity = val
        
    def levelPrint(self):
        if self.root is None:
            return 
        l = []
        l.append(self.root)
        while len(l) != 0:
            ls = len(l)
            for i in range(ls):
                node = l.pop(0)
                if node.parent==None:
                    print(str((node.key,node.value.id,None)), end=' ')
                else:
                    print(str((node.key,node.value.id,node.parent.value.id)), end=' ')
                if node.left is not None:
                    l.append(node.left)
                if node.right is not None:
                    l.append(node.right)  
            print()

