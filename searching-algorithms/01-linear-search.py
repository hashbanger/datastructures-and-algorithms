# Linear Search
def linear_search(array, num):

    for i in range(len(array)):
        if array[i] == num:
            return i
    return None

def linear_search_improved(array, num):
    left = 0
    right = len(array) - 1
    position = -1

    # moving from the left and right
    while left <= right:

        # if found from the left side
        if (array[left] == num):
            position = left
            print("Element found at position", position + 1, "position with", left + 1, "attempt.")
            return

        # if found from right side
        if (array[right] == num):
            position = right
            print("Element found at position", position + 1, "position with", len(array) - right, "attempt.")
            return
        
        left = left + 1
        right = right - 1

    if (position == -1):
        print("Element not found!")

if __name__ == '__main__':
    array = list(map(int, input().split()))
    num = int(input())
    print("Array to search:", array)
    print("Element to search:", num)

    print("\nSimple Linear Search")
    result = linear_search(array, num)
    if result:
        print("Number found at position:", result + 1)
    else:
        print("Number not found!")

    print("\nLinear Search Improved")
    linear_search_improved(array, num)