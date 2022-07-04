# Insertion Sort
# Time Complexity: O(N^2)
# Auxilary Space: O(1)
# Efficient for small data values
# Useful for arrays which are already partially sorted
def insertion_sort(array):
    
    # moving from the 1st index to the end of the array
    for i in range(1, len(array)):
        current = array[i]
        hole = i

        # iterating backwards until we find appropriate position
        while (hole > 0) and (array[hole-1] > current):
            array[hole] = array[hole-1]
            hole = hole - 1
        
        # putting the current number to its final place
        array[hole] = current
            
    return array

if __name__ == '__main__':
    input_array = list(map(int, input().split()))
    print("Input Array: ", input_array)
    print("Sorted Array: ", insertion_sort(input_array))