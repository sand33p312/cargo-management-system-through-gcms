# def delete(self, key,val):
#         curr = self.root
#         while curr:
#             if key < curr.key:
#                 curr = curr.left
#             elif key > curr.key:
#                 curr = curr.right
#             else:
#                 if val == curr.value.bin_id:
#                     break
#                 elif val < curr.value:
#                     curr = curr.left
#                 else:
#                     curr = curr.right

#         if curr is None:
#             return
#         if curr.left is None and curr.right is None: 
#             if curr.parent is None:
#                 self.root = None
#             elif curr == curr.parent.left:
#                 curr.parent.left = None
#             else:
#                 curr.parent.right = None

#         elif curr.left is None:  
#             if curr.parent is None:  
#                 self.root = curr.right
#                 self.root.parent = None
#             elif curr == curr.parent.left:
#                 curr.parent.left = curr.right
#             else:
#                 curr.parent.right = curr.right
#             curr.right.parent = curr.parent

#         elif curr.right is None:  
#             if curr.parent is None:  
#                 self.root = curr.left
#                 self.root.parent = None
#             elif curr == curr.parent.left:
#                 curr.parent.left = curr.left
#             else:
#                 curr.parent.right = curr.left
#             curr.left.parent = curr.parent

#         else:
#             successor = self.lowValue(curr.right)
#             self.delete(successor.key,successor.value.bin_id)
#             successor.left=curr.left
#             successor.right=curr.right
#             curr.left.parent=successor
#             curr.right.parent=successor
#             if curr.parent==None:
#                 self.root=successor
#                 self.root.parent=None
#             else:
#                 successor.parent=curr.parent
#                 curr = successor

#         temp = curr.parent
#         while temp is not None:
#             bf = self.balFac(temp)
            
#             # Left-heavy
#             if bf > 1 and self.balFac(temp.left) >= 0:
#                 self.rightRotate(temp)
#             elif bf > 1 and self.balFac(temp.left) < 0:
#                 self.leftRotate(temp.left)
#                 self.rightRotate(temp)

#             # Right-heavy
#             elif bf < -1 and self.balFac(temp.right) <= 0:
#                 self.leftRotate(temp)
#             elif bf < -1 and self.balFac(temp.right) > 0:
#                 self.rightRotate(temp.right)
#                 self.leftRotate(temp)

#             temp = temp.parent
    
# def delete_object(self, object_id):
#         # Implement logic to remove an object from its bin
#         curr=self.avl_obj.root
#         while(curr.key!=object_id):
#             if object_id<curr.key:
#                 curr=curr.left
#             else:
#                 curr=curr.right
#         self.avl_obj.delete(object_id,curr.value)
#         Obin_id=curr.value.stored_bin_id
#         temp=self.avl_id.root
#         while(temp.key!=Obin_id):
#             if Obin_id<temp.key:
#                 temp=temp.left
#             else:
#                 temp=temp.right
#         temp.value.remove_object(object_id)
#         temp.value.stored_bin_id=None
    
# def remove_object(self, object_id):
#     temp=self.avlt.search_id(object_id)
#     self.avlt.delete(object_id,temp)


# def blue_cl(self,root,obj):
#         curr=root
#         while(curr.left!=None):
#             if obj.size<curr.key and obj.size<=curr.left.key:
#                 curr=curr.left
#             elif obj.size>curr.key and curr.right!=None:
#                 curr=curr.right
#             elif obj.size==curr.size and curr.size==self.avl_cap.maxValue(root.left).key:
#                 curr=self.avl_cap.maxValue(root.left)
#                 break
#             else:
#                 break
            
#         return curr
    
# def yellow_cg(self,root,obj):
#     curr=root
#     while(curr.left!=None):
#         if obj.size<curr.key and obj.size<=curr.left.key:
#             curr=curr.left
#         elif obj.size>curr.key and curr.right!=None:
#             curr=curr.right
#         elif obj.size==curr.size and curr.right!=None and curr.size==self.avl_cap.lowValue(root.right):
#             curr=self.avl_cap.lowValue(root.right)
#             break
#         else:
#             break
    
#     return curr

# def red_ll(self,root,obj):
#     curr=self.avl_cap.maxValue(root)
#     if curr is not None and curr.key==self.avl_cap.maxValue(curr.left).key:
#         curr=self.avl_cap.maxValue(root.left)

#     return curr
    
# def green_lg(self,root,obj):
#     curr=self.avl_cap.maxValue(root)
    
#     return curr
    



#     def delete_object(self, object_id):
#         obj_node = self.avl_obj.search_id(object_id)
#         if obj_node is None:
#             raise ValueError(f"Object with ID {object_id} not found.")

