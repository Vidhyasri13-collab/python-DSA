# Selection Sort in Python

def selection_sort(arr):
    n = len(arr)

    # Traverse through all elements
    for i in range(n - 1):

        # Find the minimum element
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the minimum element
        # with the current element
        if min_index != i:
            arr[i], arr[min_index] = (
                arr[min_index], arr[i]
            )

    return arr


# Main program
print("Selection Sort Program")

# Get the number of elements
n = int(input("Enter number of elements: "))

arr = []

# Read array elements
for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)

# Display original array
print("Before sorting:", arr)

# Call selection sort
sorted_arr = selection_sort(arr)

# Display sorted array
print("After sorting:", sorted_arr)

print("Sorting completed successfully!")