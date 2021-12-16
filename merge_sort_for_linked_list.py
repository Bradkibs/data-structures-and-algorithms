from linked_list import LinkedList

def merge_sort(lst):
    """
    Sorts a linked list in ascending order.
    -Recursively divides the linked list into sublists containing a single node
    -Repeatedly merges the sublists to produce sorted sublists until one remains
     
    Returns a sorted linked list
    """
    if lst.size() <=1:
        return lst
    
    left_half,right_half = split(lst)

    left = merge_sort(left_half)
    right= merge_sort(right_half)

    return merge(left,right)

def split(linked_list):
    """
    Divides the unsorted list at the midpoint into sublists

    """
    if linked_list == None or linked_list.head==None:
        left_half = linked_list
        right_half  = None

        return left_half,right_half
    else:
        size = linked_list.size()
        mid = size//2

        mid_node = linked_list.node_in_index(mid-1)

        left_half= linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half,right_half

def merge(left,right):
    """
    Merges two linked lists, sorting by data in nodes.
    Returns a new merged list
    """
    #create a new linked list that contains nodes form merging left and right
    merged = LinkedList()

    #Add a fake head that is discarded later
    merged.add(0)

    #set current to the head of the linked list
    curr = merged.head
    #Obtain head nodes for left and right linked lists
    left_head = left.head
    right_head = right.head
    #Iterate over left and right until we reach the tail node of either
    while left_head or right_head:
        #If the head node of left is None, we're past the tail
        #Add the tail node from right to merged linked list
        if left_head is None:
            curr.next_node = right_head
            #call next on right to set loop condition to false
            right_head= right_head.next_node
        #If the head node of the right is None, we're past the tail
        #Add the tail node from the left to the merged linked list
        elif right_head is None:
            curr.next_node = left_head
            #call next on left to set loop condition to false
            left_head = left_head.next_node
        
        else:
            #Not at either tail node
            #Obtain node data to perform comparison operations
            left_data = left_head.data
            right_data = right_head.data
            #If data on the left is less than right, set curr to left node
            if left_data < right_data:
                curr.next_node=left_head
                #Move left head to next node
                left_head = left_head.next_node
            #If data on left is greater than right, set curr to right node
            else:
                curr.next_node = right_head
                #move right head to next node
                right_head = right_head.next_node
        #Move curr to next node
        curr = curr.next_node
    #Discard fake head and set first merged node as head
    head = merged.head.next_node
    merged.head = head

    return merged
