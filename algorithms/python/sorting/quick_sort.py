def quick_sort(unsorted_list: list):
    """Quick sort"""
    elements = len(unsorted_list)
    # base case
    if elements < 2:
        return unsorted_list
    current_position = 0 #Position of the partitioning element
    for i in range(1, elements): #Partitioning loop
         if unsorted_list[i] <= unsorted_list[0]:
              current_position += 1
              temp = unsorted_list[i]
              unsorted_list[i] = unsorted_list[current_position]
              unsorted_list[current_position] = temp

    temp = unsorted_list[0]
    unsorted_list[0] = unsorted_list[current_position] 
    unsorted_list[current_position] = temp #Brings pivot to it's appropriate position
    left = quick_sort(unsorted_list[0:current_position]) #Sorts the elements to the left of pivot
    right = quick_sort(unsorted_list[current_position+1:elements]) #sorts the elements to the right of pivot
    unsorted_list = left + [unsorted_list[current_position]] + right #Merging everything together 

    return unsorted_list