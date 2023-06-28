# Linear Search

class LinearSearch:
    # Best-case: O(1)
    # Worst-case: O(n)
    # Average-case: O(n)
    def linear_search(self, array, num):
        for i in range(len(array)):
            if array[i] == num:
                return i
        return -1


    # This approach could be considered less efficient
    # Best-case: O(1)
    # Worst-case: O(n)
    # Average-case: O(n)
    def linear_search_two_pointers(self, array, num):
        left = 0
        right = len(array) - 1

        # moving from the left and right
        while left <= right:

            # if found from the left side
            if array[left] == num:
                return left

            # if found from right side
            if array[right] == num:
                return right

            left = left + 1
            right = right - 1

        return -1

    # This approach is only better for average case for sorted arrays
    # Best-case: O(1)
    # Worst-case: O(n)
    # Average-case: O(n)
    def linear_search_sorted_array(self, array, num):
        sorted_array = sorted(array)
        for i in range(len(sorted_array)):
            if sorted_array[i] == num:
                return True
            if sorted_array[i] > num:
                return False
        return False

if __name__ == "__main__":
    array = list(map(int, input().split()))
    num = int(input())
    print("Array to search:", array)
    print("Element to search:", num)

    lsearch = LinearSearch(array, num)
    print("\nSimple Linear Search")
    result = lsearch.linear_search(array, num)
    if result != -1:
        print("Number found at position:", result + 1)
    else:
        print("Number not found!")

    print("\nLinear Search Using Two Pointers")
    result = lsearch.linear_search_two_pointers(array, num)
    if result != -1:
        print("Number found at position:", result + 1)
    else:
        print("Number not found!")

    print("\nLinear Search for Sorted Array")
    result = lsearch.linear_search_sorted_array(array, num)
    if result != -1:
        print("Number found at position:", result + 1)
    else:
        print("Number not found!")
