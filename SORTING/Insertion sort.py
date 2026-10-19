# Insertion Sort in Python

def insertion_sort(arr):
    n = len(arr)

    # Traverse from the second element
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # Move elements greater than key
        # one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1

        # Place key in correct position
        arr[j + 1] = key

    return arr


# Main program
print("Insertion Sort Program")

# Get number of elements
n = int(input("Enter number of elements: "))

arr = []

# Read elements from user
for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)

# Display original array
print("Before sorting:", arr)

# Call insertion sort
sorted_arr = insertion_sort(arr)

# Display sorted array
print("After sorting:", sorted_arr)

print("Sorting completed successfully!")