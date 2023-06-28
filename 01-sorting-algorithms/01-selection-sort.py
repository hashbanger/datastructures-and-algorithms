# Selection sort

# Best-case: O(1)
# Worst-case: O(n)
# Average-case: O(n)
def selection_sort(array):

    for i in range(len(array)):

        # take the current element as the minimum
        min_idx = i

        # look for the minimum number in the remaining array
        for j in range(i + 1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j

        # swap places with the minimum in the remaining array
        array[min_idx], array[i] = array[i], array[min_idx]

    return array


if __name__ == "__main__":
    input_array = list(map(int, input().split()))
    print("Input Array: ", input_array)
    print("Sorted Array: ", selection_sort(input_array))