#         bin_id = obj_node.value.stored_bin_id
#         bin_node = self.avl_id.search_id(bin_id)
#         self.avl_cap.delete(bin_node.value.rem_capacity, bin_id)
#         print(bin_node.value.rem_capacity)
#         self.avl_obj.delete(object_id, obj_node.value.size)

#         if bin_node is None:
#             raise ValueError(f"Bin with ID {bin_id} not found.")
#         bin_node.value.avlt.delete(object_id,obj_node.value.size)
#         # bin_node.value.avlt.levelPrint()

#         self.avl_cap.add(bin_node.value.rem_capacity, bin_node.value)




#     gcms = GCMS()

#     gcms.add_bin(1234, 10)
#     gcms.add_bin(4321, 20)
#     gcms.add_bin(1111, 15)

#     try:
#         gcms.add_object(8989, 6, Color.YELLOW )
#     except: 
#         print("Object 1 was not able to be added")
#     gcms.avl_cap.levelPrint()
#     print()    
    
#     try:
#         gcms.add_object(2892, 8, Color.YELLOW )
#     except: 
#         print("Object 2 was not able to be added")

#     gcms.avl_cap.levelPrint()
#     print()

#     try:
#         gcms.add_object(4839, 9, Color.YELLOW )
#     except: 
#         print("Object 3 was not able to be added")

#     gcms.avl_cap.levelPrint()
#     print()

#     try:
#         gcms.add_object(3283, 2, Color.YELLOW )
#     except: 
#         print("Object 4 was not able to be added")

#     gcms.avl_cap.levelPrint()
#     print()

#     try:
#         gcms.add_object(8983, 8, Color.YELLOW )
#     except: 
#         print("Object 5 was not able to be added")

#     gcms.avl_cap.levelPrint()
#     print('----------')
    
#     gcms.delete_object(8983)
#     print()

#     gcms.avl_obj.levelPrint()
#     print()


#     print(gcms.bin_info(1234))
#     print(gcms.bin_info(4321))
#     print(gcms.bin_info(1111))

l=[(1,2),(3,4),(0,2),(-1,9)]
# l.sort()
print(l.sort())


'''
    This file contains the class definition for the StrawHat class.
'''
from custom import Node,Heap_2
from crewmate import CrewMate
from heap import Heap
from treasure import Treasure

