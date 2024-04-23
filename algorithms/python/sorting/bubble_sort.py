import matplotlib.pyplot as plt
from typing import List

def bubble_sort(arr: List[int]) -> List[int]:
    """
    Sorts a list of integers using the Bubble Sort algorithm.

    Parameters:
        arr (List[int]): The input list to be sorted.

    Returns:
        List[int]: The sorted list.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def visualize_bubble_sort(arr: List[int]) -> None:
    """
    Visualizes the Bubble Sort algorithm sorting process.

    Parameters:
        arr (List[int]): The input list to be sorted.
    """
    fig, ax = plt.subplots()
    ax.bar(range(len(arr)), arr)
    ax.set_title('Bubble Sort Visualization')
    ax.set_xlabel('Indices')
    ax.set_ylabel('Values')

    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                ax.clear()
                ax.bar(range(len(arr)), arr)
                plt.pause(0.1)

    plt.show()

# Example usage:
if __name__ == "__main__":
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]
    sorted_list = bubble_sort(unsorted_list.copy())
    print("Sorted list:", sorted_list)
    visualize_bubble_sort(unsorted_list)