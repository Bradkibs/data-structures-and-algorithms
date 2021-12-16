def merge_sort(lst):
    """ 
    It takes the list and sorts it in ascending order.
    It takes O(nlogn) time 

    It is broken down to several steps as follows

    Divide: We need to divide the list into a left and right sublists
    Conquer: We need to sort the independent lists by comparing the left and right elements and rearranging their positions
    Combine: We need to combine and sort the left and right lists 
    
    """
    if lst <=1:
        return lst

    left_list,right_list = split(lst)

     
    left = merge_sort(left_list)
    right = merge_sort(right_list)

    return merge(left,right)

def split(l):
    mid = len(l)//2
    left_half = l[:mid]
    right_half = l[mid:]
    return left_half,right_half

def merge(left,right):
    sorted_list =[]
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i+=1
        else:
            sorted_list.append(right[j])
            j+=1
    while i<len(left) :
        sorted_list.append(left[i])
        i+=1
    while j<len(right):
        sorted_list.append(right[j])
    return sorted_list