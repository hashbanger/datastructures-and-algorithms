# Merge Sort
# Time complexity: O(nlogn)
# Auxilary Space: O(n)
# Merge sort is stable but it is not in-place.
# Useful for sorting linked lists
# Slower for smaller tasks
def merge(left, right, array):
    i = j = k = 0

    # copy data to array by comparing till end of either one
    while (i < len(left)) and (j < len(right)):
        if left[i] < right[j]:
            array[k] = left[i]
            i = i + 1
        else:
            array[k] = right[j]
            j = j + 1
        k = k + 1

    # copying the leftover elements
    while i < len(left):
        array[k] = left[i]
        i = i + 1
        k = k + 1

    while j < len(right):
        array[k] = right[j]
        j = j + 1
        k = k + 1

    return array


def merge_sort(array):

    # if one element, it's already sorted
    if len(array) < 2:
        return

    # calculating the middle
    mid = len(array) // 2

    # splitting arrays in two halves
    left = array[:mid]
    right = array[mid:]

    # the method is to keep splitting the array in two halves
    # till we are left with single values
    # then we start merging two values, then so on.

    # recursively sorting
    merge_sort(left)
    merge_sort(right)

    # merging the halves
    merge(left, right, array)


if __name__ == "__main__":
    input_array = list(map(int, input().split()))
    print("Input Array: ", input_array)
    merge_sort(input_array)
    print("Sorted Array: ", input_array)
