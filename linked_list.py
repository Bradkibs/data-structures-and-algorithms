class node:
    """
    models out a single node of a linked list
    it consists of the data and next node
    """
    data = None
    next_node = None

    def __init__(self,data) -> None:
        self.data = data
        

    def __repr__(self) -> str:
        return f"< Node:{self.data}>"

class linked_list:
    """
    models out a linked list which has a head initially pointing to  none

    """
    def __init__(self) -> None:
        self.head = None

    def is_empty(self):

        """checks if the head of the linked list is empty to show if the linked list is empty and returns True if its empty and False if it contains some nodes"""
        return self.head == None

    def size(self):
        """
        returns the number of nodes by traversing through the list and and adding 1 to the counter 
        takes O(n)
        """

        curr = self.head
        counter = 0

        while curr:
            counter += 1
            curr = curr.next_node

        return counter

    def add(self,data):
        """
        adds a new node at the start of the linked list
        takes O(1) time
        """
        item = node(data)
        item.next_node = self.head
        self.head = item 

    def search(self,key):
        """
        It searches for the first node containing a data that matches the key and returns it and returns item: {key} not found!

        It takes O(n) time
        """
        curr= self.head
        while curr:
            if curr.data==key:
                return curr
            else:
                curr = curr.next_node
            return f"item: {key} not found!"

    def insert(self,val,pos):
        """
        Inserts a new node at any point on the list
        It takes constant time O(1) to insert the item but the traversal through the the list to find the location of the insertion takes linear time O(n)
        
        """
        new = node(val)
        value= new 
        position = pos
        if position == 0:
            self.add(val)   
        elif position > 0:
            curr = self.head
            while position > 1:
                curr = curr.next_node
                position -= 1
            prev = curr
            next= curr.next_node
            new.next_node= next
            prev.next_node = new
            


    def __repr__(self) -> list:
        """
        represents the node from the head to the tail in a list(built in python list)
        
        """
        output = []

        curr = self.head
        
        while curr:
            if curr is self.head:
                output.append(f"[Head: {curr.data}]")
            elif curr.next_node is None:
                output.append(f"[Tail: {curr.data}]")
               
            else:
                output.append(f"{curr.data}")
            curr = curr.next_node
        joined_list= " --> ".join(output)
        return joined_list
                