class StrawHatTreasury:
    '''
    Class to implement the StrawHat Crew Treasury
    '''
    
    def __init__(self, m):
        '''
        Arguments:
            m : int : Number of Crew Mates (positive integer)
        Returns:
            None
        Description:
            Initializes the StrawHat
        Time Complexity:
            O(m)
        '''
        
        # Write your code here
        self.crew=Heap_2(0,[])
        # treasure_heap=Heap(None,[])
        for i in range(m):
            new_crewmate=CrewMate()
            self.crew.insert(new_crewmate)
    
    def add_treasure(self, treasure):
        '''
        Arguments:
            treasure : Treasure : The treasure to be added to the treasury
        Returns:
            None
        Description:
            Adds the treasure to the treasury
        Time Complexity:
            O(log(m) + log(n)) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        
        # Write your code here
        min_load_crewmate=self.crew.init_array[0]
        min_load_crewmate.Treasury.append(treasure)
        min_load_crewmate.time_added.append(treasure.arrival_time)
        self.crew.extract()
        if len(self.crew.all_time_list) > 0:
            time_gap = treasure.arrival_time-self.crew.all_time_list[-1]
            min_load_crewmate.current_load+=treasure.size+time_gap
        else:
            min_load_crewmate.current_load+=treasure.size

        self.crew.insert(min_load_crewmate)
        self.crew.all_time_list.append(treasure.arrival_time) # append arrival time to commen list for all treasure

    
    def get_completion_time(self):
        '''
        Arguments:
            None
        Returns:
            List[Treasure] : List of treasures in the order of their completion after updating Treasure.completion_time
        Description:
            Returns all the treasure after processing them
        Time Complexity:
            O(n(log(m) + log(n))) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        
        # Write your code here
        
        completion_time_list=[]

        for crew_mate in self.crew.init_array:
            if len(crew_mate.Treasury)!=0:
                treasure_heap=Heap_2(1,[])
                arrival_times=crew_mate.time_added # list of arrival_times when treasure added
                treasures=crew_mate.Treasury # list of treasures
                current_time=arrival_times[0] # store first treasure arrival time.
                # print(arrival_times)
                min_p_node_now=None
                min_p_node_prev=None

                for i in range(len(treasures)):

                    priority=arrival_times[i] + treasures[i].size # priority of ith treasure at arrival time
                    treasure_node=Node(priority,treasures[i]) # make node 

                    if min_p_node_prev is None:
                        min_p_node_prev = treasure_node

                    # if priority < crew_mate.min_priority_node.priority:
                    #     treasure_heap.init_array[0].remaining_size-=arrival_times[i]-arrival_times[i-1]
                    #     # print('yesIam')
                    #     # print(crew_mate.min_priority_node.treasure.id)
                    #     # print(crew_mate.min_priority_node.remaining_size)
                    #     crew_mate.min_priority_node = treasure_node
                    #     # print(crew_mate.min_priority_node.remaining_size)
                    #     current_time=arrival_times[i]
                    # elif priority==crew_mate.min_priority_node.priority:
                    #     if treasure_node.treasure.id < crew_mate.min_priority_node.treasure.id:
                    #         crew_mate.min_priority_node.remaining_size-=arrival_times[i]-arrival_times[i-1]
                    #         crew_mate.min_priority_node = treasure_node
                    #         current_time=arrival_times[i]

                    treasure_heap.insert(treasure_node) # insert treasure_node to treasure_heap assign above

                    
                    if i>0:
                        time_spent=arrival_times[i]-arrival_times[i-1]
                    
                        while(time_spent!=0 and len(treasure_heap.init_array)):    
                            if time_spent < min_p_node_prev.remaining_size:
                                print('&&&&&&&&&&&&&&&&')
                                current_time+=time_spent
                                # print(current_time)
                                crew_mate.min_priority_node.priority-=time_spent
                                crew_mate.min_priority_node.remaining_size-=time_spent
                                # print(crew_mate.min_priority_node.remaining_size)
                                
                                time_spent=0 # update time_spent

                            elif time_spent == crew_mate.min_priority_node.remaining_size:
                                print('_fhg____*************')
                                current_time+=time_spent
                                crew_mate.min_priority_node.remaining_size-=time_spent 
                                crew_mate.min_priority_node.treasure.completion_time = current_time
                                completion_time_list.append((crew_mate.min_priority_node.treasure)) # update completion time list
                                treasure_heap.extract()
                                if len(treasure_heap.init_array)!=0:
                                    crew_mate.min_priority_node = treasure_heap.init_array[0]
                                    # print('----000')
                                    # print(current_time)
                                    # print(crew_mate.min_priority_node.treasure.id)
                                    # print(crew_mate.min_priority_node.treasure.size)
                                    # print('----000')
                                
                                time_spent=0 # update time_stemp

                            else:
                                print('hello_____-____________')
                                current_time+=crew_mate.min_priority_node.remaining_size
                                time_spent-=crew_mate.min_priority_node.remaining_size # update time_stemp
                                crew_mate.min_priority_node.remaining_size=0 #  set remaining size of this node to zero
                                crew_mate.min_priority_node.treasure.completion_time = current_time
                                completion_time_list.append((crew_mate.min_priority_node.treasure)) # update completion time list
                                treasure_heap.extract()
                                if len(treasure_heap.init_array)!=0:
                                    crew_mate.min_priority_node = treasure_heap.init_array[0]
                # print('system_____')
                # print(current_time)
                # print(crew_mate.min_priority_node.treasure.id)
                # print(crew_mate.min_priority_node.treasure.size)
                # print('system_____')
                
                while(len(treasure_heap.init_array)!=0):
                    current_time+=crew_mate.min_priority_node.remaining_size
                    crew_mate.min_priority_node.treasure.completion_time = current_time
                    completion_time_list.append((crew_mate.min_priority_node.treasure)) # update completion time list
                    treasure_heap.extract()
                    if len(treasure_heap.init_array)!=0:
                        crew_mate.min_priority_node = treasure_heap.init_array[0] 

        return completion_time_list



            
    # You can add more methods if required

# st=StrawHatTreasury(3)
# print(st.crew.init_array[0].Treasury)
# print(st.crew.init_array[1].Treasury)
# print(st.crew.init_array[2].Treasury)

# # st.add_treasure(Treasure(4,10,0))
# st.add_treasure(Treasure(1,1,1))
# st.add_treasure(Treasure(2,2,2))
# st.add_treasure(Treasure(3,3,3))

# print(st.crew.init_array[0].Treasury)
# print(st.crew.init_array[1].Treasury)
# print(st.crew.init_array[2].Treasury)
# # print(st.crew.init_array[0].time_added)
# # print(st.crew.init_array[1].time_added)
# # print(st.crew.init_array[2].time_added)

# print('___________________')
# st.get_completion_time()
# print('___________________')
# for i in range(3):
#     print(st.crew.init_array[i].current_load)