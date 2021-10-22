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

    def __repr__(self) -> list:
        """
        represents the node from the head to the tail in a list(built in python list)
        
        """
        output = []

        curr = self.head
        
        while curr:
            if curr is self.head:
                output.append(f"Head: {curr.data}")
            elif curr.next_node:
                output.append(f"{curr.next_node}")
            else:
                output.append(f"Tail: {curr.data}")
            curr = curr.next_node
        joined_list= "--> ".join(output)
        return joined_list
                
