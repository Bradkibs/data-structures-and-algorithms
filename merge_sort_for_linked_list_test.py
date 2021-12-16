from merge_sort_for_linked_list import merge_sort
from linked_list import LinkedList

def verify_sorted(lst):
    n = lst.size()
    if n<=1:
        return True
    b= 0 
    return lst.node_in_index(b).data < lst.node_in_index(b+1).data and verify_sorted(lst.iterator(b+1))
