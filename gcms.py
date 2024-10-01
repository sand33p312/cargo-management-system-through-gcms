from bin import Bin
from avl import AVLTree
from object import Object, Color
from exceptions import NoBinFoundException
from node import Node

class GCMS:
    def __init__(self):
        self.avl_cap = AVLTree()  # Store bins according to capacity
        self.avl_id = AVLTree()    # Store bins according to bin_id
        self.avl_obj = AVLTree()    # Store objects according to object_id

    def add_bin(self, bin_id, capacity):
        new_bin = Bin(bin_id, capacity)
        self.avl_cap.add(new_bin.rem_capacity, new_bin)
        self.avl_id.add(new_bin.id, new_bin)

    def add_object(self, object_id, size, color):
        root = self.avl_cap.root
        obj = Object(object_id, size, color)

        if obj.color == Color.BLUE:
            curr = self.blue_cl(root, obj)
        elif obj.color == Color.YELLOW:
            curr = self.yellow_cg(root, obj)
        elif obj.color == Color.RED:
            curr = self.red_ll(root, obj)
        else:
            curr = self.green_lg(root, obj)

        if curr is None:
            raise NoBinFoundException

        if curr.key >= size:
            self.avl_cap.delete(curr.key, curr.value.id)
            curr.value.add_object(obj)
            curr.key = curr.value.rem_capacity
            self.avl_cap.add(curr.key,curr.value)
            self.avl_obj.add(object_id, obj)
        else:
            raise NoBinFoundException

    def delete_object(self, object_id):
        obj_node = self.avl_obj.search_id(object_id)
        if obj_node is None:
            raise NoBinFoundException

        bin_id = obj_node.value.stored_bin_id

        bin_node = self.avl_id.search_id(bin_id)

        if bin_node is None:
            raise NoBinFoundException

        self.avl_cap.delete(bin_node.key, bin_id)

        bin_node.value.remove_object(object_id)
        self.avl_cap.add(bin_node.value.rem_capacity,bin_node.value)
        self.avl_obj.delete(object_id,obj_node.value.size)


    def bin_info(self, bin_id):
        curr = self.avl_id.search_id(bin_id)
        if curr is not None:
            return (curr.value.rem_capacity, self.avl_id.inOrder_obj(curr.value.avlt.root, l=[]))
        

    def object_info(self, object_id):
        obj_node = self.avl_obj.search_id(object_id)
        if obj_node is not None:
            return obj_node.value.stored_bin_id
        # else:
        #     raise NoBinFoundException

    def blue_cl(self, root, obj):
        curr = root
        best_fit = None
        while curr is not None:
            if obj.size <= curr.key:  # Bin can fit the object
                best_fit = curr  # Mark as the best fit
                curr = curr.left  # Look for smaller bins
            else:
                curr = curr.right  # Look for larger bins
        return best_fit

    def yellow_cg(self,root, obj):
        best_bin = None  

        node = root
        while node is not None:
            if node.key >= obj.size:
                if best_bin is None:
                    best_bin = node
                elif node.key==obj.size:
                    best_bin=node
                    node=node.right
                    continue
                elif node.key < best_bin.key:
                    best_bin = node

                elif node.key == best_bin.key:
                    if node.value.id > best_bin.value.id:
                        best_bin = node

                node = node.left
            elif node.key<obj.size and node.right!=None:
                node = node.right
            else:
                break
            

        node=root
        while(node and best_bin!=None):
            if node.key<=best_bin.key:
                if node.key==best_bin.key:
                    best_bin=node
                node=node.right
            else:
                node=node.left

        return best_bin 


    def red_ll(self,root,obj):
        best_bin = None
        current = root
        
        while current:
            if best_bin is None or current.key > best_bin.key:
                best_bin = current
            elif current.key == best_bin.key:
                if current.value.id < best_bin.value.id:
                    best_bin = current
            
            current = current.right

        if best_bin and best_bin.left:
            left_current = best_bin.left
            while left_current:
                if left_current.key == best_bin.key:
                    if left_current.value.id < best_bin.value.id:
                        best_bin = left_current
                    left_current = left_current.left
                else:
                    left_current = left_current.right

        return best_bin

    def green_lg(self, root, obj):
        return self.avl_cap.maxValue(root)  # Simply return the max value node


