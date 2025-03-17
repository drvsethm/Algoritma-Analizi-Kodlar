def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Örnek kullanım
arr = [29, 10, 14, 37, 13]
sorted_arr = insertion_sort(arr)
sorted_arr
