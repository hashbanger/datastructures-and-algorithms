# Quick Sort
# Time Complexity:
    # Best Case: When the pivot is always the middle element O(nlogn)
    # Average case: O(nlogn)
    # Worst Case: When the pivot is smallest or largeset element O(n^2)
# Quick sort default implementation is not stable but is in-place.
def partition(array, start, end):
    pivot = array[end]
    p_index = start
    
    # iterate till the end and move 
    # all smaller elements to the left of the pivot
    # all the greater elements to the right of the pivot
    for i in range(start, end):

        # if number is smaller
        if (array[i] < pivot):

            # swap it
            array[i], array[p_index] = array[p_index], array[i]
            p_index = p_index + 1

    # move the pivot to the final middle position
    array[p_index], array[end] = array[end], array[p_index]

    return p_index

def quick_sort(array, start, end):

    # checking for valid segments
    if (start < end):
        partition_index = partition(array, start, end)

        # sorting the left partition
        quick_sort(array, start, partition_index - 1)

        # sorting the right parition
        quick_sort(array, partition_index + 1, end)

if __name__ == '__main__':
    input_array = list(map(int, input().split()))
    print("Input Array: ", input_array)
    quick_sort(input_array, 0, len(input_array)-1)
    print("Sorted Array: ", input_array)