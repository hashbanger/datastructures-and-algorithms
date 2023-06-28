# Linear Search
def binary_search(array, num):
    start = 0
    end = len(array) - 1

    while start <= end:

        # calculating the middle
        mid = (start + end) // 2

        # if element is found
        if array[mid] == num:
            return mid

        # if element is larger than middle move to right
        elif array[mid] < num:
            start = mid + 1

        # if element is smaller than middle move to left
        else:
            end = mid - 1

    return -1


def binary_search_recursive(array, num, start, end):

    # check the base condition
    if start <= end:
        # calculating middle element
        mid = (start + end) // 2

        # if the element is found
        if array[mid] == num:
            return mid

        # if element is larger than middle move to right
        elif array[mid] < num:
            return binary_search_recursive(array, num, mid + 1, end)

        # if element is smaller than middle move to left
        else:
            return binary_search_recursive(array, num, start, mid - 1)
    else:
        return -1


if __name__ == "__main__":
    array = list(map(int, input().split()))
    num = int(input())
    print("Array to search:", array)
    print("Element to search:", num)

    print("\nIterative Binary Search")
    result = binary_search(array, num)
    if result != -1:
        print("Number found at position:", result + 1)
    else:
        print("Number not found!")

    print("\nRecursive Binary Search")
    result = binary_search_recursive(array, num, 0, len(array) - 1)
    if result != -1:
        print("Number found at position:", result + 1)
    else:
        print("Number not found!")
