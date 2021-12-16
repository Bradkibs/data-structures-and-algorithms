def verify_sorted(lst):
    n = len(lst)
    if n <=1:
        return True
    return lst[0]<lst[1] and verify_sorted[1:]