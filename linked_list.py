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
        It searches for the first node containing a data that matches the key and returns it, if item is not found it returns item: {key} not found!

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
        It takes constant time O(1) to insert the item but the traversal through the list to find the location of the insertion takes linear time O(n)
        It also takes O(n) time to calculate the size of the list  and so the total time complexity is a multiple of O(n) time which can be still expressed as O(n)
        
        """
        size_of_list = self.size()
        if size_of_list == 0:
            self.add(val)
        if pos > size_of_list:
            return f"Invalid insertion position! please insert it in a position less than {size_of_list}"
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
        elif position < 0:
            """
            When an input is less than zero it should count from the last item of the linked list.
            Takes O(n) time to find the size of the linked list but O(1) time to insert the item

            """    
            if size_of_list == 0:
                return f"Error! this list has a size of {size_of_list} nodes please add some data first"
            position = size_of_list + pos + 1

            if position < 0:
                return f"Error! the item's position is out of range"
            else:
                return self.insert(val,position)
    def remove(self, key):
        """
        It  searches first if the item is really in the linked list then removes it from its position
        It takes O(n) time to search for the item in the list and O(1) to remove it
        """
        curr = self.head
        prev = None
        found= False
        while curr and not found:
            if curr.data == key and curr is self.head:
                
                self.head = curr.next_node
                found = True
                
            elif curr.data == key:
                prev.next_node = curr.next_node
                found = True
            else:
                prev = curr
                curr = curr.next_node
        return curr
        

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
                
