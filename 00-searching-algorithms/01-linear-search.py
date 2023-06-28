# Linear Search

class LinearSearch:
    def __init__(self, array, num):
        self.array = sorted(array)
        self.num = num
    # Best-case: O(1)
    # Worst-case: O(n)
    # Average-case: O(n)
    def linear_search(self, array=None, num=None):
        for i in range(len(self.array)):
            if self.array[i] == self.num:
                return i
        return -1


    # This approach could be considered less efficient
    # Best-case: O(1)
    # Worst-case: O(n)
    # Average-case: O(n)
    def linear_search_two_pointers(self, array=None, num=None):
        left = 0
        right = len(self.array) - 1

        # moving from the left and right
        while left <= right:

            # if found from the left side
            if self.array[left] == self.num:
                return left

            # if found from right side
            if self.array[right] == self.num:
                return right

            left = left + 1
            right = right - 1

        return -1

    # This approach is only better for average case for sorted arrays
    # Best-case: O(1)
    # Worst-case: O(n)
    # Average-case: O(n)
    def linear_search_sorted_array(self, array=None, num=None):
        sorted_array = sorted(self.array)
        for i in range(len(sorted_array)):
            if sorted_array[i] == self.num:
                return True
            if sorted_array[i] > self.num:
                return False
        return False

if __name__ == "__main__":
    array = list(map(int, input().split()))
    num = int(input())
    print("Array to search:", array)
    print("Element to search:", num)

    lsearch = LinearSearch(array, num)
    print("\nSimple Linear Search")
    result = lsearch.linear_search()
    if result != -1:
        print("Number found at position:", result + 1)
    else:
        print("Number not found!")

    print("\nLinear Search Using Two Pointers")
    result = lsearch.linear_search_two_pointers()
    if result != -1:
        print("Number found at position:", result + 1)
    else:
        print("Number not found!")

    print("\nLinear Search for Sorted Array")
    result = lsearch.linear_search_sorted_array()
    if result != -1:
        print("Number found at position:", result + 1)
    else:
        print("Number not found!")
