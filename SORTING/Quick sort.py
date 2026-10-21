# Quick Sort Algorithm in Python

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    left = []
    right = []

    for i in range(len(arr) - 1):
        if arr[i] <= pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    sorted_left = quick_sort(left)
    sorted_right = quick_sort(right)

    return sorted_left + [pivot] + sorted_right


def display_array(arr):
    print("Array elements:", arr)


def main():
    arr = [45, 12, 78, 34, 23, 89, 10]

    print("Original Array:")
    display_array(arr)

    result = quick_sort(arr)

    print("Sorted Array:")
    display_array(result)


if __name__ == "__main__":
    main()