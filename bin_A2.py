from avl import AVLTree
from node import Node
from object import Object, Color
from exceptions import NoBinFoundException

class Bin:
    def __init__(self, bin_id, capacity):
        self.id = bin_id
        self.capacity = capacity
        self.rem_capacity = capacity
        self.avlt = AVLTree()
        self.is_bin=1  

    def add_object(self, object):
        new_obj=Node(object.id, object)
        self.avlt.insert(new_obj)
        
        self.rem_capacity -= object.size  # Update remaining capacity
        object.stored_bin_id = self.id  # Set the bin ID for the object

    def remove_object(self, object_id):
        node_to_remove = self.avlt.search_id(object_id)

        if node_to_remove is None:
            raise NoBinFoundException
        self.avlt.delete(object_id,node_to_remove.value.size)
        self.rem_capacity += node_to_remove.value.size

