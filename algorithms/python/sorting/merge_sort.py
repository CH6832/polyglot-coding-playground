def merge_sort(input_list: list):
    """Merge sort"""
    # check if list exists
    if len(input_list) > 1:
        # finding mid of list, ...
        mid = len(input_list)//2
        # dividing the list elems ...
        left_part = input_list[:mid]
        # into 2 halves
        right_part = input_list[mid:]
 
        # sorting both halfs
        merge_sort(left_part)
        merge_sort(right_part)

        i = j = k = 0

        # copy data to temp lists
        while i < len(left_part) and j < len(right_part):
            if left_part[i] <= right_part[j]:
                input_list[k] = left_part[i]
                i += 1
            else:
                input_list[k] = right_part[j]
                j += 1
            k += 1

        # check if element was left
        while i < len(left_part):
            input_list[k] = left_part[i]
            i += 1
            k += 1

        while j < len(right_part):
            input_list[k] = right_part[j]
            j += 1
            k += 1
