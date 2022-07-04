# Bubble Sort
# Time Complexity: O(n^2)
# Suitable for large datasets
def bubble_sort(array):

    # number of time to run the logic
    for _ in range(len(array)-1):

        # keep swapping adjacent elements till the end of array
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
            
    return array

# Time Complexity: Best Case = O(N), Worst/Average Case = O(N^2)
def bubble_sort_optimized(array):
    
    # number of time to run the logic
    for _ in range(len(array)-1):
        swapped = True
        # keep swapping adjacent elements till the end of array
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                swapped = True

        # if no two elements were swapped
        # means array is already sorted
        if swapped == False:
            break

    return array

if __name__ == '__main__':
    input_array = list(map(int, input().split()))
    print("Input Array: ", input_array)
    print("Sorted Array: ", bubble_sort(input_array))
    print("Sorted Array: ", bubble_sort_optimized(input_array))