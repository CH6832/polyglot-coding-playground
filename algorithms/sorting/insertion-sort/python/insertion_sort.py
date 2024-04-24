def insertion_sort(list_to_sort: list) -> None:
    """Insertion sort algorithm"""
    print(f"Unsorted : {list_to_sort}")
    # iterate over array to be sorted
    for i in range(1, len(list_to_sort)):
        x = list_to_sort[i] # get each element
        j = i-1 # get one position before x
        # shift until reaching index 0 or getting an element smaller than x
        while j>=0 and x<list_to_sort[j]:
            # swap here
            list_to_sort[j+1] = list_to_sort[j]
            j = j-1
        # keep as it is
        list_to_sort[j+1] = x
    print(f"Sorted : {list_to_sort}")