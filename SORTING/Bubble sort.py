# Bubble Sort in Python

def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        swapped = False

        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr


def display_array(arr):
    for element in arr:
        print(element, end=" ")
    print()


# Main program
numbers = []

n = int(input("Enter number of elements: "))

for i in range(n):
    value = int(input(f"Enter element {i + 1}: "))
    numbers.append(value)

print("\nOriginal array:")
display_array(numbers)

sorted_numbers = bubble_sort(numbers)

print("\nSorted array in ascending order:")
display_array(sorted_numbers)